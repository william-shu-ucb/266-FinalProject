---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:402588
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-mpnet-base-v2
widget:
- source_sentence: Before I decide on what pokemon I want to evolve, I wanted to pick
    the one with the moves or tricks I wanted to keep. But I'm unsure if evolving
    the pokemon will change the moves or tricks that is has so it really does not
    matter.
  sentences:
  - The question is prove the Hellinger-Toeplitz theorem, using the uniform boundedness
    principle. All hints are welcome
  - When is it appropriate to use that as opposed to which with relative clauses?
  - 'FYI: I am using Kubuntu 18.04  I keep getting the following error when I install
    apt-transport-https  Things I have already tired to fix this error are:  sudo
    apt-get autoremove libdvd-pkg  sudo apt-get install libdvd-pkg sudo apt-get update
    sudo apt-get install -f sudo apt-get purge apt-transport-https &amp;&amp; sudo
    apt-get install apt-transport-https   The error I continue to see is  Reading
    package lists... Done Building dependency tree        Reading state information...
    Done The following packages will be REMOVED:   apt-transport-https* 0 upgraded,
    0 newly installed, 1 to remove and 0 not upgraded. After this operation, 152 kB
    disk space will be freed. Do you want to continue? [Y/n] Y (Reading database ...
    246794 files and directories currently installed.) Removing apt-transport-https
    (1.6.6) ... libdvd-pkg: Checking orig.tar integrity... /usr/src/libdvd-pkg/libdvdcss_1.4.2.orig.tar.bz2:
    OK libdvd-pkg: `apt-get check` failed, you may have broken packages. Aborting...
    Reading package lists... Done Building dependency tree        Reading state information...
    Done The following NEW packages will be installed:   apt-transport-https 0 upgraded,
    1 newly installed, 0 to remove and 0 not upgraded. Need to get 1,692 B of archives.
    After this operation, 152 kB of additional disk space will be used. Get:1 http://ca.archive.ubuntu.com/ubuntu
    bionic-updates/universe amd64 apt-transport-https all 1.6.6 [1,692 B] Fetched
    1,692 B in 0s (6,872 B/s)                Selecting previously unselected package
    apt-transport-https. (Reading database ... 246791 files and directories currently
    installed.) Preparing to unpack .../apt-transport-https_1.6.6_all.deb ... Unpacking
    apt-transport-https (1.6.6) ... Setting up apt-transport-https (1.6.6) ... libdvd-pkg:
    Checking orig.tar integrity... /usr/src/libdvd-pkg/libdvdcss_1.4.2.orig.tar.bz2:
    OK libdvd-pkg: `apt-get check` failed, you may have broken packages. Aborting...'
