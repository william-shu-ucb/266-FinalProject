---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:402276
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: How do you attach a debugger to a Web service? I am using a Web
    service. Can anybody tell me how to debug through it?
  sentences:
  - 'Which Schengen countries have bilateral agreements which ignore the standard
    90/180 rule? The Schengen rules have certain exemptions for citizens of countries
    which concluded bilateral visa-free agreements before the Schengen area took effect.
    For example, a relevant quote from the :     In practice, it means that, for instance,
    a citizen of the Korean Republic can travel in the Schengen area (including the
    CR) for a period of 90 days in any 180-day period. If the citizen of the Korean
    Republic stayed in the Schengen area for the entire period, he/she can move to
    the CR before the 3 months are up and then stay for a further 90 days in the CR
    without a visa. During these 90 days in the CR, he/she can no longer travel to
    other Schengen states without a visa. In the event of departing and returning
    to the CR during this period, it is necessary to take a direct flight.   The provision
    above applies to citizens of:     Argentina, Chile, Croatia, Israel, Korea, Costa
    Rica, Malaysia, Uruguay   What other countries have similar provisions and to
    citizens of which countries do they apply? And does the Schengen clock "count
    back" while the tourist is using his rights as part of a bilateral agreement?  Note
    that since the rule still precludes staying for more than 90 days in any single
    country, this is on topic for Travel.SE.'
  - I have a question regarding the proper usage of the word "nor" Is "...not legal
    advice, nor is it intended to be" the proper usage of "nor" in the prior partial
    statement?
  - 'Remove Fujitsu Lifebook Bios Password on Startup I Tried to remove the Boot up
    Bios password in a Fujitsu Lifebook Bios SH530 Model. But it still asking for
    password on bootup and now may password did not work. Can anybody help me? Here''s
    what I did:   Press F12 on Bootup  Sign in using the old password Go to Security
    Settings Tab Change the Boot up Password by Typing in the Current Password and
    leaving the New Password Inputbox Blank. I just press enter 2x. exit the bios
    screen and save settings &lt;-- The Worst next time I Boot up it still ask for
    password but my old password did not work. I tried just leaving it blank and press
    enter but it is Invalid! I tried 3x and wooops a non stop long beepp sounded with
    SYSTEM DISABLED on screen no Hash code or what so ever.   What did I do Wrong?
    Do anyone have this experience? What did you do to solve this problem?   PS. I
    do not know the supervisor password for it.  UPDATE:   It seems the Master Password
    will only show up on boot before loading windows 7. If will not show up on Bios
    Settings. I''m currently using this page to decrypt the hash code  My question
    now is how do you display the Master Password Hash in Bios Setup? If I can get
    it I can decrypt it and hopefully remove the password.'
