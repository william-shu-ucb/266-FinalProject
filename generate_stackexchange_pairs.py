"""
Generate duplicate and non-duplicate pairs from
`sentence-transformers/stackexchange-duplicates` with a simple DFS approach.
Runs all Hugging Face configs (title/body/post), saves the raw HF records, and writes
split JSONL files per config.
"""

import json
import random
from pathlib import Path
from typing import Dict, List, Set, Tuple

from datasets import load_dataset

# Declarative settings
BASE_OUTPUT_DIR = Path("data/stackexchange")
CONFIGS = ["title-title-pair", "body-body-pair", "post-post-pair"]
FIELD_MAP = {
    "title-title-pair": ("title1", "title2"),
    "body-body-pair": ("body1", "body2"),
    "post-post-pair": ("post1", "post2"),
}
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1
NEG_POS_RATIO = 1.0  # 1.0 => same number of negatives as positives
SEED = 42


def load_pairs_and_save_raw(
    config: str, field1: str, field2: str, raw_path: Path
) -> List[Tuple[str, str]]:
    """
    Load raw duplicate pairs from Hugging Face for a given config and write the raw
    examples to disk for comparison/debugging.
    """
    ds = load_dataset("sentence-transformers/stackexchange-duplicates", config, split="train")
    if raw_path.exists():
        raw_path.unlink()

    pairs: List[Tuple[str, str]] = []
    written = 0
    with raw_path.open("w", encoding="utf-8") as f:
        for ex in ds:
            pairs.append((ex[field1], ex[field2]))
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
            written += 1
            if written % 100000 == 0:
                print(f"{config}: wrote {written} raw rows so far...")

    print(f"{config}: wrote {written} raw rows to {raw_path}")
    return pairs


