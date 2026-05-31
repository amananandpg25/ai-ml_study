import re
import os

def generate_week14():
    week13_path = '/Users/amananand/Downloads/SDE/ai:ml/week13.html'
    week14_path = '/Users/amananand/Downloads/SDE/ai:ml/week14.html'
    
    with open(week13_path, 'r', encoding='utf-8') as f:
        week13_content = f.read()
        
    style_match = re.search(r'<style>(.*?)</style>', week13_content, re.DOTALL)
    if not style_match:
        print("CSS style block not found in week13.html!")
        return
    css_content = style_match.group(1)
    
    css_content = css_content.replace('--accent:var(--purple);', '--accent:var(--pink);')
    css_content = css_content.replace('var(--blue)', 'var(--pink)')
    css_content = css_content.replace('#6c8cff', '#e56b8c')
    
    # Construct complete HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Week 14 — Transformers & Attention | 135-Day AI/ML Roadmap</title>
<style>
{css_content}
/* Additional styles for Mermaid and advanced elements */
.mermaid {{ background: var(--bg3); padding: 1.5rem; border-radius: 10px; border: 1px solid var(--border); margin: 1.5rem 0; overflow-x: auto; text-align: center; }}
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.2.0/dist/mermaid.min.js"></script>
</head>
<body>

<div class="xp-toast" id="xp-toast">+50 XP ⚡</div>

<nav class="topnav">
  <div class="topnav-left">
    <button class="mob-menu-btn" onclick="toggleSidebar()">☰ Menu</button>
    <div class="brand">Week 14 — Transformers & Attention</div>
    <div class="xp-display" id="xp-show">⚡ 0 XP</div>
    <div class="streak-display" id="streak-show">🔥 0 day streak</div>
  </div>
  <div style="display:flex;align-items:center;gap:.8rem">
    <div class="prog-wrap">
      <div class="prog-outer"><div class="prog-inner" id="prog-bar"></div></div>
      <span id="prog-text">0/7 days</span>
    </div>
    <div class="day-pills">
      <div class="day-pill active" onclick="goDay(94)" id="pill-94">94</div>
      <div class="day-pill" onclick="goDay(95)" id="pill-95">95</div>
      <div class="day-pill" onclick="goDay(96)" id="pill-96">96</div>
      <div class="day-pill" onclick="goDay(97)" id="pill-97">97</div>
      <div class="day-pill" onclick="goDay(98)" id="pill-98">98</div>
      <div class="day-pill" onclick="goDay(99)" id="pill-99">99</div>
      <div class="day-pill" onclick="goDay(100)" id="pill-100">100</div>
    </div>
  </div>
</nav>

<div class="layout">

<aside class="sidebar" id="sidebar">
  <div class="sb-label">Week 14 — Days</div>
  <div class="sb-item active" onclick="goDay(94);closeSidebar()" id="sb-94"><span class="sb-dot" style="background:var(--pink)"></span>Day 94 — Attention Math</div>
  <div class="sb-item" onclick="goDay(95);closeSidebar()" id="sb-95"><span class="sb-dot" style="background:var(--purple)"></span>Day 95 — Transformers & RoPE</div>
  <div class="sb-item" onclick="goDay(96);closeSidebar()" id="sb-96"><span class="sb-dot" style="background:var(--orange)"></span>Day 96 — BERT & MLM Theory</div>
  <div class="sb-item" onclick="goDay(97);closeSidebar()" id="sb-97"><span class="sb-dot" style="background:var(--green)"></span>Day 97 — HF Tokenizer Mechanics</div>
  <div class="sb-item" onclick="goDay(98);closeSidebar()" id="sb-98"><span class="sb-dot" style="background:var(--pink)"></span>Day 98 — GPT-2 & nanoGPT</div>
  <div class="sb-item" onclick="goDay(99);closeSidebar()" id="sb-99"><span class="sb-dot" style="background:var(--teal)"></span>Day 99 — Fine-tuning BERT</div>
  <div class="sb-item" onclick="goDay(100);closeSidebar()" id="sb-100"><span class="sb-dot" style="background:var(--yellow)"></span>Day 100 — HF Spaces Spaces</div>
  <div class="sb-divider"></div>
  <div class="sb-label">Progress</div>
  <div class="sb-item"><span class="sb-dot" style="background:var(--orange)"></span><span id="sb-xp">0 XP earned</span></div>
  <div class="sb-item"><span class="sb-dot" style="background:var(--pink)"></span><span id="sb-streak">0 day streak</span></div>
  <div class="sb-divider"></div>
  <div class="sb-label">Quick Jump</div>
  <div class="sb-item" onclick="jumpTo('theory')"><span class="sb-dot" style="background:var(--pink)"></span>Theory</div>
  <div class="sb-item" onclick="jumpTo('tasks-section')"><span class="sb-dot" style="background:var(--orange)"></span>Tasks</div>
  <div class="sb-item" onclick="jumpTo('quiz-section')"><span class="sb-dot" style="background:var(--purple)"></span>Quiz</div>
  <div class="sb-item" onclick="jumpTo('resources-section')"><span class="sb-dot" style="background:var(--green)"></span>Resources</div>
</aside>

<main class="main">

<!-- ═══════════════════════════════════════
     DAY 94
     ════════════════════════════════════════ -->