- source_sentence: 'I just started using XFCE and I''m loving it so far but I''ve
    yet to figure this out.   I''m having trouble removing a duplicate Google Chrome
    file in this folder. The main thing is I want to remove it from my menu since
    I have one under the Internet sub-folder in the menu and also one under Other.
    I''m OCD so this is driving me insane.   In the applications folder, the only
    thing that differentiates the two is that the duplicate just has the command entry
    (as "google-chrome" filled under properties while the other has a description
    and comment which is the one I want to keep.   I don''t know how to remove the
    duplicate since the rm command says it can''t find that directory (and I''m not
    sure how to word it exactly since they are both named the same).   I tried the
    fix of the "NoDisplay=true" but I''m not sure how to differentiate between the
    two since they both have the same name.   I also tried changing the duplicate
    to renaming it to the desktop.old extension but it said that it doesn''t exist.   I''m
    ok with uninstalling and installing again if I can be absolutely sure it removes
    both.    Edit: Sorry for the late response and thanks for those who responded.
    I should have clarified better, I''m currently using the crouton installation
    of ubuntu on an Acer C720. I have just removed Google Chrome but this second application
    in the /usr/share/applications folder is still there, although its grey and doesn''t
    launch anything since it''s uninstalled. I tried this way (How to remove single
    file from /usr directory?) by using the command BUT, the file name is Google Chrome
    (and I''ve tried google-chrome, google-chrome.desktop) and I can''t remove it
    by command because it doesn''t recognize the space, so it looks for Google and
    Chrome separately and it says No such file or directory for both (including google-chrome
    and google-chrome.desktop). Anyone have any ideas of getting rid of this thing?'
  sentences:
  - 'I am not sure which of the following sentences is correct:  To put virus-resistance
    genes in the sweet potato. To put virus-resistance genes into the sweet potato.  Could
    they both be correct? If one of the sentences above is not correct, could you
    briefly explain why? Why could not &quot;into&quot; be replaced with &quot;in&quot;
    in the following sentence?  One approach that works very well is to segment the
    market into three different areas.  Thank you.'
  - 'The following definition is needed for my actual question:  For $A, B \in \mathcal{M}_{n
    \times n}$ define $$  \langle A, B \rangle = \text{Trace}(B^{T}A) = \sum_{j=1}^{n}\sum_{i=1}^{n}b_{ij}
    \, a_{ij} $$  And here is the actual question:  For $B \in \mathcal{M}_{n \times
    n}$ show that $$ \text{Trace}(B)^{2} \:\leq\: n \,\text{Trace}(B^{T}B) $$  I know
    I have to use the Cauchy-Schwarz Inequality, but I wasn''t exactly sure how to.  Here
    is my attempt:  Since I only have one matrix I decided to use the identity matrix
    $$ \begin{align} \text{Trace}(B)^{2} \:&amp;\leq\: n \,\text{Trace}(B^{T}B) \\
    \text{Trace}(I^{T}B)^{2} \:&amp;\leq\: n \, \langle B, B \rangle \\ \langle I_{n},
    B \rangle^{2} \:&amp;\leq\: n \, \Vert B \Vert^{2} \\ \langle I_{n}, B \rangle
    \:&amp;\leq\: \sqrt{n} \, \Vert B \Vert \end{align} $$  I feel like I either did
    it incorrect, or that I''m close but am missing something.'
  - 'My main preoccupation is to find different Method to prove that the function   $$
    f :x\mapsto \frac{\sin x}{x}$$ is uniformly continuous on $\mathbb R$.  Particularly
    I am not able to prove it direct using the $\epsilon-\delta $ definition .  Here
    What is I found so far. Since $f$ is continuous and $f(x)\to 0$ as $|x|\to \infty
    $  we conclude that $f$ is uniformly continuous using  But I believe that there
    are others ways to overcome this this issue.  Edit: Note that I am asking different
    possible way to to prove the uniform continuity of $f.$'
- source_sentence: Which one is grammatically correct?        One hour and a half
    is all you have left.   One hour and a half are all you have left.   Two hours
    is all you have left.   Two hours are all you have left.      And why?
  sentences:
  - 'Possible Duplicate:             Can anyone help me determine the correct verb
    in this sentence? I am not sure what to do. If it were not such a complex introductory
    phrase, it would be more obvious. The general consensus of my friends who are
    not professional writers is that the verb should be are.   To me the question
    is whether or not the subject is singular (i.e., “a large collective volume of
    paint”, perhaps in a tank) or plural (a lot of the individual gallon containers
    of paint).  If simplified to other options, it would be like these:   Paint is
    sold. Gallons of paint are sold. More paint is sold. More gallons of paint are
    sold. More than 1000 gallons of paint is sold. [emphasis on total volume] More
    than 1000 gallons of paint are sold. [emphasis on individual containers]'
  - 'While researching another problem, I ,  locate something | xargs -I {} bash -c
    "if [ -d "{}" ]; then echo {}; fi"   that I wanted to learn more about.  So I
    ran man xargs and get the following output:  XARGS(1)                    General
    Commands Manual                   XARGS(1)  NAME        xargs - build and execute
    command lines from standard input  SYNOPSIS        xargs  [-0prtx]  [-E  eof-str]
    [-e[eof-str]] [--eof[=eof-str]] [--null]        [-d delimiter] [--delimiter delimiter]  [-I  replace-str]  [-i[replace-        str]]    [--replace[=replace-str]]   [-l[max-lines]]   [-L   max-lines]        [--max-lines[=max-lines]]
    [-n max-args] [--max-args=max-args] [-s  max-        chars]  [--max-chars=max-chars]  [-P
    max-procs] [--max-procs=max-procs]        [--interactive]      [--verbose]      [--exit]      [--no-run-if-empty]        [--arg-file=file]   [--show-limits]   [--version]   [--help]   [command        [initial-arguments]]  DESCRIPTION        This
    manual page documents the GNU version of xargs...   I am trying to get better
    at using documentation to learn about Linux programs, but that "Synopsis" section
    is intimidating to new users.  It literally looks like gibberish compared to man
    locate or man free.  So far, I understand that square brackets mean optional and
    nested brackets mean options in optional.  But how am I supposed to induce a valid
    command with that?  I am not asking for help with xargs here.  I am looking for
    help interpreting a man page to understand complicated commands.  I want to stop
    making Google-indexed web blogs and personal help from others my first approach
    to learning Linux commands.'
  - 'Some spells have somatic and vocal components, that''s well known.  How loud
    must a wizard talk? How obvious/wide should his gestures be?  Some spells that
    would be awesome would be fairly limited if you need to shout them (ex: mage hand,
    range 30ft).'