def build_graph(pairs: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """
    Build an adjacency map from the raw duplicate pairs.
    Keys are titles; values are sets of titles marked as duplicates with them.
    Example input pairs [(A,B), (B,C)] produce adjacency: A:{B}, B:{A,C}, C:{B}.
    """
    adj: Dict[str, Set[str]] = {}
    for t1, t2 in pairs:
        if t1 == t2:
            continue
        adj.setdefault(t1, set()).add(t2)
        adj.setdefault(t2, set()).add(t1)
    print(f"Graph: built adjacency for {len(adj)} unique titles.")
    return adj


def find_duplicate_clusters(adj: Dict[str, Set[str]]) -> Tuple[List[List[str]], int]:
    """
    Find duplicate clusters over the adjacency map (title -> set of duplicate titles).
    DFS walks the graph to group all duplicate titles into one cluster.
    Example: adj: A:{B}, B:{A,C}, C:{B}, X:{Y}, Y:{X}
             edges (A,B), (B,C), (X,Y)
             result clusters [[A,B,C], [X,Y]].
    """
    seen: Set[str] = set()
    res: List[List[str]] = []
    size_ge_3 = 0
    for start in adj:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        nodes: List[str] = []
        while stack:
            node = stack.pop()
            nodes.append(node)
            for nbr in adj[node]:
                if nbr not in seen:
                    seen.add(nbr)
                    stack.append(nbr)
        res.append(nodes)
        if len(nodes) >= 3:
            size_ge_3 += 1
    print(f"Found {len(res)} clusters.")
    if size_ge_3:
        print(f"Clusters with size >= 3: {size_ge_3}")
    return res, size_ge_3


def split_duplicate_clusters(num: int, rng: random.Random) -> Dict[str, List[int]]:
    """
    Shuffle duplicate clusters and split them into train/val/test sets based on the ratios.
    Example: with 10 clusters and ratios 0.8/0.1/0.1, train gets 8, val 1, test 1.
    Returns a dict with keys train/val/test mapping to lists of cluster indices.
    """
    cluster_indices = list(range(num))
    rng.shuffle(cluster_indices)
    n_train = int(TRAIN_RATIO * num)
    n_val = int(VAL_RATIO * num)
    n_test = int(TEST_RATIO * num)
    
    if n_train + n_val + n_test < num:
        n_test = num - n_train - n_val
        print(f"Adjusted test split size to {n_test} to cover all clusters.")
        
    splits = {
        "train": cluster_indices[:n_train],
        "val": cluster_indices[n_train : n_train + n_val],
        "test": cluster_indices[n_train + n_val : n_train + n_val + n_test],
    }
    print(f"Splits: train {len(splits['train'])}, val {len(splits['val'])}, test {len(splits['test'])}")
    return splits


def main() -> None:
    base_rng = random.Random(SEED)

    for config in CONFIGS:
        field1, field2 = FIELD_MAP[config]
        rng_seed = base_rng.randint(0, 10**9)
        rng = random.Random(rng_seed)
        output_dir = BASE_OUTPUT_DIR / config
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"=== Processing config: {config} ===")
        raw_path = output_dir / "raw_original.jsonl"

        print("Loading dataset and writing raw copy...")
        pairs = load_pairs_and_save_raw(config, field1, field2, raw_path)
        print(f"Loaded raw pairs: {len(pairs)}")

        print("Building graph...")
        adj = build_graph(pairs)
        print(f"Graph built with {len(adj)} nodes.")

        print("Finding duplicate clusters...")
        duplicate_clusters, clusters_ge3 = find_duplicate_clusters(adj)
        print(f"Found {len(duplicate_clusters)} duplicate clusters.")
        text_to_cluster: Dict[str, int] = {}
        for cid, texts in enumerate(duplicate_clusters):
            for text in texts:
                text_to_cluster[text] = cid

        print("Splitting clusters...")
        splits = split_duplicate_clusters(len(duplicate_clusters), rng)

        print(
            f"{config}: {len(pairs)} pairs, {len(adj)} unique texts, "
            f"{len(duplicate_clusters)} duplicate clusters. Split sizes: { {k: len(v) for k, v in splits.items()} }"
        )

        split_stats: Dict[str, Dict[str, int]] = {}
        for split_name, cluster_ids in splits.items():
            out_path = output_dir / f"{split_name}.jsonl"
            if out_path.exists():
                out_path.unlink()

            # Positives: original HF edges whose cluster belongs to this split
            cluster_set = set(cluster_ids)
            pos_pairs: List[Tuple[str, str]] = []
            for a, b in pairs:
                ca = text_to_cluster.get(a)
                cb = text_to_cluster.get(b)
                if ca is None or cb is None or ca != cb:
                    continue
                if ca not in cluster_set:
                    continue
                pos_pairs.append((a, b))
            print(f"{config}/{split_name}: collected {len(pos_pairs)} positive pairs from original edges.")

            # Negatives: sample across different clusters
            neg_target = int(len(pos_pairs) * NEG_POS_RATIO)
            neg_pairs: Set[Tuple[str, str]] = set()
            neg_samples = 0
            while len(neg_pairs) < neg_target:
                if len(cluster_ids) < 2:
                    break
                c1, c2 = rng.sample(cluster_ids, 2)
                n1 = rng.choice(duplicate_clusters[c1])
                n2 = rng.choice(duplicate_clusters[c2])
                if n1 == n2:
                    continue
                a, b = (n1, n2) if n1 <= n2 else (n2, n1)
                if (a, b) in neg_pairs:
                    continue
                neg_pairs.add((a, b))
                neg_samples += 1
                if neg_samples % 100000 == 0:
                    print(f"{config}/{split_name}: generated {neg_samples}/{neg_target} negatives so far...")
            print(f"{config}/{split_name}: generated all {neg_target} negatives.")

            # Shuffle and write combined pairs
            all_records = (
                [{field1: a, field2: b, "label": 1} for a, b in pos_pairs]
                + [{field1: a, field2: b, "label": 0} for a, b in neg_pairs]
            )
            rng.shuffle(all_records)
            written = 0
            with out_path.open("w", encoding="utf-8") as f:
                for rec in all_records:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    written += 1
                    if written % 100000 == 0:
                        print(f"{config}/{split_name}: wrote {written}/{len(all_records)} rows so far.")

            print(f"{config}/{split_name}: wrote {len(pos_pairs)} positives and {len(neg_pairs)} negatives to {out_path} (total {written})")

            split_stats[split_name] = {
                "positives": len(pos_pairs),
                "negatives": len(neg_pairs),
                "total": written,
            }

        # Metadata for reproducing the dataset
        meta = {
            "hf_config": config,
            "field1": field1,
            "field2": field2,
            "train_ratio": TRAIN_RATIO,
            "val_ratio": VAL_RATIO,
            "test_ratio": TEST_RATIO,
            "neg_pos_ratio": NEG_POS_RATIO,
            "seed": rng_seed,
            "num_titles": len(adj),
            "num_clusters": len(duplicate_clusters),
            "num_clusters_ge_3": clusters_ge3,
            "split_cluster_counts": {k: len(v) for k, v in splits.items()},
        }
        meta_path = output_dir / "meta.json"
        with meta_path.open("w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=True)
        print(f"{config}: wrote meta to {meta_path}")

        stats = {
            "config": config,
            "field1": field1,
            "field2": field2,
            "raw_pairs": len(pairs),
            "unique_texts": len(adj),
            "num_clusters": len(duplicate_clusters),
            "num_clusters_ge_3": clusters_ge3,
            "split_cluster_counts": {k: len(v) for k, v in splits.items()},
            "splits": split_stats,
            "settings": {
                "train_ratio": TRAIN_RATIO,
                "val_ratio": VAL_RATIO,
                "test_ratio": TEST_RATIO,
                "neg_pos_ratio": NEG_POS_RATIO,
                "seed": rng_seed,
            },
        }
        stats_path = output_dir / "stats.json"
        with stats_path.open("w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=True)
        print(f"{config}: wrote stats to {stats_path}")

main()