<div class="day-section active" id="day-94">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 94 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>The Mathematics of Scaled Dot-Product Attention</h1>
    <p>Understanding the fundamental limits of recurrent models and deriving the mathematical foundation of Self-Attention, Queries, Keys, Values, and the necessity of temperature scaling (1/&radic;d_k).</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">🧠 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
      <span class="meta-badge b">🔬 Linear Algebra</span>
    </div>
  </div>

  <div class="objectives">
    <h3>🎯 Objectives:</h3>
    <ul>
      <li>Mathematically define the Seq2Seq Information Bottleneck.</li>
      <li>Derive the Attention matrix computations using linear projections.</li>
      <li>Analyze the gradient saturation problem in unscaled dot products.</li>
      <li>Implement a computationally optimal causal masked self-attention block.</li>
    </ul>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Information Bottleneck in RNNs</h3>
    <p>In standard sequence-to-sequence models (e.g., LSTMs), an entire input sequence of length <em>T</em> is encoded into a fixed-dimensional context vector <em>h_T &isin; &reals;^d</em>. For large <em>T</em>, compressing a distribution of variable length into a static bounded space leads to high information loss. The Jacobian matrix of hidden states across time steps reveals exponentially decaying singular values, proving that long-term dependencies vanish.</p>
    
    <h3 class="sh3">2. Q, K, V Projections</h3>
    <p>Attention resolves this by allowing the decoder to access a soft-addressed memory of all encoder states. We project the input embeddings <em>X &isin; &reals;^(T &times; d_model)</em> into three distinct sub-spaces using learned weight matrices:</p>
    <div class="math-block">
      <span class="formula">Q = X W_Q &nbsp; (where W_Q &isin; &reals;^(d_model &times; d_k))</span>
      <span class="formula">K = X W_K &nbsp; (where W_K &isin; &reals;^(d_model &times; d_k))</span>
      <span class="formula">V = X W_V &nbsp; (where W_V &isin; &reals;^(d_model &times; d_v))</span>
      <span class="desc">Q represents what we are searching for, K acts as the database index, and V is the actual feature content.</span>
    </div>

    <h3 class="sh3">3. Deriving Scaled Dot-Product Attention</h3>
    <p>The unscaled attention scores are given by <em>S = Q K^T</em>. If components of Q and K are independent random variables with mean 0 and variance 1, the dot product will have mean 0 and variance <em>d_k</em>. For a large <em>d_k</em> (e.g., 64), the variance is 64.</p>
    <p>Passing a vector with high variance into the Softmax function pushes the values to the tails of the exponential curve, where the derivative of softmax approaches zero. This causes <strong>gradient saturation</strong> and halts learning. To solve this, we scale by the standard deviation <em>&radic;d_k</em>.</p>

    <div class="math-block">
      <span class="formula">Attention(Q, K, V) = Softmax( (Q K^T) / &radic;d_k ) V</span>
    </div>

    <div class="mermaid">
      graph TD
      Q["Query Q"] --> M1["MatMul"]
      K["Key K"] --> T["Transpose K^T"]
      T --> M1
      M1 --> S["Scale by 1/&radic;d_k"]
      S --> Mask["Mask (optional)"]
      Mask --> Softmax["Softmax"]
      Softmax --> M2["MatMul"]
      V["Value V"] --> M2
      M2 --> Out["Output Vector"]
    </div>
    <div class="diagram-cap">Scaled Dot-Product Attention tensor operations pipeline</div>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — causal_attention.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> torch
<span class="kw">import</span> torch.nn.functional <span class="kw">as</span> F
<span class="kw">import</span> math

<span class="kw">def</span> <span class="fn">causal_self_attention</span>(q, k, v, mask=<span class="bi">True</span>):
    <span class="cm"># q, k, v shapes: [batch_size, seq_len, d_k]</span>
    d_k = q.size(-<span class="num">1</span>)
    seq_len = q.size(-<span class="num">2</span>)
    
    <span class="cm"># 1. Dot product: (Q @ K.T) / sqrt(d_k)</span>
    scores = torch.matmul(q, k.transpose(-<span class="num">2</span>, -<span class="num">1</span>)) / math.sqrt(d_k)
    
    <span class="cm"># 2. Causal Masking (autoregressive property)</span>
    <span class="kw">if</span> mask:
        <span class="cm"># lower triangular matrix of ones</span>
        causal_mask = torch.tril(torch.ones(seq_len, seq_len, device=q.device))
        <span class="cm"># replace 0s with -infinity</span>
        scores = scores.masked_fill(causal_mask == <span class="num">0</span>, float(<span class="str">'-inf'</span>))
        
    <span class="cm"># 3. Softmax along the last dimension (keys)</span>
    attn_weights = F.softmax(scores, dim=-<span class="num">1</span>)
    
    <span class="cm"># 4. Multiply with values</span>
    output = torch.matmul(attn_weights, v)
    <span class="kw">return</span> output, attn_weights</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">QUESTION 1</div>
      <div class="quiz-q">Mathematically, what is the variance of the dot product of two vectors of size d_k, assuming their elements are i.i.d with mean 0 and variance 1?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q94')"><span class="quiz-letter">A</span> 1 / &radic;d_k</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q94')"><span class="quiz-letter">B</span> d_k</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q94')"><span class="quiz-letter">C</span> &radic;d_k</div>
      <div class="quiz-feedback correct-fb" id="q94-correct">✅ Correct! The variance of the sum of independent variables is the sum of their variances, which equals d_k. Scaling by &radic;d_k brings the standard deviation back to 1.</div>
      <div class="quiz-feedback wrong-fb" id="q94-wrong">❌ Incorrect. Review the properties of variance for independent random variables.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.06)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Implement FlashAttention Concept (Tiling)</span>
        <span class="task-time">⏱ 90 min</span>
      </div>
      <div class="task-body">
        <p>Standard attention has <code>O(N^2)</code> memory complexity because it instantiates the full <code>N x N</code> attention matrix. FlashAttention avoids this by block-tiling the computation and keeping it in fast SRAM. Write a naive PyTorch implementation of block-wise attention (without fused CUDA kernels) that iterates over chunks of queries and keys to calculate the output without ever instantiating the full <code>N x N</code> score matrix.</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://arxiv.org/abs/1706.03762" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">Attention Is All You Need</div>
        <div class="rc-sub">Vaswani et al. (2017)</div>
      </a>
      <a class="resource-card" href="https://arxiv.org/abs/2205.14135" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">FlashAttention</div>
        <div class="rc-sub">Fast and Memory-Efficient Exact Attention with IO-Awareness (Dao et al. 2022)</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-94" onclick="completeDay(94, 150)">✓ Mark Day 94 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 95
     ════════════════════════════════════════ -->