- source_sentence: 'Listing database Nullpointer exeption This is my database helper
    class. I am calling createWord methot to create databese. It is working. But when
    I calling listEnWords method to display on recyclerview I am taking nullpointerexeption.
    I think my context is wrong. How should I change my context?     java.lang.NullPointerException:
    Attempt to invoke virtual method ''android.database.sqlite.SQLiteDatabase android.content.Context.openOrCreateDatabase(java.lang.String,
    int, android.database.sqlite.SQLiteDatabase$CursorFactory, android.database.DatabaseErrorHandler)''
    on a null object reference   public class WordsDbHelper extends SQLiteOpenHelper
    {  private static final int DATABASE_VERSION = 3; private static final String
    DATABASE_NAME = "words.db"; private Context context;  public WordsDbHelper(Context
    context) {     super(context, DATABASE_NAME, null, DATABASE_VERSION);     this.context=context;
    }   @Override public void onCreate(SQLiteDatabase db) {     final String SQL_CREATE_BOOKS_TABLE
    =              "CREATE TABLE " + WordEntry.table_WORDS + " (" +                      WordEntry.word_iD
    + " INTEGER PRIMARY KEY AUTOINCREMENT, " +                      WordEntry.word_ENG
    + " TEXT NOT NULL, " +                      WordEntry.word_TR + " TEXT NOT NULL
    )";      db.execSQL(SQL_CREATE_BOOKS_TABLE);  }  @Override public void onUpgrade(SQLiteDatabase
    db, int oldVersion, int newVersion) {     db.execSQL("DROP TABLE IF EXISTS " +
    WordEntry.table_WORDS);     onCreate(db); }  public void createWord(Words book)
    {     String table_WORDS = "words";     String word_ENG = "engWord";     String
    word_TR = "trWord";      // get reference of the BookDB database     SQLiteDatabase
    db = this.getWritableDatabase();      // make values to be inserted     ContentValues
    values = new ContentValues();     values.put(word_ENG, book.getEngWord());     values.put(word_TR,
    book.getTrWord());      // insert book     db.insertWithOnConflict(table_WORDS,
    null, values, SQLiteDatabase.CONFLICT_IGNORE);      // close database transaction     db.close();
    }  public List&lt;String&gt; listEnWords() {     List&lt;String&gt; dataEng =
    new ArrayList&lt;&gt;();      SQLiteDatabase db = this.getWritableDatabase();
    //Error is here     String[] columns = {WordEntry.word_iD, WordEntry.word_ENG,
    WordEntry.word_TR};      Cursor cursor = db.query(WordEntry.table_WORDS, columns,
    null,             null,             null,             null,             null);      while
    (cursor.moveToNext()) {         dataEng.add(cursor.getString(0) + "-" + cursor.getString(1));      }     return
    dataEng; }  public List&lt;String&gt; listTrWords() {     List&lt;String&gt; dataTr
    = new ArrayList&lt;&gt;();      SQLiteDatabase db = this.getWritableDatabase();     String[]
    columns = {WordEntry.word_iD, WordEntry.word_ENG, WordEntry.word_TR};      Cursor
    cursor = db.query(WordEntry.table_WORDS, columns,             null,             null,             null,             null,             null);      while
    (cursor.moveToNext()) {         dataTr.add(cursor.getString(2));      }     return
    dataTr; }   I am calling list methods from adapter of recyclerviev like this.  @Override
    public void onBindViewHolder(RecyclerView.ViewHolder viewHolder, int position)
    {     WordListRecyclerItemViewHolder holder = (WordListRecyclerItemViewHolder)
    viewHolder;      WordsDbHelper helper = new WordsDbHelper(null);      List&lt;String&gt;
    enWordData = helper.listEnWords();     List&lt;String&gt; trWordData = helper.listTrWords();      String
    itemEnText = enWordData.get(position);     String itemTrText = trWordData.get(position);      holder.setNewsTitle(itemEnText
    + ". word");     holder.setNewsDesc(itemTrText + ". kelime"); }'
  sentences:
  - 'Ubuntu 12.04 boots to TTY1 Alrighty, I have perused the threads already in existence
    and am finding none of them seem to have the exact combination of variables I''ve
    got going.  I''m working on a computer using Ubuntu 12.04. Currently, it boots
    straight into tty1  Ubuntu 12.04.4 LTS [computer name] tty1  [computer name] login:
    Password:   Login leads to:  Last login: Wed Mar 19 13:47:11MDT 2014 on tty1  Welcome
    to Ubuntu 12.04.4 LTS (GNU/Linux 3.2.0-32generic-pae i686   The owner of the computer
    stated that this issue happened after a recent update, if that gives anyone a
    hint as to the specific location of the graphics failure.   I''m capable of booting
    into the GUI utilizing startx, but am frankly at a loss of where to go from here.
    Years of Windows has molded me into a GUI heavy kinda person, so, if possible,
    work off the assumption that I''ve no idea what you''re talking about and break
    it down to the simplest of steps.  Thanks!'
  - What is a NullPointerException, and how do I fix it? What are Null Pointer Exceptions
    (java.lang.NullPointerException) and what causes them?  What methods/tools can
    be used to determine the cause so that you stop the exception from causing the
    program to terminate prematurely?
  - Rename SQL Server Schema How can I rename a schema using SQL Server?
- source_sentence: Unable to paste unicode character into MySQL console I am working
    on a server Ubuntu 16.04 in which is installed MySQL 5.7.31. I have a trouble
    about paste a unicode character like ù or à in the console of MySQL. What kind
    of check I can do to solve this issue? Many thanks.
  sentences:
  - UTF-8 all the way through I'm setting up a new server and want to support UTF-8
    fully in my web application. I have tried this in the past on existing servers
    and always seem to end up having to fall back to ISO-8859-1.  Where exactly do
    I need to set the encoding/charsets? I'm aware that I need to configure Apache,
    MySQL, and PHP to do this — is there some standard checklist I can follow, or
    perhaps troubleshoot where the mismatches occur?  This is for a new Linux server,
    running MySQL 5, PHP, 5 and Apache 2.
  - QGIS 2.12 symbology does not work correctly I use QGIS for a long times on mac
    and windows and I have a problem with the 2.12 version on my OSX 10.8.5 when I
    want to edit style of my vector layer.    When I click on properties of a vector
    layer and I want to edit the style, QGIS tells me that This layer doesn't have
    any editable properties. I attach a file to be as clear as possible. Is anyone
    having the same problem ? Do you find a solution?  I had the same problem with
    the 2.10 version.
  - Is JavaScript a pass-by-reference or pass-by-value language? The primitive types
    (number, string, etc.) are passed by value, but objects are unknown, because they
    can be both passed-by-value (in case we consider that a variable holding an object
    is in fact a reference to the object) and passed-by-reference (when we consider
    that the variable to the object holds the object itself).  Although it doesn't
    really matter at the end, I want to know what is the correct way to present the
    arguments passing conventions. Is there an excerpt from JavaScript specification,
    which defines what should be the semantics regarding this?
- source_sentence: 'Markdown inconsistency between preview and post when using blank
    lines This happened in  on , where we have all sorts of uncommon programming languages
    to put in a code block. OP''s code is copied here at the markdown level:   bbcccbc-cc-b--b--
    c b   &#32; c  - L`.{6} . $0X&#32; Y`X`\LAPACK .L L  The above uses raw &lt;pre&gt;&lt;code&gt;
    to preserve the blank-only line (by ending with &amp;#32;) between the line with
    single b and the one with single c (check it by dragging on it). But it is wrong
    because the code should start with a single empty line, not two; removing a line
    there will break the entire code block. On the other hand, using the fenced or
    indented block does not have any way to preserve the blank-only line (it is stripped
    now, but it should be preserved in order to be a valid code) works as expected
    with the blank-only lines, but is not shown as such in the preview section. Using
    fenced block:  bbcccbc-cc-b--b-- c b     c  - L`.{6} . $0X  Y`X`\LAPACK .L L  Using
    indented block: bbcccbc-cc-b--b-- c b     c  - L`.{6} . $0X  Y`X`\LAPACK .L L  Edit:
    I just found that the three blanks are preserved on the main post. I saw the bug
    described above in the preview section, and wrongly assumed that it will be the
    same when actually posted. It is very likely a bug in the preview renderer.'
  sentences:
  - 'using mixed effect logistic regression properly I am new to data analysis and
    now working on a Mixed Effects Logistic Regression Model.Currently I have a data
    frame (model_data) that looks like the following:  Vehicle_id    entry_time         exit_time          last_veh_time  vehicle_type  __________     ___________       __________        ____________    ____________     1        2017-01-31
    00:00:00  2017-01-31 00:00:00    300         4 wheel    status _______   0    Likewise,
    I have information(nearly a million rows) on all vehicles entering a place and
    exiting the same place. status can be either 1 or 0 for all of these. last_veh_time
    is the last vehicle passed the same place before how much time. I want to know
    the probability of a getting status 0 for a vehicle based on entry_time and last_veh_time.
    So here my response is status and which will be my dependent variable?Is it entry_time
    and  last_veh_time?Any help is appreciated'
  - 'Force GraphicsMagick to resize image to specific width I''m batch processing
    a folder of image to a uniform width with GraphicsMagick (though I assume the
    same would apply to ImageMagick):  $ gm convert -resize 1000x in.jpg out.jpg   But
    when I inspect some of the images, I get 999px instead of 1000px.  $ gm identify
    -verbose out.jpg  ==&gt; Image: out.jpg ==&gt; Format: JPEG (Joint Photographic
    Experts Group JFIF format ==&gt;   Geometry: 999x591   Is there a way to enforce
    the right width? I assume it''s doing some estimation to preserve aspect ratios.'
  - Captured variable in a loop in C# I met an interesting issue about C#. I have
    code like below.  List&lt;Func&lt;int&gt;&gt; actions = new List&lt;Func&lt;int&gt;&gt;();  int
    variable = 0; while (variable &lt; 5) {     actions.Add(() =&gt; variable * 2);     ++
    variable; }  foreach (var act in actions) {     Console.WriteLine(act.Invoke());
    }   I expect it to output 0, 2, 4, 6, 8. However, it actually outputs five 10s.  It
    seems that it is due to all actions referring to one captured variable. As a result,
    when they get invoked, they all have same output.  Is there a way to work round
    this limit to have each action instance have its own captured variable?
- source_sentence: 'What is most efficient way to find the sum of the series: (N/2^2)*2^2+(N/3^2)*3^2+(N/4^2)*4^2+........
    I have been given a series: $$\lfloor(N/2^2)\rfloor*2^2+\lfloor(N/3^2)\rfloor*3^2+\lfloor(N/4^2)\rfloor*4^2+....+\lfloor(N/\lfloor\sqrt(N)\rfloor^2)\rfloor*\lfloor\sqrt(N)\rfloor^2$$  Where
    N is a natural number. I know it can be solved in $O({\sqrt N})$ time complexity,
    but can there be any other way to solve this.'
  sentences:
  - 'Sections running off page I have a long list of sections and subsections like
    so  \chapter{Thin Lenses} \section*{Aim} \section*{A. Types of Lenses} \subsection*{Prediction}
    \subsection*{Observation} \subsection*{Explanation} \section*{B. Image Formation}
    \subsection*{B1. The lens and the image and the object position} \subsection*{B2.
    Partial lens} \subsection*{B3. Eyeballing the image} \section*{C. Focal Length
    of a Converging Lens} \subsubsection*{Question 1} \subsection*{C1. Estimating
    the focal length: Eyeballing the image} \subsubsection*{Prediction} \subsubsection*{Observation}
    \subsubsection*{Explanation} \subsubsection*{Focal length estimation 1} \subsection*{C2.
    Estimating the focal length: Parallel rays} \subsubsection*{Prediction} \subsubsection*{Observation}
    \subsubsection*{Explanation} \subsubsection*{Focal length estimation 2} \subsubsection*{Question
    2}   etc. which just run off the bottom of the first page and disappear. Why is
    this? It doesn''t happen if I include some text in the sections.'
  - Unexpected goods delivery - is this a scam, and what kind of scam? My wife received
    a small package, containing a pair of Ray Ban sunglasses (whether original or
    fake I don't know) in a nice leather-looking case. It is addressed to her, correct
    name, street, postcode, and her mobile phone number printed on it. Declared with
    a value of $15 printed on it, and coming from a company in China. Everything fine,
    except she never ordered any sunglasses, and she never paid for any sunglasses.
    I know there are scams where scammers send rubbish items to random people, and
    that entitles them to post fake reviews on Amazon, for example. The only thing
    is, this isn't a rubbish item. Even if these sunglasses are fake, they would be
    worth some money. Does anyone have an idea how either (a) a company in China could
    send goods to a random real person by mistake, or (b) what kind of scam would
    make it worth while to send an item that would probably cost £10 to £20 on Amazon?
  - 'Why is the voltage across the inputs of an ideal OP Amp zero? The property that
    the voltage across the inputs of an ideal OP Amp is zero cannot be taken as an
    axiom because it isn''t a property you can directly &quot;adjust&quot; (as opposed
    to say the resistance across the input terminals or the gain). It''s a consequence
    of the properties that you can &quot;adjust&quot;, hence it must be derived from
    these properties. All proofs I''ve come across essentially prove it like this:  Let
    the voltage across the input terminals of an ideal OP Amp be \$V_{in}\$, the output
    voltage be \$V_o\$ and the gain be \$G\$. \$V_o\$ is given by: \$V_o = GV_{in}\$
    The voltage across the OP Amp is bounded by the voltage being supplied to it.
    Let the supplied voltage be \$V_s\$. Then \$-V_s \le GV_{in} \le +V_s \$ The gain
    is a property than can ideally be fixed to any value, so taking the limit of \$G\$
    going to infinity gives: \$ \lim_{G \to \infty} \frac{-V_s}{G} \le V_{in} \le
    \frac{+V_s}{G} \$ \$\implies 0 \le V_{in} \le 0\$ Hence the voltage across the
    input terminals of an ideal OP Amp must be zero.  The proof above would only be
    valid if OP Amps were always linear, which isn''t true. If the output is greater
    in magnitude than the supplied voltage, the OP Amp becomes saturated - the proof
    doesn''t take this into account. In other words, the proof assumes that \$V_o
    = GV_{in}\$ which is false. The correct equation would be: \$V_o = \begin{cases}
    GV_{in}, \space -V_{s} \le GV_{in} \le +V_{s} \\ +Vs, \space GV_{in} &gt; V_s
    \\ -Vs, \space GV_{in} &lt; -V_s \end{cases}\$'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: Unknown
      type: unknown
    metrics:
    - type: pearson_cosine
      value: 0.9445932631174006
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8640266636517354
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
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
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
    'What is most efficient way to find the sum of the series: (N/2^2)*2^2+(N/3^2)*3^2+(N/4^2)*4^2+........ I have been given a series: $$\\lfloor(N/2^2)\\rfloor*2^2+\\lfloor(N/3^2)\\rfloor*3^2+\\lfloor(N/4^2)\\rfloor*4^2+....+\\lfloor(N/\\lfloor\\sqrt(N)\\rfloor^2)\\rfloor*\\lfloor\\sqrt(N)\\rfloor^2$$  Where N is a natural number. I know it can be solved in $O({\\sqrt N})$ time complexity, but can there be any other way to solve this.',
    "Why is the voltage across the inputs of an ideal OP Amp zero? The property that the voltage across the inputs of an ideal OP Amp is zero cannot be taken as an axiom because it isn't a property you can directly &quot;adjust&quot; (as opposed to say the resistance across the input terminals or the gain). It's a consequence of the properties that you can &quot;adjust&quot;, hence it must be derived from these properties. All proofs I've come across essentially prove it like this:  Let the voltage across the input terminals of an ideal OP Amp be \\$V_{in}\\$, the output voltage be \\$V_o\\$ and the gain be \\$G\\$. \\$V_o\\$ is given by: \\$V_o = GV_{in}\\$ The voltage across the OP Amp is bounded by the voltage being supplied to it. Let the supplied voltage be \\$V_s\\$. Then \\$-V_s \\le GV_{in} \\le +V_s \\$ The gain is a property than can ideally be fixed to any value, so taking the limit of \\$G\\$ going to infinity gives: \\$ \\lim_{G \\to \\infty} \\frac{-V_s}{G} \\le V_{in} \\le \\frac{+V_s}{G} \\$ \\$\\implies 0 \\le V_{in} \\le 0\\$ Hence the voltage across the input terminals of an ideal OP Amp must be zero.  The proof above would only be valid if OP Amps were always linear, which isn't true. If the output is greater in magnitude than the supplied voltage, the OP Amp becomes saturated - the proof doesn't take this into account. In other words, the proof assumes that \\$V_o = GV_{in}\\$ which is false. The correct equation would be: \\$V_o = \\begin{cases} GV_{in}, \\space -V_{s} \\le GV_{in} \\le +V_{s} \\\\ +Vs, \\space GV_{in} &gt; V_s \\\\ -Vs, \\space GV_{in} &lt; -V_s \\end{cases}\\$",
    "Unexpected goods delivery - is this a scam, and what kind of scam? My wife received a small package, containing a pair of Ray Ban sunglasses (whether original or fake I don't know) in a nice leather-looking case. It is addressed to her, correct name, street, postcode, and her mobile phone number printed on it. Declared with a value of $15 printed on it, and coming from a company in China. Everything fine, except she never ordered any sunglasses, and she never paid for any sunglasses. I know there are scams where scammers send rubbish items to random people, and that entitles them to post fake reviews on Amazon, for example. The only thing is, this isn't a rubbish item. Even if these sunglasses are fake, they would be worth some money. Does anyone have an idea how either (a) a company in China could send goods to a random real person by mistake, or (b) what kind of scam would make it worth while to send an item that would probably cost £10 to £20 on Amazon?",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.0459,  0.0139],
#         [ 0.0459,  1.0000, -0.0798],
#         [ 0.0139, -0.0798,  1.0000]])
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

| Metric              | Value     |
|:--------------------|:----------|
| pearson_cosine      | 0.9446    |
| **spearman_cosine** | **0.864** |

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

* Size: 402,276 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                           | sentence_1                                                                           | label                                                         |
  |:--------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                               | string                                                                               | float                                                         |
  | details | <ul><li>min: 17 tokens</li><li>mean: 148.31 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 17 tokens</li><li>mean: 145.53 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.5</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                    | label            |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Bijection between $[a,b)$ and $(a,b)$? I know this question has been asked and answered before, but I am working on my own through an analysis textbook and just wanted to check if the following construction would be appropriate:  Define $a\|b=(a+b)/2$ to be the midpoint of interval $(a,b)$ and $a\|b^n=(...(a\underbrace{\|b)\|b)...\|b)}_{n\text{ times}}$ (note that $a\|b^0=a$). Then define the bijection $f:[a,b)\rightarrow(a,b)$ as follows:$$f(x)=\begin{cases}a\|b^{i+1},   &amp; \text{if $x=a\|b^i$, for $i=0,1,...$} \\x,   &amp; \text{otherwise} \end{cases}$$  So $a$ gets sent to the midpoint of $(a,b)$, which in turn gets sent to the midpoint of itself and $b$, and so on ad infinitum, while the rest of the elements stay fixed. I know this doesn't seem like something worthy of posting a question for, but I am working on my own and struggling with a lot of the exercises, so I am anxious for at least some of my solutions to be correct.</code> | <code>Explicit bijection between $[0,1)$ and $(0,1)$ Proving that $[0,1)$ and $(0,1)$ have the same cardinality (without assuming any previous knowledge) can be done easily using Cantor-Bernstein theorem.  However I'm wondering if someone can build an explicit bijection between these sets.  It's easy to build a bijection between $(0,1)$ and $\mathbb R$, so a bijection from $[0,1)$ to $\mathbb R$ will also fit the bill.</code> | <code>1.0</code> |
  | <code>"Half of its" or "Half its" I couldn't seem to find anyone asking a question like this anywhere, so I figured I'd start here. The sentence in question is      "A dolphin sleeps with half its brain awake so it can remain aware of   its underwater environment."   My question is would it be more grammatically correct to say "half of its" or is "half its" just as valid a way to write this sentence as "half of its"? Whatever the answer, is there anyone that may have a rule or some form of logical explanation as to why that answer is correct?   I appreciate any help that can be offered.</code>                                                                                                                                                                                                                                                                                                                                                                        | <code>Can I receive the newsletter under a different email address? I want to subscribe to the newsletter on my work email address but still have everything else go to my normal SO email account. I don't have a way to set up a forwarding filter from my normal email account.  Any way I can do this?</code>                                                                                                                             | <code>0.0</code> |
  | <code>Good book on non-Euclidean geometry What's a good book on non-Euclidean geometry for undergrads?  Especially ones that consider hyperbolic and spherical trigonometry?</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <code>Term for someone asking "For a friend" Is there a word that describes the phenomenon, often seen on SE sites, where someone says they are asking a question "for a friend", but actually mean themselves?</code>                                                                                                                                                                                                                        | <code>0.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 12
- `per_device_eval_batch_size`: 12
- `num_train_epochs`: 1
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 12
- `per_device_eval_batch_size`: 12
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
| 0.0149 | 500  | 0.0827        | 0.8640          |


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