- source_sentence: 'In $\triangle ABC$, $X$ and $Y$ are points on the sides $AC$ and
    $BC$ respectively. If $Z$ is on the segment $XY$ such that $\frac{AX}{XC}=\frac{CY}{YB}=\frac{XZ}{ZY}$,
    prove that the area of $\triangle ABC$ is given by: $$ \text{area of }\triangle
    ABC=\left((\text{area of }\triangle AXZ)^{1/3} +(\text{area of }\triangle BYZ)^{1/3}\right)^3
    $$'
  sentences:
  - In triangle $ABC$ , $X$ and $Y$ are points on sides $AC$ and $BC$ respectively
    . If $Z$ is on the segment $XY$ such that $\frac{AX}{XC} = \frac{CY}{YB} = \frac{XZ}{ZY}$
    , then how to prove that the area of  triangle $ABC$ is given by $[ABC]=([AXZ]  ^{1/3}  +
    [BYZ]^{1/3})^3.$
  - 'I''m trying to get my head wrapped around transformer operation and in the process
    regretting the times I snoozed in my Electromagnetics class as a EE student back
    when I was a lad :)  I''m looking for an intuitive understanding, but not just
    an analogous one. I''d like it to be grounded in the actual physics of what''s
    happening. I''ve found several excellent sources on the web, but they all seem
    to skirt this question.  I''ve come across a few interesting hints and am now
    tantalizingly close, I think, but still yearning :)  Fact 1: Although varying
    sinusoidally, the "peak-to-peak" flux, so to speak, in a transformer''s core is
    essentially constant (for a given voltage applied to the primary), regardless
    of the load.  My intuitive hypothesis was that variation in the "strength" of
    the flux was what transferred the energy from the primary to the secondary, but
    this fact would seem to contradict that theory. I had thought that the primary
    makes a bunch of flux based on the current flowing through it and the secondary
    sucks it up to make current of its own. No dice, it seems.  Then of course there''s
    the fact that the formula for flux involves only voltage, time (frequency), and
    turns :)  Fact 2: The current in the primary is (approximately) 90 degrees out
    of phase with the voltage at no load, and approximately aligned in phase at full
    load.  This fact seems very promising and also curiously satisfying. It would
    imply that the Volt-Amps (VA) of the primary is constant and only the power factor
    changes as the current load on the secondary increases.  But I still don''t get
    how the energy is actually being transferred. It seems vaguely like the flux is
    just there as an energy conductor or something and some other phenomenon is actually
    doing the energy transfer bit.  Can someone see what I''m missing and explain
    what''s actually happening in there?'
  - 'I would like to use beamer''s fonts in a standard LaTeX article.  Something like:  \documentclass{article}  \begin{document}
    bla $bla$ \end{document}   But with everything with beamer''s fonts inside?  I
    have found how to change the math fonts only (using  package) but I would like
    to change also the text fonts.'