<div class="day-section" id="day-95">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 95 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>Transformer Architecture & Modern Positional Encodings (RoPE)</h1>
    <p>Constructing the full Encoder-Decoder stack, understanding Multi-Head Attention, and upgrading from sinusoidal absolute position embeddings to Rotary Positional Embeddings (RoPE) used in LLaMA.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. The Transformer Architecture</h3>
    <div class="mermaid">
      graph TD
      subgraph EncoderBlock [Encoder]
      E1[Input Embeddings] --> E2[Add Positional Encoding]
      E2 --> E3[Multi-Head Self Attention]
      E3 --> E4[Add & Norm]
      E4 --> E5[Feed Forward Network]
      E5 --> E6[Add & Norm]
      end
      
      subgraph DecoderBlock [Decoder]
      D1[Target Embeddings] --> D2[Add Positional Encoding]
      D2 --> D3[Masked Multi-Head Attention]
      D3 --> D4[Add & Norm]
      E6 --> D5[Cross-Attention]
      D4 --> D5
      D5 --> D6[Add & Norm]
      D6 --> D7[Feed Forward Network]
      D7 --> D8[Add & Norm]
      end
    </div>
    <div class="diagram-cap">Standard Transformer Encoder-Decoder Block Connections</div>

    <h3 class="sh3">2. Rotary Positional Embeddings (RoPE)</h3>
    <p>The original Transformer used Absolute Positional Encodings (adding sine/cosine waves to token vectors). Modern LLMs (like LLaMA and Mistral) use <strong>RoPE</strong>, which encodes relative position by rotating the query and key representations in a 2D plane by an angle proportional to their absolute position.</p>
    <div class="math-block">
      <span class="formula">RoPE(x_m) = x_m * cos(m&theta;) + [-x_m(2), x_m(1)] * sin(m&theta;)</span>
      <span class="desc">Where m is the absolute position. The inner product between two rotated vectors naturally decays relative to their distance (m - n), giving strong relative position bias.</span>
    </div>

    <h3 class="sh3">3. Pre-LN vs Post-LN</h3>
    <p>Original Transformers used Post-LayerNorm (LayerNorm after residual connections). This led to severe gradient vanishing during early training, requiring a long learning rate warmup. Modern architectures (GPT-2, LLaMA) use Pre-LayerNorm (LayerNorm inside the residual block), allowing for stable training without warmup.</p>
    
    <h3 class="sh3">4. Autoregressive Generation & KV Caching</h3>
    <p>During inference, decoder models generate tokens one by one. Recomputing attention for all past tokens at every step is computationally expensive <em>O(N^2)</em>. <strong>KV Caching</strong> solves this by storing the previously computed Key and Value vectors for past tokens in memory. At step <em>t</em>, we only compute the Query, Key, and Value for the new token, and append its K and V to the cache, reducing time complexity per step to <em>O(N)</em>.</p>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.06)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Implement RoPE from Scratch</span>
        <span class="task-time">⏱ 90 min</span>
      </div>
      <div class="task-body">
        <p>Implement the <code>apply_rotary_emb(q, k, freqs_cis)</code> function in PyTorch as described in the RoPE paper. You will need to reshape vectors into complex numbers (<code>torch.view_as_complex</code>), multiply by complex exponentials of frequencies, and cast back to real tensors.</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://arxiv.org/abs/2104.09864" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">RoFormer: Enhanced Transformer with Rotary Position Embedding</div>
      </a>
      <a class="resource-card" href="https://arxiv.org/abs/2002.04745" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">On Layer Normalization in the Transformer Architecture</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-95" onclick="completeDay(95, 150)">✓ Mark Day 95 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 96
     ════════════════════════════════════════ -->
