import os
import re
from html import escape

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
w2_path = os.path.join(dir_path, "week2.html")
w12_path = os.path.join(dir_path, "week12.html")
w13_path = os.path.join(dir_path, "week13.html")
w14_path = os.path.join(dir_path, "week14.html")
w15_path = os.path.join(dir_path, "week15.html")
w16_path = os.path.join(dir_path, "week16.html")
w17_path = os.path.join(dir_path, "week17.html")
w18_path = os.path.join(dir_path, "week18.html")
roadmap_path = os.path.join(dir_path, "roadmap.html")

print("Executing Content Quality and Pedagogical updates for Weeks 12-18...")

# ─── BUG-02: Checklist duplication fix (Weeks 16 & 17) ─────────────────────────
for path in [w16_path, w17_path]:
    if os.path.exists(path):
        content = open(path, 'r', encoding='utf-8').read()
        pattern = re.compile(r'(<div class="callout" style="background:rgba\(247,169,75,\.05\);border-left:3px solid var\(--orange\);padding:\.8rem 1\.1rem;margin:1rem 0;font-size:13\.5px;">\s*<strong>🚦 Before You Start Checklist:</strong>.*?</div>\s*)\1\1', re.DOTALL)
        content, count = pattern.subn(r'\1', content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Cleaned duplicate checklists in {os.path.basename(path)}: replaced {count} instances.")

# ─── BUG-03: Remove generic 'production deployments' boilerplate ────────────────
for path in [w12_path, w13_path, w14_path, w15_path, w16_path, w17_path, w18_path]:
    if os.path.exists(path):
        content = open(path, 'r', encoding='utf-8').read()
        content, count = re.subn(r'<div class="ml-connect">\s*In production deployments of.*?\s*</div>', '', content, flags=re.DOTALL)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Removed boilerplate connection boxes from {os.path.basename(path)}: {count} removed.")

# ─── ACC-05: torch.fill bug in Day 94 ──────────────────────────────────────────
if os.path.exists(w14_path):
    content = open(w14_path, 'r', encoding='utf-8').read()
    content = content.replace("M = torch.fill(torch.zeros(T, 1), float('-inf'))",
                              "M = torch.full((T, 1), float('-inf'))")
    content = content.replace("Day 98 — PEFT &amp; LoRA", "Day 98 — PEFT &amp; LoRA (Theory)")
    content = content.replace("PEFT &amp; LoRA", "PEFT &amp; LoRA (Theory &amp; Concepts)")
    content = content.replace("Day 99 — Advanced RAG", "Day 99 — RAG Fundamentals: Retrieval Architecture")
    content = content.replace("⏱ 6 hours", "⏱ 6 hours (Note: High-volume day. Take 2 days to fully digest if needed)")
    with open(w14_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched week14.html bugs & scope declarations.")

# ─── ACC-06: Day 87 spaCy misconception ────────────────────────────────────────
if os.path.exists(w13_path):
    content = open(w13_path, 'r', encoding='utf-8').read()
    content = content.replace(
        "spaCy pipelines hamesha baseline parameters ke sath bina tuning ke perfectly kaam karega.",
        "Disabling pipeline components (parser, NER) affects lemmatization output quality."
    )
    content = content.replace(
        "Har dataset ki characteristics alag hoti hain, isliye hyperparameter tuning aur proper features scaling model performance ke liye zaroori hain.",
        "Lemmatization only requires tokenization and morphologization. Disabling parser and NER is best practice for fast preprocessing pipelines."
    )
    content = content.replace(
        "n_process=-1",
        "n_process=1 # (n_process=1 is safe for all systems; n_process=-1 may cause spawn errors on Windows/macOS)"
    )
    with open(w13_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched week13.html spaCy misconception & multiprocessing.")

# ─── ACC-01: Month 5 label removal in Week 16 ───────────────────────────────
if os.path.exists(w16_path):
    content = open(w16_path, 'r', encoding='utf-8').read()
    content = content.replace("MONTH 5 — PRODUCTION AI ENGINEERING", "MONTH 4 — MODERN AI STACK")
    
    old_map_108 = """<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Model Serialization</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Flask REST API</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">WSGI Gunicorn</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Docker Containers</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Docker Compose</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Gradio UI</span>"""

    new_map_108 = """<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">LoRA/QLoRA</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">PEFT library</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Supervised Fine-Tuning</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Dataset Formatting</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Adapter Merging</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Model Quantization</span>"""
    
    content = content.replace(old_map_108, new_map_108)

    lora_visual = """
  <div class="diagram">
    <pre>
      Base Weight W (4096 x 4096)        LoRA Adapters delta_W = B x A
      [  Active but Frozen weights  ]   +   B (4096 x r)  x  A (r x 4096)
      [                             ]       Where rank r is small (e.g., r=8)
      [                             ]       Params reduced from 16.7M to 65K!
    </pre>
    <div class="diagram-cap">Figure: LoRA Low-Rank Adaptation Matrix Decomposition</div>
  </div>"""
    content = content.replace("<h3>2. LoRA — Low-Rank Adaptation</h3>", "<h3>2. LoRA — Low-Rank Adaptation</h3>" + lora_visual)

    eval_links = """
    <div class="res-grid">
      <a class="res-card type-doc-card" href="https://docs.ragas.io" target="_blank">
        <div class="res-icon type-doc">📖</div>
        <div class="res-body">
          <div class="res-type">DOCS · RAGAS</div>
          <div class="res-title">RAGAS Evaluation Framework</div>
          <div class="res-desc">Learn how to measure faithfulness, answer relevance, and context recall.</div>
        </div>
      </a>
      <a class="res-card type-doc-card" href="https://www.trulens.org/docs/getting_started/" target="_blank">
        <div class="res-icon type-doc">📖</div>
        <div class="res-body">
          <div class="res-type">DOCS · TRULENS</div>
          <div class="res-title">TruLens Evaluation</div>
          <div class="res-desc">Details on setting up the RAG Triad for hallucinations detection.</div>
        </div>
      </a>
    </div>"""
    content = content.replace("<h4>Week 16 Resources</h4>", "<h4>Week 16 Resources</h4>" + eval_links)

    with open(w16_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched week16.html labels & visual diagrams.")

# ─── BUG-05: Day 118 Flask concept map correction ─────────────────────────────
if os.path.exists(w17_path):
    content = open(w17_path, 'r', encoding='utf-8').read()
    content = content.replace("MONTH 5 — DEPLOY + FLASK + DOCKER", "MONTH 4 — DEPLOY + FLASK + DOCKER")
    
    old_map_118 = """<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Microservices</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Docker Compose Network</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Prometheus Metrics</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">CI/CD Pipelines</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Cloud Deployment</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Portfolio Polish</span>"""

    new_map_118 = """<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Flask Routes</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">View Functions</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Jinja2 Templates</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Blueprints</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">WSGI &amp; Gunicorn</span>
<span style="color:var(--muted); font-weight:bold;">➔</span>
<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">API Deployments</span>"""

    content = content.replace(old_map_118, new_map_118)
    content = content.replace("Advanced Production Project, Deployment, Final Portfolio Polish?",
                              "Basic Python routing and web service concepts?")
    content = content.replace("+160 XP", "+150 XP")
    content = content.replace("+175 XP", "+150 XP")

    with open(w17_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched week17.html blueprints & checklist prerequisites.")

# ─── ROADMAP-LEVEL: Salary numbers and LangChain pins ─────────────────────────
if os.path.exists(roadmap_path):
    content = open(roadmap_path, 'r', encoding='utf-8').read()
    content = content.replace("8–20 LPA", "10–25 LPA ($70k–120k Remote)")
    content = content.replace("10–25 LPA", "12–30 LPA ($80k–140k Remote)")
    content = content.replace("8–18 LPA", "10–22 LPA ($65k–110k Remote)")
    content = content.replace("12–30 LPA", "15–40 LPA ($90k–160k Remote)")
    content = content.replace("langchain==0.1.20", "langchain>=0.3.0")
    content = content.replace("langchain-community==0.0.38", "langchain-community>=0.3.0")
    content = content.replace("langchain-openai==0.1.6", "langchain-openai>=0.2.0")

    ecosystem_note = """
    <h3 style="margin-top:2rem">💡 Note on the Orchestration Ecosystem</h3>
    <p>While LangChain is the most common industry-standard framework, modern AI architectures often prefer <strong>LlamaIndex</strong> for complex RAG tasks, <strong>LangGraph</strong> for stateful multi-agent pipelines, or directly utilizing <strong>LiteLLM</strong> for provider-agnostic structured inputs.</p>
    """
    content = content.replace("<h3>4 Career Tracks — Choose Your Path</h3>", ecosystem_note + "\n<h3>4 Career Tracks — Choose Your Path</h3>")

    with open(roadmap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched roadmap.html salaries, packages, and ecosystem notes.")

# ─── PED-02: Pandas joins comparison visual on Week 2 ──────────────────────────
if os.path.exists(w2_path):
    content = open(w2_path, 'r', encoding='utf-8').read()
    joins_diagram = """
  <div class="diagram">
    <pre>
      INNER JOIN: Match keys present in BOTH DataFrames.
      LEFT JOIN:  Keep ALL rows from left, match keys from right (NaN if missing).
      RIGHT JOIN: Keep ALL rows from right, match keys from left (NaN if missing).
      OUTER JOIN: Keep ALL rows from BOTH sides, filling missing keys with NaN.
      
      Left DF: [A, B]        Right DF: [B, C]
        Inner: [B]
        Left:  [A, B (matches)]
        Right: [B (matches), C]
        Outer: [A, B, C]
    </pre>
    <div class="diagram-cap">Figure: Visual row-matching logic for merge join types</div>
  </div>"""
    content = content.replace("<h4>Pandas Joins</h4>", "<h4>Pandas Joins</h4>" + joins_diagram)
    with open(w2_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Patched week2.html with Pandas joins diagram.")

# ─── DYNAMIC PREDICTORS & FLASHCARDS REPLACEMENTS FOR WEEKS 12-18 ─────────────
# We will read files and substitute the identical placeholders with actual ones.
# In Weeks 12-18, the placeholder matches np.ones((2, 3)) shape calculations.
# We replace it with day-specific code blocks.

def replace_placeholders(path, day_predictors, day_flashcards):
    if not os.path.exists(path):
        return
    html = open(path, 'r', encoding='utf-8').read()
    
    placeholder_code = """# Predict basic shape of a numpy array
import numpy as np
a = np.ones((2, 3))
print(a.shape)"""

    for day, (code, ans) in day_predictors.items():
        # Match day pill or day container bounds
        # We can do exact string checks:
        target_check = f"checkPredict('day{day}-p1', '(2, 3)')"
        if target_check in html:
            html = html.replace(target_check, f"checkPredict('day{day}-p1', '{ans}')")
            # Replace the code in the immediate <pre> element
            # Since there could be multiple np.ones((2, 3)) across the file, we target it relative to day ID or replace sequentially.
            # But the order of days is sequential. Let's do a replace for the first occurrence of placeholder_code:
            html = html.replace(placeholder_code, code.strip(), 1)
            
    # Also replace generic flashcards
    for day, cards in day_flashcards.items():
        old_fronts = [
            f"What is the main goal of Day {day}?",
            f"How is Day {day} structured?",
            f"Where does Day {day} fit in Week ",
            f"What is the recommended study time?"
        ]
        def replace_flashcard_front(old_front, new_front):
            nonlocal html
            html = html.replace(old_front, new_front, 1)

        def replace_flashcard_back(front_text, back_text):
            nonlocal html
            pattern = re.compile(
                rf'(<div class="fc-front">{re.escape(front_text)}</div>\s*<div class="fc-back">)(.*?)(</div>)',
                re.DOTALL,
            )
            html = pattern.sub(lambda m: f"{m.group(1)}{escape(back_text)}{m.group(3)}", html, count=1)

        # Replace the front/back pair for each day-specific flashcard.
        for idx, (f_txt, b_txt) in enumerate(cards):
            if idx < len(old_fronts):
                replace_flashcard_front(old_fronts[idx], f_txt)
                replace_flashcard_back(f_txt, b_txt)

        # Keep the study-time card generic and unique.
        replace_flashcard_back("How is Day {} structured?".format(day), "It combines theory, hands-on coding tasks, and quizzes.")
        replace_flashcard_back("What is the recommended study time?", "Approximately 4 to 6 hours including exercises.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Replaced Predictors and Flashcards in {os.path.basename(path)}")

# Mappings for Week 12
w12_preds = {
    80: ("# Day 80: Attention Matrix shape\\n# Q of shape (1, 10, 64) and K of shape (1, 12, 64).\\n# What is the shape of attention weights (Q K^T)?", "(1, 10, 12)"),
    81: ("# Day 81: Context vector length\\n# If encoder hidden states size is 256, what is context vector shape?", "(256,)"),
    82: ("# Day 82: Image Captioning vocab index output\\n# Predict vocabulary token mapping index for standard <SOS> token", "1"),
    83: ("# Day 83: Temperature decoding\\n# If Temp = 0.0, the decoding behavior is strictly equivalent to which search?", "Greedy Search"),
    84: ("# Day 84: BERT Masked Language Modeling\\n# If input has 100 tokens, standard pre-training masks what percentage?", "15%"),
    85: ("# Day 85: GPT-2 causal mask shape\\n# For sequence length 5, what is the lower triangular causal mask shape?", "(5, 5)"),
    86: ("# Day 86: Gradio Input type\\n# If fn accepts gr.Image(), what datatype does it pass to the function?", "numpy.ndarray")
}
w12_cards = {
    80: [("What is Attention?", "A mechanism allowing models to focus on specific parts of input sequences dynamically."),
         ("Additive Attention?", "Proposed by Bahdanau. Uses a feedforward network to calculate alignment scores.")],
    81: [("Encoder-Decoder bottleneck?", "Fixed-length context vector fails to summarize long sequences correctly."),
         ("Luong Attention?", "Multiplicative attention using dot-product alignment: score = h_t^T W s_a.")],
    82: [("Show and Tell model?", "CNN extracts visual features, feeds them as initial state to an LSTM language decoder."),
         ("Captioning loss function?", "Sparse Categorical Cross-Entropy over the generated vocabulary sequence.")],
    83: [("Temperature scaling?", "Divides logits by T before softmax. T < 1 sharpens, T > 1 flattens probability.")],
    84: [("BERT training goals?", "Masked Language Modeling (MLM) and Next Sentence Prediction (NSP).")],
    85: [("Causal masking?", "Triangular masking prevents self-attention from looking at future tokens during training.")],
    86: [("Gradio application factory?", "gr.Interface(fn=predict, inputs='text', outputs='label').launch()")]
}
replace_placeholders(w12_path, w12_preds, w12_cards)

# Mappings for Week 13
w13_preds = {
    87: ("# Day 87: spaCy doc length\\n# doc = nlp(\\'AI is fun\\')\\n# print(len(doc))", "3"),
    88: ("# Day 88: Named Entity Recognition\\n# doc = nlp(\\'Flipkart in India\\')\\n# print([ent.label_ for ent in doc.ents])", "['ORG', 'GPE']"),
    89: ("# Day 89: spaCy textcat output format\\n# doc.cats is a dictionary of categories.\\n# What datatype is doc.cats?", "dict"),
    90: ("# Day 90: LDA Topic Word matrix shape\\n# LDA with 5 topics over 1000 vocabulary words. Shape of components_:", "(5, 1000)"),
    91: ("# Day 91: Word similarity\\n# What is cosine similarity of identical word vectors?", "1.0"),
    92: ("# Day 92: Hugging Face pipeline output\\n# print(pipeline(\\'sentiment-analysis\\')(\\'I love AI\\')[0][\\'label\\'])", "POSITIVE"),
    93: ("# Day 93: Capstone classification shape\\n# Classifier output nodes for 3-class classification", "3")
}
w13_cards = {
    87: [("spaCy nlp object?", "The central pipeline containing tokenizer, morphologizer, parser, and NER loaded from models.")],
    88: [("NER?", "Named Entity Recognition. Locating and classifying entities (names, places, organizations) in text.")],
    89: [("Text Categorization?", "Supervised text classification mapping input documents to discrete label categories.")],
    90: [("LDA?", "Latent Dirichlet Allocation. Unsupervised generative model grouping documents into topics.")],
    91: [("GloVe?", "Global Vectors for Word Representation. Unsupervised method training on global co-occurrence matrix.")],
    92: [("Hugging Face Hub?", "Central repository hosting model checkpoints, dataset cards, and spaces demos.")],
    93: [("NLP Capstone goal?", "Build and deploy an end-to-end production classifier using spaCy or HuggingFace transformers.")]
}
replace_placeholders(w13_path, w13_preds, w13_cards)

# Mappings for Week 14
w14_preds = {
    94: ("# Day 94: Scale factor in Self-Attention\\n# If embedding dim d_k is 64, what is the scale factor sqrt(d_k)?", "8"),
    95: ("# Day 95: RoPE properties\\n# Does RoPE use absolute or relative positional encoding mappings?", "relative"),
    96: ("# Day 96: Hugging Face map batch shape\\n# dataset.map(fn, batched=True, batch_size=16) passes input batch shape of", "16"),
    97: ("# Day 97: SFT supervised learning loss\\n# Loss function for predicting target sequence tokens", "Cross-Entropy"),
    98: ("# Day 98: LoRA weight delta shape\\n# B shape (4096, 8) and A shape (8, 4096). What is output dimension?", "(4096, 4096)"),
    99: ("# Day 99: Vector distance metric\\n# Euclidean distance between orthogonal vectors of norm 1.0", "1.414"),
    100: ("# Day 100: Capstone parameter count\\n# If base parameters are 1B and LoRA trains 1M, percentage trained is", "0.1%")
}
w14_cards = {
    94: [("Self-Attention formula?", "Softmax(Q K^T / sqrt(d_k)) V"),
         ("Scale factor role?", "Divides dot product to prevent logits from blowing up and causing vanishing gradients.")],
    95: [("RoPE?", "Rotary Positional Embedding. Multiplies key/query vectors by rotation matrix to encode position."),
         ("Pre-LN vs Post-LN?", "Pre-LN puts LayerNorm inside residual path before attention, enabling stable training.")],
    96: [("Hugging Face Datasets?", "Library optimized for streaming, caching, and tokenizing large text datasets with Arrow backend.")],
    97: [("SFT?", "Supervised Fine-Tuning. Training LLM on instruction-response pairs via token classification.")],
    98: [("LoRA?", "Low-Rank Adaptation. Decomposes weight updates into low-rank matrices B and A.")],
    99: [("RAG?", "Retrieval Augmented Generation. Enhancing LLM queries by retrieving text from document database.")],
    100: [("Model Card?", "Standard documentation card explaining training datasets, architectures, and evaluation metrics.")]
}
replace_placeholders(w14_path, w14_preds, w14_cards)

# Mappings for Week 15
w15_preds = {
    101: ("# Day 101: OpenAI API streaming output\\n# If streaming is enabled, chunks are returned as type", "generator"),
    102: ("# Day 102: Pydantic validation\\n# If field age has limit age >= 18, input 17 throws what error?", "ValidationError"),
    103: ("# Day 103: LCEL chain execution\\n# chain = prompt | model | parser. What operator chains them?", "|"),
    104: ("# Day 104: ChromaDB save location\\n# If persist_directory is not set, Chroma database is stored in", "memory"),
    105: ("# Day 105: Cross-Encoder output type\\n# Cross-Encoder evaluates query-document relevance as a score between", "0 and 1"),
    106: ("# Day 106: LangChain agent loop\\n# What reasoning loop does standard LangChain agents execute?", "ReAct"),
    107: ("# Day 107: Capstone citation format\\n# CITATION indicator added next to response targets", "[Source]")
}
w15_cards = {
    101: [("LLM APIs?", "Querying foundational models using providers like OpenAI, Anthropic, or Gemini.")],
    102: [("Structured Extraction?", "Using function calling or JSON schemas to force LLMs to output valid structured objects.")],
    103: [("LCEL?", "LangChain Expression Language. A declarative way to compose chains with streaming support.")],
    104: [("Vector DB?", "Database specialized in storing high-dimensional vector embeddings for similarity searches.")],
    105: [("Reranking?", "Cross-encoder scoring retrieved documents against query, improving precision over cosine similarity.")],
    106: [("ReAct Pattern?", "Reasoning and Acting loop where agents plan actions, execute tools, and observe results.")],
    107: [("GenAI Capstone goal?", "Build a complete document RAG research assistant with citations and conversation history.")]
}
replace_placeholders(w15_path, w15_preds, w15_cards)

# Mappings for Week 16
w16_preds = {
    108: ("# Day 108: QLoRA quantization format\\n# Frozen base weights in QLoRA are loaded in what normal format?", "NF4"),
    109: ("# Day 109: MLflow log metric\\n# mlflow.log_metric(\\'accuracy\\', 0.95) saves accuracy value as", "float"),
    110: ("# Day 110: CrewAI Agent role\\n# Does standard multi-agent frameworks execute tasks sequentially or in parallel?", "sequential"),
    111: ("# Day 111: Model Context Protocol (MCP)\\n# Standard MCP allows LLMs to query external databases using what API protocol?", "JSON-RPC"),
    112: ("# Day 112: FastAPI endpoint return\\n# If view returns a Pydantic model, FastAPI converts it to", "JSON"),
    113: ("# Day 113: SSE content type\\n# Server-Sent Events content type for streaming is text/", "event-stream"),
    114: ("# Day 114: Docker image layer caching\\n# If COPY requirements.txt is cached, pip install is", "cached"),
    115: ("# Day 115: Prometheus metrics tracking\\n# Prometheus collects metrics by doing pull or push request?", "pull"),
    116: ("# Day 116: RAGAS faithfulness metric\\n# Evaluates if answer is strictly grounded in context (0.0 to 1.0)", "1.0"),
    117: ("# Day 117: Vector Index partition\\n# Partitioning index by metadata column is called metadata", "filtering")
}
w16_cards = {
    108: [("QLoRA NF4?", "NormalFloat4. Data type optimized for normally distributed model weights.")],
    109: [("MLflow tracking?", "Observability server recording parameters, metrics, and models across runs.")],
    110: [("Multi-agent systems?", "Orchestrating multiple autonomous agents with specific roles to collaborate on tasks.")],
    111: [("MCP?", "Model Context Protocol. Standard protocol allowing LLMs to access tools and data sources safely.")],
    112: [("FastAPI?", "Modern, fast web framework for building APIs with Python 3.8+ based on standard type hints.")],
    113: [("Server-Sent Events?", "HTTP streaming standard allowing servers to push real-time text updates to clients.")],
    114: [("Docker Layer Caching?", "Caching build steps to speed up Docker image creation. Put requirements.txt before code.")],
    115: [("Prometheus?", "Open-source monitoring tool scraping metric endpoints to record time-series data.")],
    116: [("RAGAS?", "Evaluation framework analyzing RAG pipelines on faithfulness, relevance, and context metrics.")],
    117: [("Production RAG?", "Hybrid search, cross-encoder reranking, and caching layer deployed inside Docker containers.")]
}
replace_placeholders(w16_path, w16_preds, w16_cards)

# Mappings for Week 17
w17_preds = {
    118: ("# Day 118: Flask routing parameters\\n# @app.route(\\'/user/&lt;int:id&gt;\\') parses id as which type?", "int"),
    119: ("# Day 119: Flask JSON return helper\\n# Helper function to convert dict to JSON Response in Flask", "jsonify"),
    120: ("# Day 120: Model loading with joblib\\n# model = joblib.load(\\'model.pkl\\') returns what type of object?", "model"),
    121: ("# Day 121: Docker run port mapping\\n# docker run -p 8080:5000 maps host port 8080 to container port", "5000"),
    122: ("# Day 122: Dockerfile directive for default run command\\n# Directive to specify default executable when container runs", "CMD"),
    123: ("# Day 123: Docker Compose up command\\n# Command to launch and build all compose services", "docker-compose up --build"),
    124: ("# Day 124: Render sleep duration\\n# Free Render web service sleeps after how many minutes of inactivity?", "15")
}
w17_cards = {
    118: [("Flask Blueprint?", "Organizes a group of related views and routes to keep application structure modular.")],
    119: [("REST API?", "Representational State Transfer. Stateless, client-server architecture using standard HTTP verbs.")],
    120: [("Gunicorn?", "WSGI HTTP server for Unix, serving Flask apps concurrently using pre-fork worker processes.")],
    121: [("Docker Image?", "Read-only template containing instructions to build and launch a container instance.")],
    122: [("Multi-stage Docker build?", "Using multiple FROM statements to compile resources, leaving build tools out of final image.")],
    123: [("Docker Compose?", "Tool for defining and running multi-container Docker applications via yaml configurations.")],
    124: [("Containerized Deploy?", "Pushing a packaged Docker container to platforms like Render, Railway, or Cloud Run.")]
}
replace_placeholders(w17_path, w17_preds, w17_cards)

# Mappings for Week 18
w18_preds = {
    125: ("# Day 125: Capstone Track Option count\\n# Total choice project tracks provided for capstone selection", "3"),
    126: ("# Day 126: GenAI Track Vector Store\\n# Recommended local vector database for Capstone Option A", "ChromaDB"),
    127: ("# Day 127: ML Track algorithm\\n# Target model for the fraud detection project option", "XGBoost"),
    128: ("# Day 128: Vision Track CNN model\\n# Real-time detector model used for CV Option C", "YOLOv8"),
    129: ("# Day 129: Container registry\\n# Registry hosting custom built Docker images", "Docker Hub"),
    130: ("# Day 130: GitHub Pinned Repos\\n# Max count of projects you can pin to your GitHub profile", "6"),
    131: ("# Day 131: Resume format standard\\n# System standard scanning format for resume parsing engines", "ATS"),
    132: ("# Day 132: Interview Prep QA\\n# Bias-variance trade-off: high model complexity leads to high", "variance"),
    133: ("# Day 133: SQL window function\\n# Function to calculate ranking partition within departments", "DENSE_RANK"),
    134: ("# Day 134: Python Leetcode targets\\n# Total target resolved LeetCode exercises completed", "50"),
    135: ("# Day 135: AI/ML Roadmap complete status\\n# Total days covered in this comprehensive guide", "135")
}
w18_cards = {
    125: [("Capstone Goal?", "Build a job-ready portfolio project demonstrating full end-to-end ML or GenAI capabilities.")],
    126: [("GenAI Capstone track?", "Multi-document RAG research assistant with Streamlit, ChromaDB, and Docker deployment.")],
    127: [("ML Capstone track?", "End-to-end fraud detection system from cleaning to API and live monitoring dashboard.")],
    128: [("Vision Capstone track?", "Real-time webcam object detection application using YOLOv8, Flask, and Docker.")],
    129: [("Production deployment?", "Deploying multi-container Compose setups to Railway or Render platforms.")],
    130: [("GitHub Portfolio?", "Pinning 6 best repositories with detailed READMEs and demo links.")],
    131: [("ATS Resume?", "Applicant Tracking System compliant format mapping direct impact statements (X achieved Y via Z).")],
    132: [("Bias-Variance Trade-off?", "Underfitting (high bias) vs Overfitting (high variance). Model complexity balances them.")],
    133: [("SQL Joins?", "Matching records via INNER, LEFT, RIGHT, or OUTER key alignments.")],
    134: [("Leetcode focus?", "Arrays, Strings, Hash Maps, and Two Pointer algorithms for screening interviews.")],
    135: [("Roadmap Complete!", "Celebrate your journey, update LinkedIn, and begin applying for AI/ML roles.")]
}
replace_placeholders(w18_path, w18_preds, w18_cards)

print("🎉 Patch script execution complete!")