- source_sentence: 'When I try to install anything, it fails with error message:   installArchives()
    failed: perl: warning: Setting locale failed. perl: warning: Please check that
    your locale settings:     LANGUAGE = (unset),     LC_ALL = (unset),     LANG =
    "en_IN.ISO8859-1"     are supported and installed on your system. perl: warning:
    Falling back to the standard locale ("C"). locale: Cannot set LC_CTYPE to default
    locale: No such file or directory locale: Cannot set LC_MESSAGES to default locale:
    No such file or directory locale: Cannot set LC_ALL to default locale: No such
    file or directory Preconfiguring packages ... perl: warning: Setting locale failed.
    perl: warning: Please check that your locale settings:     LANGUAGE = (unset),     LC_ALL
    = (unset),     LANG = "en_IN.ISO8859-1"     are supported and installed on your
    system. perl: warning: Falling back to the standard locale ("C"). locale: Cannot
    set LC_CTYPE to default locale: No such file or directory locale: Cannot set LC_MESSAGES
    to default locale: No such file or directory locale: Cannot set LC_ALL to default
    locale: No such file or directory Preconfiguring packages ... Selecting previously
    unselected package ladspa-sdk. (Reading database ...  (Reading database ... 5%
    (Reading database ... 10% (Reading database ... 15% (Reading database ... 20%
    (Reading database ... 25% (Reading database ... 30% (Reading database ... 35%
    (Reading database ... 40% (Reading database ... 45% (Reading database ... 50%
    (Reading database ... 55% (Reading database ... 60% (Reading database ... 65%
    (Reading database ... 70% (Reading database ... 75% (Reading database ... 80%
    (Reading database ... 85% (Reading database ... 90% dpkg: unrecoverable fatal
    error, aborting:  reading files list for package ''texlive-base'': Input/output
    error   This is not a duplicate question:  Below is the message that appears at
    the end and if I install anything, below error appears:    dpkg: unrecoverable
    fatal error, aborting:  reading files list for package ''texlive-base'': Input/output
    error   Disk or partition is not full.'
  sentences:
  - I am trying to navigate the command on the alert box, but I am not able to do
    it in Web Driver with JAVA. Please help me with it. Apart from this I would also
    like to know how to tackle with the confirmation box and Warnings prompts displayed.
  - Yesterday I started the upgrade from 12.10 to 13.04, but I interrupted it because
    it was taking too long. Now if I restart it, it doesn't proceed.  Is there any
    possibility to clean the mess it left when I interrupted it and make a clean restart
    of this update?
  - 'I am getting this message every time I do something like starting or stopping
    a service.  perl: warning: Setting locale failed.    perl: warning: Please check
    that your locale settings:            LANGUAGE = "en_US:en",            LC_ALL
    = (unset),            LC_MESSAGES = "en_US.UTF-8",            LANG = "en_US.UTF-8"        are
    supported and installed on your system.    perl: warning: Falling back to the
    standard locale ("C").    locale: Cannot set LC_CTYPE to default locale: No such
    file or directory    locale: Cannot set LC_MESSAGES to default locale: No such
    file or directory    locale: Cannot set LC_ALL to default locale: No such file
    or directory    (Reading database ... 21173 files and directories currently installed.)   Removing
    bind9 ...    * Stopping domain name service... bind9                                        [
    OK ] Processing triggers for man-db ...    locale: Cannot set LC_CTYPE to default
    locale: No such file or directory    locale: Cannot set LC_MESSAGES to default
    locale: No such file or directory    locale: Cannot set LC_ALL to default locale:
    No such file or directory      How do I fix this error ?'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-mpnet-base-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: Unknown
      type: unknown
    metrics:
    - type: pearson_cosine
      value: 0.9499442714034495
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8633690403518242
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-mpnet-base-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision e8c3b32edf5434bc2275fc9bab85f82640a19130 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'MPNetModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'When I try to install anything, it fails with error message:   installArchives() failed: perl: warning: Setting locale failed. perl: warning: Please check that your locale settings:     LANGUAGE = (unset),     LC_ALL = (unset),     LANG = "en_IN.ISO8859-1"     are supported and installed on your system. perl: warning: Falling back to the standard locale ("C"). locale: Cannot set LC_CTYPE to default locale: No such file or directory locale: Cannot set LC_MESSAGES to default locale: No such file or directory locale: Cannot set LC_ALL to default locale: No such file or directory Preconfiguring packages ... perl: warning: Setting locale failed. perl: warning: Please check that your locale settings:     LANGUAGE = (unset),     LC_ALL = (unset),     LANG = "en_IN.ISO8859-1"     are supported and installed on your system. perl: warning: Falling back to the standard locale ("C"). locale: Cannot set LC_CTYPE to default locale: No such file or directory locale: Cannot set LC_MESSAGES to default locale: No such file or directory locale: Cannot set LC_ALL to default locale: No such file or directory Preconfiguring packages ... Selecting previously unselected package ladspa-sdk. (Reading database ...  (Reading database ... 5% (Reading database ... 10% (Reading database ... 15% (Reading database ... 20% (Reading database ... 25% (Reading database ... 30% (Reading database ... 35% (Reading database ... 40% (Reading database ... 45% (Reading database ... 50% (Reading database ... 55% (Reading database ... 60% (Reading database ... 65% (Reading database ... 70% (Reading database ... 75% (Reading database ... 80% (Reading database ... 85% (Reading database ... 90% dpkg: unrecoverable fatal error, aborting:  reading files list for package \'texlive-base\': Input/output error   This is not a duplicate question:  Below is the message that appears at the end and if I install anything, below error appears:    dpkg: unrecoverable fatal error, aborting:  reading files list for package \'texlive-base\': Input/output error   Disk or partition is not full.',
    'I am getting this message every time I do something like starting or stopping a service.  perl: warning: Setting locale failed.    perl: warning: Please check that your locale settings:            LANGUAGE = "en_US:en",            LC_ALL = (unset),            LC_MESSAGES = "en_US.UTF-8",            LANG = "en_US.UTF-8"        are supported and installed on your system.    perl: warning: Falling back to the standard locale ("C").    locale: Cannot set LC_CTYPE to default locale: No such file or directory    locale: Cannot set LC_MESSAGES to default locale: No such file or directory    locale: Cannot set LC_ALL to default locale: No such file or directory    (Reading database ... 21173 files and directories currently installed.)   Removing bind9 ...    * Stopping domain name service... bind9                                        [ OK ] Processing triggers for man-db ...    locale: Cannot set LC_CTYPE to default locale: No such file or directory    locale: Cannot set LC_MESSAGES to default locale: No such file or directory    locale: Cannot set LC_ALL to default locale: No such file or directory      How do I fix this error ?',
    "Yesterday I started the upgrade from 12.10 to 13.04, but I interrupted it because it was taking too long. Now if I restart it, it doesn't proceed.  Is there any possibility to clean the mess it left when I interrupted it and make a clean restart of this update?",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8515, 0.4578],
#         [0.8515, 1.0000, 0.3949],
#         [0.4578, 0.3949, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.9499     |
| **spearman_cosine** | **0.8634** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 402,588 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                           | sentence_1                                                                           | label                                                         |
  |:--------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                               | string                                                                               | float                                                         |
  | details | <ul><li>min: 11 tokens</li><li>mean: 141.66 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 10 tokens</li><li>mean: 128.03 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.5</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | label            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Can you please tell me what "working out of" means in this context?  "African composers working out of European-based choral and instrumental art music traditions are gaining recognition, as are the varied roles that women play in making music."   Google Books: 'The Harvard Dictionary of Music' By Don Michael Randel</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | <code>I have seen people use both forms below. Which is correct? If both are, in which situation is each better used?  I am a software engineer based in New York. I am a software engineer based out of New York.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | <code>1.0</code> |
  | <code>At the beginning the villain is lured to a meeting where an attempt is made on his life. Another character fired a projectile out of a cane which wounded him but he was able to magic up a shield or something to avoid death. There's also a bit later on where our protagonist (young male) has sex with a woman. There are elements of BDSM. She ties him up if I recall correctly. I think him and his companions are guests at her home.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <code>I found an explanation for my question here , which suggests that water washes out sebum (special oil, which covers our skin) and water gets into outer layer of now unprotected skin by osmosis. This article also suggests that fingers are not really shriveled - they are water-logged. But is this right? I think I observed many times my wrinkly fingers after swimming, but I never felt that they are water-logged. Any thought on this matter would be highly appreciated.</code>                                                                                                                                                                                                                                                                                                                                                         | <code>0.0</code> |
  | <code>I have written a trigger on custom object Order_Item__c. This object has a custom field Shipping_Number__c. When the user enters value in Shipping_Number__c and clicks save, the contact lookup field will automatically populate with contact record which has same shipping number as the value entered by the user.  All the contact records have the shipping customer number. Now custom object order item has a field called shipping customer number. When user enters the value in it, the trigger checks the contact record which has same number and populate the contact lookup field on order item object. The trigger is running as it is supposed to run. I am unable to achieve code coverage.  trigger updatelookupfield on Order_Item__c (before update, before insert)  {  Set&lt;String&gt; shippingNumbers = new Set&lt;String&gt;();  for (Order_Item__c collectNumFromOrder : Trigger.new) {     shippingNumbers.add(collectNumFromOrder.Shipping_Customer_Number__c); }    List&lt;Contact&gt; contactList = [SE...</code> | <code>I'd like to start by pointing out that this question may seem like a duplicate, but it isn't. All the questions I saw here on Ask Ubuntu were regarding pip for Python 3 and I'm talking about Python 3.6. The steps used back then don't work for Python 3.6.   I got a clear Ubuntu 16.10 image from the . Run apt-get update Run apt-get install python3.6 Run apt-get install python3-pip Run pip3 install requests bs4 Run python3.6 script.py   Got ModuleNotFoundError below:   Traceback (most recent call last):     File "script.py", line 6, in &lt;module&gt;      import requests  ModuleNotFoundError: No module named 'requests'   Python's and pip's I have in the machine:  python3 python3.5 python3.5m python3.6 python3m python3-config python3.5-config python3.5m-config python3.6m python3m-config    pip pip3 pip3.5</code> | <code>0.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 1
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|
| 0.0199 | 500  | 0.0746        | 0.8634          |


### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.1.2
- Transformers: 4.57.2
- PyTorch: 2.9.0+cu126
- Accelerate: 1.12.0
- Datasets: 4.0.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->