<div class="day-section" id="day-96">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 96 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>BERT, GPT & Language Modeling Objectives</h1>
    <p>Deep dive into Bidirectional Encoders (BERT), Autoregressive Decoders (GPT), Masked vs Causal Language Modeling, and how we evaluate them using Perplexity.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. BERT: Masked Language Modeling (MLM)</h3>
    <p>Unlike autoregressive models, BERT relies entirely on the Transformer Encoder without causal masks. The self-supervised task is <strong>Masked Language Modeling (MLM)</strong>, where 15% of tokens are corrupted and predicted using cross-entropy loss. BERT follows the 80-10-10 masking rule to mitigate train-test discrepancies (80% [MASK], 10% random, 10% original).</p>
    
    <h3 class="sh3">2. GPT: Causal Language Modeling (CLM)</h3>
    <p>GPT and LLaMA are <strong>Decoder-only</strong> models. They use a strict lower-triangular causal mask so tokens can only attend to past tokens. Their objective is <strong>Next Token Prediction</strong> (Autoregressive Generation). While BERT learns deep bidirectional context for understanding tasks, GPT excels at generative tasks by modeling the joint probability of a sequence as a product of conditional probabilities.</p>

    <div class="mermaid">
      graph LR
      subgraph BERTBlock [BERT: Bidirectional Attention]
      B1["Token 1"] --- B2["Token 2"]
      B2 --- B3["Token 3"]
      B1 --- B3
      end
      subgraph GPTBlock [GPT: Causal Masked Attention]
      G1["Token 1"] --> G2["Token 2"]
      G1 --> G3["Token 3"]
      G2 --> G3
      end
    </div>
    <div class="diagram-cap">Bidirectional vs Causal (Autoregressive) Attention flows</div>

    <h3 class="sh3">3. NLP Evaluation Metrics</h3>
    <p>How do we know if a language model is good?</p>
    <ul>
      <li><strong>Perplexity (PPL):</strong> The exponentiated average negative log-likelihood of a sequence. Lower is better. A perplexity of 10 means the model is as confused as if it had to guess uniformly among 10 words.</li>
      <li><strong>BLEU:</strong> Used for translation. Measures n-gram precision between generated and reference text.</li>
      <li><strong>ROUGE:</strong> Used for summarization. Measures n-gram recall (how much of the reference text was captured).</li>
    </ul>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(247,169,75,.06)" onclick="toggleTask(this)">
        <span class="task-badge tb-med">🟡 MEDIUM</span>
        <span class="task-title">Custom MLM Data Collator</span>
        <span class="task-time">⏱ 60 min</span>
      </div>
      <div class="task-body">
        <p>Write a PyTorch <code>DataCollator</code> class that takes a batch of tokenized sequences and applies the 80-10-10 masking strategy manually. Return the <code>input_ids</code>, <code>attention_mask</code>, and <code>labels</code> (with -100 for unmasked tokens to ignore in CrossEntropy calculation).</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://arxiv.org/abs/1810.04805" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">BERT</div>
      </a>
      <a class="resource-card" href="https://arxiv.org/abs/1907.11692" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">RoBERTa</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-96" onclick="completeDay(96, 150)">✓ Mark Day 96 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 97
     ════════════════════════════════════════ -->
<div class="day-section" id="day-97">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 97 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>Hugging Face Ecosystem & Advanced Tokenizers</h1>
    <p>Mastering BPE, WordPiece, and the Hugging Face `transformers` API for distributed training and inference.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 5 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Subword Tokenization Algorithms</h3>
    <p>Out of Vocabulary (OOV) issues break word-level tokenization. Modern models use subwords:</p>
    <ul>
      <li><strong>BPE (Byte Pair Encoding):</strong> Merges the most frequent pairs of bytes/characters iteratively. Used in GPT.</li>
      <li><strong>WordPiece:</strong> Merges pairs that maximize the language model likelihood (Score = freq(ab) / (freq(a)*freq(b))). Used in BERT.</li>
      <li><strong>SentencePiece (Unigram):</strong> Starts with a massive vocabulary and iteratively prunes tokens that cause the smallest drop in total probability. Used in LLaMA / ALBERT.</li>
    </ul>

    <div class="mermaid">
      graph TD
      Raw["Raw Input Text"] --> Norm["Normalizer\nLowercase, strip accents, Unicode normalization"]
      Norm --> PreT["Pre-Tokenizer\nSplits on whitespace and punctuation"]
      PreT --> Mod["Subword Model\nApplies trained BPE / WordPiece rules"]
      Mod --> PostP["Post-Processor\nApplies special tokens: CLS, SEP"]
      PostP --> Out["Tokenizer Output\ninput_ids, attention_mask"]
    </div>
    <div class="diagram-cap">Hugging Face Fast Tokenization pipeline stages</div>

    <h3 class="sh3">2. Fast Tokenizers in Rust</h3>
    <p>Hugging Face's `tokenizers` library is written in Rust, utilizing a highly parallelized pipeline (Normalization -> Pre-tokenization -> Model -> Post-processing) allowing encoding of 1GB of text in under 20 seconds.</p>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.06)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Train a Custom BPE Tokenizer</span>
        <span class="task-time">⏱ 60 min</span>
      </div>
      <div class="task-body">
        <p>Using the <code>tokenizers</code> library (not <code>transformers</code>), build and train a BPE tokenizer from scratch on a downloaded text corpus. Define the normalizer (NFKC), pre-tokenizer (ByteLevel), and train it with a vocab size of 10,000. Save it and load it back using <code>PreTrainedTokenizerFast</code>.</p>
      </div>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-97" onclick="completeDay(97, 150)">✓ Mark Day 97 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 98
     ════════════════════════════════════════ -->
