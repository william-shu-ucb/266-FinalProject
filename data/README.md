# StackExchange Duplicate Pair Datasets

This folder contains three derived datasets built from the Hugging Face dataset `sentence-transformers/stackexchange-duplicates`. For each config (title/body/post), we keep the original duplicate edges as positives and generate an equal number of negatives by sampling across different duplicate clusters. Clusters (connected components) are computed per config, and splits are made at the cluster level to avoid leakage.

## Contents
- `title-title-pair/` - fields `title1`, `title2`
- `body-body-pair/` - fields `body1`, `body2`
- `post-post-pair/` - fields `post1`, `post2`

Each config directory includes:
- `train.jsonl`, `val.jsonl`, `test.jsonl`: shuffled pairs with fields `{field1, field2, label}` where `label` is 1 for duplicate (original pair), 0 for non-duplicate.
- `raw_original.jsonl`: raw Hugging Face rows for the corresponding config, copied before any processing.
- `meta.json`: basic settings and counts (splits, ratios, seeds, cluster counts).
- `stats.json`: extended stats (raw pairs, unique texts, cluster counts incl. size >= 3, per-split pos/neg totals, split cluster counts, and settings).

## How the data was built
1. Load the HF config (title/body/post) and take the provided duplicate pairs as positives.
2. Build a graph where nodes are texts and edges are the given duplicates; find connected components (duplicate clusters).
3. Split clusters into train/val/test (80/10/10) to avoid cross-split leakage.
4. Keep only the original edges whose clusters fall in each split (no transitive expansion).
5. Sample negatives across different clusters at a 1:1 ratio with positives.
6. Shuffle positives and negatives together per split and write JSONL.

## Quick reference (from `stats.json`)
- `raw_pairs`: number of original HF edges used as positives before splitting.
- `unique_texts`: number of unique nodes in the graph.
- `num_clusters` / `num_clusters_ge_3`: duplicate clusters found (and how many have size >= 3, in case of A ~ B, B ~ C).
- `split_cluster_counts`: how many clusters go to train/val/test.
- `splits`: per split `positives`, `negatives`, `total`.
- `settings`: train/val/test ratios, neg_pos_ratio, seed, and field names.

## File formats
- JSONL lines: `{field1: "...", field2: "...", label: 0|1}`; field names depend on the config above.
- All text is kept as provided by HF;