<div class="day-section" id="day-98">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 98 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>GPT-2 Architecture & nanoGPT Study</h1>
    <p>Transitioning from BERT encoders to autoregressive decoder models. We study the GPT-2 block architecture, pre-LayerNorm stability, and analyze Andrej Karpathy's open-source nanoGPT repository.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
      <span class="meta-badge t">nanoGPT Walkthrough</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Decoders vs Encoders</h3>
    <p>BERT is an encoder-only model that learns bidirectional representations. GPT (Generative Pre-trained Transformer) is a **decoder-only** model that generates text autoregressively. This requires a causal mask to ensure the token at position $t$ can only attend to tokens at positions $1, ..., t$.</p>

    <h3 class="sh3">2. GPT-2 Block Architecture</h3>
    <p>GPT-2 uses Pre-LayerNorm (applying normalization before attention and FeedForward blocks, rather than after residual connections). This establishes a clean path for gradient flow through the network, allowing training to start without a warm-up phase.</p>

    <div class="mermaid">
      graph TD
      Input["Block Input x"] --> LN1["LayerNorm 1"]
      LN1 --> MHA["Multi-Head Causal Attention"]
      MHA --> Add1["Residual Add"]
      Input --> Add1
      Add1 --> LN2["LayerNorm 2"]
      LN2 --> MLP["FeedForward MLP (GELU)"]
      MLP --> Add2["Residual Add"]
      Add1 --> Add2
      Add2 --> Output["Block Output"]
    </div>
    <div class="diagram-cap">GPT-2 Pre-LayerNorm Transformer Block Layer Connections</div>

    <h3 class="sh3">3. Next-Token Prediction & Autoregressive Inference</h3>
    <p>A decoder model outputs logits of shape <code>(Batch, SeqLen, VocabSize)</code>. During training, the target is the input sequence shifted left by one token. During inference, we run the model on a prompt, extract the logits for the *last* token, apply temperature and top-k filtering, sample a token, append it to the input, and repeat.</p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — gpt_block.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> torch
<span class="kw">import</span> torch.nn <span class="kw">as</span> nn

<span class="kw">class</span> <span class="fn">GPT2MLP</span>(nn.Module):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, d_model):
        <span class="bi">super</span>().__init__()
        self.c_fc = nn.Linear(d_model, 4 * d_model)
        self.gelu = nn.GELU()
        self.c_proj = nn.Linear(4 * d_model, d_model)
        self.dropout = nn.Dropout(0.1)

    <span class="kw">def</span> <span class="fn">forward</span>(self, x):
        x = self.c_fc(x)
        x = self.gelu(x)
        x = self.c_proj(x)
        x = self.dropout(x)
        return x</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">What is the structural difference between Pre-LayerNorm and Post-LayerNorm?</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q98-1')"><span class="quiz-letter">A</span> Pre-LN applies LayerNorm at the beginning of sub-blocks before attention and MLP layers, which stabilizes gradients.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q98-1')"><span class="quiz-letter">B</span> Pre-LN is only used in bidirectional encoders like BERT.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q98-1')"><span class="quiz-letter">C</span> Pre-LN requires an extra set of trainable weights.</div>
      <div class="quiz-feedback correct-fb" id="q98-1-correct">✅ Correct! Pre-LN establishes an unblocked identity path for the residual gradients, preventing vanishing or exploding gradients.</div>
      <div class="quiz-feedback wrong-fb" id="q98-1-wrong">❌ Incorrect. Look at the positioning of LayerNorm relative to the residual blocks.</div>
    </div>
    <div class="quiz-block">
      <div class="quiz-num">Q2 OF 3</div>
      <div class="quiz-q">In next-token prediction, what is the target output shape of the logits when training on input batch size B, sequence length S, and vocabulary size V?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q98-2')"><span class="quiz-letter">A</span> (B, S)</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q98-2')"><span class="quiz-letter">B</span> (B, S, V)</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q98-2')"><span class="quiz-letter">C</span> (B, V)</div>
      <div class="quiz-feedback correct-fb" id="q98-2-correct">✅ Correct! The model computes logits for every possible word in the vocabulary, at every timestep, for every sample in the batch.</div>
      <div class="quiz-feedback wrong-fb" id="q98-2-wrong">❌ Incorrect. Recall that a probability distribution must be computed for each token slot.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Tasks</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(79,209,165,.05);border-left:3px solid var(--green)" onclick="toggleTask(this)">
        <span class="task-badge tb-easy">🟢 EASY</span>
        <span class="task-title">Generate Causal Mask</span>
        <span class="task-time">⏱ 20 min</span>
      </div>
      <div class="task-body">
        <p>Write a PyTorch script to create a lower triangular causal mask of size 5x5 using <code>torch.tril</code>. Verify that elements above the diagonal are filled with <code>-inf</code>.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d98t1')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d98t1">
          <pre><span class="kw">import</span> torch
mask = torch.tril(torch.ones(5, 5))
masked_scores = torch.zeros(5, 5).masked_fill(mask == 0, float('-inf'))
print(masked_scores)</pre>
        </div>
      </div>
    </div>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Walkthrough nanoGPT Attention Code</span>
        <span class="task-time">⏱ 90 min</span>
      </div>
      <div class="task-body">
        <p>Inspect Andrej Karpathy's <code>model.py</code> in the <code>nanoGPT</code> repository. Implement a PyTorch module <code>CausalSelfAttention</code> that mirrors nanoGPT's handling of key-query-value projections, causal masking, attention dropout, and residual projections.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d98t2')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d98t2">
          <pre><span class="kw">import</span> torch
<span class="kw">import</span> torch.nn <span class="kw">as</span> nn
<span class="kw">import</span> math

<span class="kw">class</span> <span class="fn">CausalSelfAttention</span>(nn.Module):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, d_model, n_head):
        <span class="bi">super</span>().__init__()
        self.c_attn = nn.Linear(d_model, 3 * d_model)
        self.c_proj = nn.Linear(d_model, d_model)
        self.n_head = n_head
        self.d_model = d_model

    <span class="kw">def</span> <span class="fn">forward</span>(self, x):
        B, T, C = x.size()
        q, k, v = self.c_attn(x).split(self.d_model, dim=2)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        
        y = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True)
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.c_proj(y)</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://www.youtube.com/watch?v=kCc8FmEb1nY" target="_blank">
        <div class="rc-type">🎥 YOUTUBE</div>
        <div class="rc-title">Let's build GPT: from scratch, in code — Karpathy</div>
        <div class="rc-sub">The definitive 2-hour video tutorial detailing how to code a decoder transformer.</div>
      </a>
      <a class="resource-card" href="https://github.com/karpathy/nanoGPT" target="_blank">
        <div class="rc-type">💻 GITHUB</div>
        <div class="rc-title">nanoGPT Repository</div>
        <div class="rc-sub">Cleanest, most readable PyTorch repository for training medium-sized GPTs.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-98" onclick="completeDay(98, 150)">✓ Mark Day 98 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 99
     ════════════════════════════════════════ -->
<div class="day-section" id="day-99">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 99 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>Capstone Part 1: Fine-Tuning BERT for Sequence Classification</h1>
    <p>Applying pre-trained language models to practical tasks. Today, we write a complete PyTorch script to load a BERT/DistilBERT checkpoint, set up a classification head, and train it on a custom text classifier.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 8 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +200 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. BERT's Classification Mechanism</h3>
    <p>BERT uses a special classification token `[CLS]` at the start of every input sequence. In the final Encoder layer, the 768-dimensional output vector corresponding to this `[CLS]` token acts as a pooled representation of the entire sentence. To build a classifier, we pass this pooled vector into a Linear layer mapping to the number of classes.</p>

    <div class="mermaid">
      graph LR
      Tokens["Tokens: [CLS], x_1, x_2, ..."] --> BERTModel["BERT Encoder Layers"]
      BERTModel --> CLSOut["CLS Token final embedding (768-D)"]
      CLSOut --> LinearHead["Linear Classifier Layer"]
      LinearHead --> Logits["Class Logits / Probabilities"]
    </div>
    <div class="diagram-cap">BERT Sequence Classification pooling and classification head</div>

    <h3 class="sh3">2. Fine-Tuning vs Feature Extraction</h3>
    <p>In **Feature Extraction**, we freeze the BERT weights and only train the final classification head. In **Fine-Tuning**, we train the classification head AND update the weights of the BERT model itself using a very low learning rate (e.g., $2 \times 10^{-5}$). Fine-tuning yields much higher accuracy because the model adapts its representations to the domain.</p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — finetune_bert.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">from</span> transformers <span class="kw">import</span> AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
<span class="kw">from</span> datasets <span class="kw">import</span> Dataset

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

<span class="cm"># Load sample text classification dataset</span>
train_data = {{"text": ["This is great", "Terrible movie", "Highly recommend", "Waste of time"], "label": [1, 0, 1, 0]}}
ds = Dataset.from_dict(train_data)
tokenized_ds = ds.map(<span class="kw">lambda</span> x: tokenizer(x["text"], truncation=<span class="kw">True</span>, padding=<span class="str">"max_length"</span>, max_length=<span class="num">16</span>), batched=<span class="kw">True</span>)

args = TrainingArguments(
    output_dir="results",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    num_train_epochs=1,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_ds,
)
trainer.train()</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">Why is a very low learning rate (e.g., 2e-5) used when fine-tuning BERT?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q99-1')"><span class="quiz-letter">A</span> To prevent out-of-memory errors on the GPU.</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q99-1')"><span class="quiz-letter">B</span> To prevent overwriting the useful pre-trained features (catastrophic forgetting).</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q99-1')"><span class="quiz-letter">C</span> Because BERT is pre-quantized.</div>
      <div class="quiz-feedback correct-fb" id="q99-1-correct">✅ Correct! Large learning rates will destroy the pre-trained weights, causing the model to lose its general language understanding capabilities.</div>
      <div class="quiz-feedback wrong-fb" id="q99-1-wrong">❌ Incorrect. High learning rates overwrite the rich pre-trained language parameters completely.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Tasks</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(247,169,75,.05);border-left:3px solid var(--orange)" onclick="toggleTask(this)">
        <span class="task-badge tb-med">🟡 MEDIUM</span>
        <span class="task-title">Run BERT Inference</span>
        <span class="task-time">⏱ 30 min</span>
      </div>
      <div class="task-body">
        <p>Use Hugging Face <code>pipeline</code> API to load a pre-trained sentiment analysis model (e.g., <code>distilbert-base-uncased-finetuned-sst-2-english</code>). Run it on three customer reviews and print the predicted label and score.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d99t1')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d99t1">
          <pre><span class="kw">from</span> transformers <span class="kw">import</span> pipeline
classifier = pipeline("sentiment-analysis")
results = classifier(["I loved this course!", "It was okay.", "This is awful."])
for r in results:
    print(r)</pre>
        </div>
      </div>
    </div>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Fine-Tune DistilBERT on Custom Dataset</span>
        <span class="task-time">⏱ 120 min</span>
      </div>
      <div class="task-body">
        <p>Create a custom classification dataset with 10 reviews (5 positive, 5 negative). Complete the training script using Hugging Face <code>Trainer</code> to fine-tune <code>distilbert-base-uncased</code> on your dataset. Verify that the loss decreases after training.</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://huggingface.co/learn/nlp-course/chapter3/1" target="_blank">
        <div class="rc-type">🌐 COURSE</div>
        <div class="rc-title">Hugging Face NLP Course: Chapter 3</div>
        <div class="rc-sub">Detailed visual walkthrough of fine-tuning sequence models using PyTorch.</div>
      </a>
      <a class="resource-card" href="https://arxiv.org/abs/1910.01108" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">DistilBERT Paper (Sanh et al., 2019)</div>
        <div class="rc-sub">A distilled version of BERT: smaller, faster, cheaper.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-99" onclick="completeDay(99, 200)">✓ Mark Day 99 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 100
     ════════════════════════════════════════ -->
<div class="day-section" id="day-100">
  <div class="day-header">
    <div class="day-tag">WEEK 14 · DAY 100 · MONTH 4 — TRANSFORMERS & ATTENTION</div>
    <h1>Capstone Part 2: Serving Models via Gradio & Hugging Face Spaces</h1>
    <p>Finalizing the Week 14 Capstone. We build an interactive Gradio web application for our fine-tuned sentiment classifier and deploy it to Hugging Face Spaces using the Git Hub workflow.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +250 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Web UI Prototyping: Gradio</h3>
    <p>Gradio allows ML engineers to build interactive UIs directly in Python. It maps web input elements (like textboxes) directly to Python function arguments, runs the inference function, and renders the returns in output elements.</p>

    <h3 class="sh3">2. Hugging Face Spaces Ecosystem</h3>
    <p>Hugging Face Spaces is a free hosting platform for hosting Gradio and Streamlit models. Each Space acts as a git repository. To deploy, we push an <code>app.py</code> script and a <code>requirements.txt</code> file to the Hugging Face remote repository. HF automatically builds a Docker container and launches the application.</p>

    <div class="mermaid">
      graph LR
      LocalGit["Local Git Repo (app.py, reqs.txt)"] -->|"git push huggingface main"| HFSpace["Hugging Face Space Remote"]
      HFSpace -->|"Build Trigger"| DockerBuild["Docker Container Build"]
      DockerBuild -->|"Launch App"| LiveWeb["Live Public Web Application"]
    </div>
    <div class="diagram-cap">Hugging Face Spaces git-based deployment workflow</div>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — app.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> gradio <span class="kw">as</span> gr
<span class="kw">from</span> transformers <span class="kw">import</span> pipeline

<span class="cm"># Load model from Hugging Face Hub</span>
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

<span class="kw">def</span> <span class="fn">predict</span>(text):
    result = classifier(text)[0]
    return f\"Label: {{result['label']}} (Score: {{result['score']:.4f}})\"

demo = gr.Interface(
    fn=predict, 
    inputs=gr.Textbox(placeholder="Enter review text..."), 
    outputs="text",
    title="Sentiment Analysis Classifier"
)
demo.launch()</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">What file acts as the entrypoint for Hugging Face Spaces to run your Gradio application?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q100-1')"><span class="quiz-letter">A</span> server.js</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q100-1')"><span class="quiz-letter">B</span> app.py</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q100-1')"><span class="quiz-letter">C</span> index.html</div>
      <div class="quiz-feedback correct-fb" id="q100-1-correct">✅ Correct! Hugging Face Spaces looks for `app.py` as the default execution entrypoint.</div>
      <div class="quiz-feedback wrong-fb" id="q100-1-wrong">❌ Incorrect. HF Spaces expects a standard Python app entrypoint file.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Tasks</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(247,169,75,.05);border-left:3px solid var(--orange)" onclick="toggleTask(this)">
        <span class="task-badge tb-med">🟡 MEDIUM</span>
        <span class="task-title">Gradio Hello World</span>
        <span class="task-time">⏱ 30 min</span>
      </div>
      <div class="task-body">
        <p>Write a script to build a simple Gradio interface that accepts a user name text input and outputs "Hello {{name}}". Run it locally to verify the port binds correctly.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d100t1')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d100t1">
          <pre><span class="kw">import</span> gradio <span class="kw">as</span> gr
def greet(name):
    return f"Hello {{name}}!"
gr.Interface(fn=greet, inputs="text", outputs="text").launch()</pre>
        </div>
      </div>
    </div>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Write Space Deploy Manifests</span>
        <span class="task-time">⏱ 60 min</span>
      </div>
      <div class="task-body">
        <p>Prepare the deployment directory:
        <br>1. Create <code>app.py</code> with a Gradio interface loading your fine-tuned BERT classifier.
        <br>2. Create a <code>requirements.txt</code> file containing the necessary packages (<code>transformers</code>, <code>torch</code>, <code>gradio</code>).
        <br>3. Write down the sequence of Git commands needed to initialize, log in, add remote, and push to Hugging Face Spaces.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d100t2')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d100t2">
          <strong>Requirements.txt</strong>
          <pre>transformers
torch
gradio</pre>
          <br>
          <strong>Git Commands</strong>
          <pre># 1. Install Hugging Face Hub CLI and login
pip install huggingface_hub
huggingface-cli login

# 2. Add remote and push
git init
git add app.py requirements.txt
git commit -m "Initial commit of Gradio app"
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
git push -u origin main -f</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://gradio.app/quickstart/" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">Gradio Quickstart Guide</div>
        <div class="rc-sub">Official guide to building interactive web interfaces in Python.</div>
      </a>
      <a class="resource-card" href="https://huggingface.co/docs/hub/spaces" target="_blank">
        <div class="rc-type">📖 HF DOCS</div>
        <div class="rc-title">Hugging Face Spaces Guide</div>
        <div class="rc-sub">Official walkthrough for Git and Docker deployments on HF Hub.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-100" onclick="completeDay(100, 250)">✓ Mark Day 100 Complete</button>
</div>

</main>
</div>

<script>
// State Management
const STATE_KEY = 'w14-state';
let state = JSON.parse(localStorage.getItem(STATE_KEY)) || {{
  xp: 0,
  streak: 0,
  lastDate: null,
  completed: []
}};

function saveState() {{
  localStorage.setItem(STATE_KEY, JSON.stringify(state));
  updateUI();
}}

function updateUI() {{
  document.getElementById('xp-show').innerText = `⚡ ${{state.xp}} XP`;
  document.getElementById('sb-xp').innerText = `${{state.xp}} XP earned`;
  document.getElementById('streak-show').innerText = `🔥 ${{state.streak}} day streak`;
  document.getElementById('sb-streak').innerText = `${{state.streak}} day streak`;
  
  let compCount = state.completed.length;
  let pct = Math.round((compCount / 7) * 100);
  document.getElementById('prog-bar').style.width = pct + '%';
  document.getElementById('prog-text').innerText = `${{compCount}}/7 days`;
  
  document.querySelectorAll('.day-pill').forEach(p => p.classList.remove('done'));
  state.completed.forEach(d => {{
    let pill = document.getElementById('pill-' + d);
    if(pill) pill.classList.add('done');
    let btn = document.getElementById('btn-day-' + d);
    if(btn) {{
      btn.classList.add('done');
      btn.innerText = `✓ Day ${{d}} Completed`;
    }}
  }});
}}

function completeDay(day, xpAmount) {{
  if(state.completed.includes(day)) return;
  state.completed.push(day);
  state.xp += xpAmount;
  
  let today = new Date().toDateString();
  if(state.lastDate !== today) {{
    state.streak += 1;
    state.lastDate = today;
  }}
  
  saveState();
  showToast(`+${{xpAmount}} XP ⚡`);
}}

function showToast(msg) {{
  let t = document.getElementById('xp-toast');
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}}

function goDay(day) {{
  document.querySelectorAll('.day-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.day-pill').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.sb-item').forEach(i => i.classList.remove('active'));
  
  document.getElementById('day-' + day).classList.add('active');
  document.getElementById('pill-' + day).classList.add('active');
  document.getElementById('sb-' + day).classList.add('active');
  window.scrollTo(0,0);
}}

function toggleSidebar() {{
  document.getElementById('sidebar').classList.toggle('open');
}}
function closeSidebar() {{
  if(window.innerWidth <= 768) {{
    document.getElementById('sidebar').classList.remove('open');
  }}
}}

function jumpTo(id) {{
  let target = document.querySelector('.day-section.active #' + id);
  if(target) {{
    let top = target.getBoundingClientRect().top + window.scrollY - 80;
    window.scrollTo({{ top, behavior: 'smooth' }});
  }}
  closeSidebar();
}}

function copyCode(btn) {{
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {{
    navigator.clipboard.writeText(pre.innerText).then(() => {{
      btn.textContent = 'copied!';
      setTimeout(() => btn.textContent = 'copy', 1500);
    }});
  }}
}}

function toggleTask(header) {{
  let body = header.nextElementSibling;
  body.style.display = body.style.display === 'block' ? 'none' : 'block';
}}

function toggleSolution(id) {{
  let sol = document.getElementById(id);
  if(sol) {{
    sol.style.display = sol.style.display === 'block' ? 'none' : 'block';
  }}
}}

function quiz(opt, status, qid) {{
  let block = opt.parentElement;
  if(block.classList.contains('answered')) return;
  block.classList.add('answered');
  
  if(status === 'correct') {{
    opt.classList.add('correct');
    document.getElementById(qid + '-correct').style.display = 'block';
  }} else {{
    opt.classList.add('wrong');
    document.getElementById(qid + '-wrong').style.display = 'block';
  }}
}}

function openRepl() {{
  window.open("https://replit.com/languages/python3", "_blank");
}}

// Init
updateUI();
</script>
</body>
</html>
"""

    with open(week14_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("week14.html successfully generated with mathematical depth and updated days!")

if __name__ == '__main__':
    generate_week14()
