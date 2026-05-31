import re

with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Day 68 diagram replacement
print("Updating Day 68 diagram...")
day68_start = content.find('<div class="day-section" id="day-68">')
day69_start = content.find('<div class="day-section" id="day-69">')
if day68_start != -1 and day69_start != -1:
    day68_block = content[day68_start:day69_start]
    m_idx = day68_block.find('<div class="mermaid">')
    if m_idx != -1:
        m_end = day68_block.find('</div>', m_idx)
        old_m = day68_block[m_idx:m_end+6]
        new_m = """    <div class="mermaid">
      graph TD
      X[Input x_t] --> L1[LSTM Layer 1] --> L2[LSTM Layer 2] --> Out[Dense Output / Prediction]
      L1 -. hidden state .-> L1
      L2 -. hidden state .-> L2
    </div>"""
    new_day68_block = day68_block.replace(old_m, new_m)
    content = content.replace(day68_block, new_day68_block)
    print("  Day 68 diagram replaced!")

# 2. Day 69 diagram replacement
print("Updating Day 69 diagram...")
day69_start = content.find('<div class="day-section" id="day-69">')
day70_start = content.find('<div class="day-section" id="day-70">')
if day69_start != -1 and day70_start != -1:
    day69_block = content[day69_start:day70_start]
    m_idx = day69_block.find('<div class="mermaid">')
    if m_idx != -1:
        m_end = day69_block.find('</div>', m_idx)
        old_m = day69_block[m_idx:m_end+6]
        new_m = """    <div class="mermaid">
      graph LR
      X_t2["Input x(t-2)"] --> LSTM1["LSTM Cell"] --> X_t1["Input x(t-1)"] --> LSTM2["LSTM Cell"] --> X_t["Input x(t)"] --> LSTM3["LSTM Cell"] --> Output["Future Prediction y(t+1)"]
    </div>"""
    new_day69_block = day69_block.replace(old_m, new_m)
    content = content.replace(day69_block, new_day69_block)
    print("  Day 69 diagram replaced!")

# 3. Day 70 replacement (Bidirectional & Stacked LSTMs)
print("Replacing Day 70...")
day70_start = content.find('<div class="day-section" id="day-70">')
day71_start = content.find('<div class="day-section" id="day-71">')

new_day70 = """<div class="day-section" id="day-70">
  <div class="day-header">
    <div class="day-tag">WEEK 10 · DAY 70 · MONTH 3 — SEQUENCE MODELING</div>
    <h1>Bidirectional LSTMs & Stacked RNNs</h1>
    <p>
      Standard recurrent networks process sequences strictly from left to right, ignoring future context.
      Today, we master **Bidirectional RNNs** and **Stacked recurrent architectures**.
      We will study how Bidirectional LSTMs simultaneously capture past and future sequence context,
      analyze the mathematical shape transformations in stacked layers,
      and implement a multi-layer Bidirectional LSTM network in Keras.
    </p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 5 hours</span>
      <span class="meta-badge o">🧠 Intermediate</span>
      <span class="meta-badge p">⚡ +150 XP</span>
      <span class="meta-badge b">🔬 Bidirectional Math</span>
    </div>
  </div>

  <div class="objectives">
    <h3>🎯 By end of Day 70 you will be able to:</h3>
    <ul>
      <li>Explain the architecture and forward pass equations of Bidirectional RNNs.</li>
      <li>Understand stacked recurrent architectures and the role of hidden state sequences.</li>
      <li>Configure return_sequences parameters in Keras to stack multiple LSTM layers.</li>
      <li>Build and train a robust Stacked Bidirectional LSTM model for sequence prediction.</li>
    </ul>
  </div>

  <div class="mermaid">
    graph TD
    X[Input Sequence x_t] --> Fwd[Forward LSTM Layer] --> H_fwd[Forward State h_t_fwd]
    X --> Bwd[Backward LSTM Layer] --> H_bwd[Backward State h_t_bwd]
    H_fwd --> Concat["Concatenation [h_fwd, h_bwd]"]
    H_bwd --> Concat
    Concat --> Out[Output Layer / Next Stacked Layer]
  </div>
  <div class="diagram-cap">Bidirectional Recurrent Neural Network forward-backward states concatenation</div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory & Engineering Deep Dive</h2>

    <h3 class="sh3">1. Bidirectional RNNs: Using Future Context</h3>
    <p>
      In many tasks (like translation or sentiment analysis), the meaning of a word depends on both preceding and succeeding words.
      A **Bidirectional RNN** processes the input sequence in two directions:
    </p>
    <ul>
      <li><strong>Forward Recurrence:</strong> Processes the sequence from $t=1$ to $t=T$, producing hidden states $\vec{h}_t$.</li>
      <li><strong>Backward Recurrence:</strong> Processes the sequence from $t=T$ to $t=1$, producing hidden states $\overleftarrow{h}_t$.</li>
    </ul>
    <p>
      At each step $t$, the output is formed by concatenating or summing the forward and backward hidden states:
      $$h_t = [\vec{h}_t; \overleftarrow{h}_t]$$
      This doubles the hidden state dimension (e.g., if hidden units = 64, the bidirectional output shape at step $t$ is 128).
    </p>

    <h3 class="sh3">2. Stacked Recurrent Networks</h3>
    <p>
      To learn higher-level temporal representations, we can stack recurrent layers on top of each other.
      The hidden states output by layer $l$ serve as the sequence input for layer $l+1$.
    </p>
    <p>
      In Keras, recurrent layers by default only return the hidden state of the **last step** (shape: <code>(batch, units)</code>).
      To stack them, the lower layer must output the hidden states of **all steps** (shape: <code>(batch, timesteps, units)</code>).
      We enable this by setting <code>return_sequences=True</code>.
    </p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — stacked_bilstm.py</span><div class="cb-btns"><button class="run-btn" onclick="openRepl()">▶ try online</button><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">from</span> keras.models <span class="kw">import</span> Sequential
<span class="kw">from</span> keras.layers <span class="kw">import</span> Embedding, Bidirectional, LSTM, Dense

model = Sequential([
    <span class="cm"># Embedding Layer maps token indices to 64-dim dense vectors</span>
    Embedding(input_dim=<span class="num">1000</span>, output_dim=<span class="num">64</span>),
    
    <span class="cm"># First layer: Stacked Bidirectional LSTM (returns sequence)</span>
    Bidirectional(LSTM(<span class="num">64</span>, return_sequences=<span class="kw">True</span>)),
    
    <span class="cm"># Second layer: Final Bidirectional LSTM (returns last step hidden state)</span>
    Bidirectional(LSTM(<span class="num">32</span>, return_sequences=<span class="kw">False</span>)),
    
    <span class="cm"># Classification head</span>
    Dense(<span class="num">1</span>, activation=<span class="str">'sigmoid'</span>)
])

model.compile(optimizer=<span class="str">'adam'</span>, loss=<span class="str">'binary_crossentropy'</span>, metrics=[<span class="str">'accuracy'</span>])
model.summary()</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check — Day 70 Quiz</h2>
    <div class="q-box">
      <p><strong>Question 1:</strong> If a Bidirectional LSTM layer has 64 units (dimensionality of output space), what is the shape of its output tensor at each timestep (excluding batch dimension)?</p>
      <button class="opt-btn" onclick="showFeedback(this, false, 'q70-1')">64</button>
      <button class="opt-btn" onclick="showFeedback(this, true, 'q70-1')">128 (concatenated 64-dim forward and 64-dim backward states)</button>
      <button class="opt-btn" onclick="showFeedback(this, false, 'q70-1')">32</button>
      <div class="feedback" id="q70-1-correct">Correct! Bidirectional concatenation merges forward and backward hidden states, doubling the output units.</div>
      <div class="feedback" id="q70-1-wrong">Incorrect. Review the concatenation math of bidirectional layers.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Coding Tasks</h2>
    <div class="task-block">
      <div class="task-header" onclick="toggleTask(this)">
        <span class="chk-box" onclick="event.stopPropagation(); toggleCheck(this)"></span>
        <span>Task 1: Build Stacked Bidirectional Classifier</span>
      </div>
      <div class="task-body">
        <p>Implement a Keras text classifier using Stacked Bidirectional LSTM layers. Fine-tune it on a dummy IMDB reviews dataset and inspect the model summary to trace tensor dimensions.</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://keras.io/guides/working_with_rnns/" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">Working with RNNs — Keras Guide</div>
        <div class="rc-sub">The official Keras RNN guide covering stacking and bidirectional setups</div>
      </a>
      <a class="resource-card" href="https://colah.github.io/posts/2015-08-Understanding-LSTMs/" target="_blank">
        <div class="rc-type">📝 ARTICLE</div>
        <div class="rc-title">Understanding LSTMs — Colah's Blog</div>
        <div class="rc-sub">The classic illustrated blog post covering LSTM architecture</div>
      </a>
    </div>
  </div>
  
  <button class="complete-btn" id="btn-day-70" onclick="completeDay(70, 150)">✅ Mark Day 70 Complete — Claim 150 XP</button>
</div>"""

if day70_start != -1 and day71_start != -1:
    content = content.replace(content[day70_start:day71_start], new_day70)
    print("Day 70 replaced in week10.html!")

# 4. Day 72 replacement (Seq2Seq Model Capstone)
print("Replacing Day 72...")
# Find the indices again since the content changed
day72_start = content.find('<div class="day-section" id="day-72">')
day_toolkit_start = content.find('<div class="day-section" id="day-toolkit">')

new_day72 = """<div class="day-section" id="day-72">
  <div class="day-header">
    <div class="day-tag">WEEK 10 · DAY 72 · MONTH 3 — SEQUENCE MODELING</div>
    <h1>Capstone Project: Sequence-to-Sequence (Seq2Seq) Model</h1>
    <p>
      Mapping input sequences to output sequences of different lengths (like translation or spelling correction) requires specialized encoder-decoder architectures.
      Today, we build our Week 10 Capstone: a character-level **Sequence-to-Sequence (Seq2Seq)** model.
      We will analyze the Encoder-Decoder framework, implement **Teacher Forcing** during decoder training,
      and write custom inference logic to decode target output sequences step-by-step.
    </p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge o">🧠 Advanced</span>
      <span class="meta-badge p">⚡ +300 XP</span>
      <span class="meta-badge b">💻 Seq2Seq Capstone</span>
    </div>
  </div>

  <div class="objectives">
    <h3>🎯 By end of Day 72 you will be able to:</h3>
    <ul>
      <li>Explain the mathematical mapping of Encoder-Decoder sequence architectures.</li>
      <li>Configure Keras functional API models with recurrent state passing.</li>
      <li>Implement Teacher Forcing decoder inputs for training sequence models.</li>
      <li>Write custom autoregressive decoding loops for inference sequence generations.</li>
    </ul>
  </div>

  <div class="mermaid">
    graph LR
    subgraph Encoder [Encoder Network]
    Input[Input Tokens] --> EncLSTM[Encoder LSTM] --> Context[Context Vector / Final States]
    end
    subgraph Decoder [Decoder Network]
    Context --> DecLSTM[Decoder LSTM] --> Output[Output Tokens]
    DecLSTM -. Feed previous output .-> DecLSTM
    end
  </div>
  <div class="diagram-cap">Recurrent Sequence-to-Sequence (Seq2Seq) Encoder-Decoder architecture</div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory & Engineering Deep Dive</h2>

    <h3 class="sh3">1. The Encoder-Decoder Framework</h3>
    <p>
      In Seq2Seq architectures, we separate the network into two parts:
    </p>
    <ul>
      <li><strong>Encoder:</strong> Processes the input sequence token by token. Its final hidden and cell states represent a compressed <em>Context Vector</em> of the input.</li>
      <li><strong>Decoder:</strong> Initialized with the Encoder's final states. It generates the output sequence step-by-step.</li>
    </ul>

    <h3 class="sh3">2. Teacher Forcing during Training</h3>
    <p>
      At step $t$ during training, instead of feeding the decoder's own predicted token from step $t-1$ as input (which could lead to slow convergence), we feed the **actual target token** from the ground-truth sequence. This is called **Teacher Forcing**.
    </p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — character_seq2seq.py</span><div class="cb-btns"><button class="run-btn" onclick="openRepl()">▶ try online</button><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">from</span> keras.models <span class="kw">import</span> Model
<span class="kw">from</span> keras.layers <span class="kw">import</span> Input, LSTM, Dense

latent_dim = <span class="num">256</span>

<span class="cm"># --- Encoder Setup ---</span>
encoder_inputs = Input(shape=(<span class="kw">None</span>, num_encoder_tokens))
encoder_lstm = LSTM(latent_dim, return_state=<span class="kw">True</span>)
_, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c] # Context vector states

<span class="cm"># --- Decoder Setup (Training) ---</span>
decoder_inputs = Input(shape=(<span class="kw">None</span>, num_decoder_tokens))
decoder_lstm = LSTM(latent_dim, return_sequences=<span class="kw">True</span>, return_state=<span class="kw">True</span>)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation=<span class="str">'softmax'</span>)
decoder_outputs = decoder_dense(decoder_outputs)

<span class="cm"># --- Seq2Seq Model ---</span>
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer=<span class="str">'rmsprop'</span>, loss=<span class="str">'categorical_crossentropy'</span>)</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check — Day 72 Quiz</h2>
    <div class="q-box">
      <p><strong>Question 1:</strong> What is Teacher Forcing during Seq2Seq training?</p>
      <button class="opt-btn" onclick="showFeedback(this, false, 'q72-1')">Letting the model predict without correct output reference</button>
      <button class="opt-btn" onclick="showFeedback(this, true, 'q72-1')">Feeding ground-truth target tokens as input to the decoder at step t</button>
      <button class="opt-btn" onclick="showFeedback(this, false, 'q72-1')">Forcing gradients to scale up</button>
      <div class="feedback" id="q72-1-correct">Correct! Teacher forcing speeds up training by using target ground truths rather than decoder outputs.</div>
      <div class="feedback" id="q72-1-wrong">Incorrect. Review teacher forcing concepts in recurrent decoders.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Coding Tasks</h2>
    <div class="task-block">
      <div class="task-header" onclick="toggleTask(this)">
        <span class="chk-box" onclick="event.stopPropagation(); toggleCheck(this)"></span>
        <span>Task 1: Build Character-Level Seq2Seq Reversal Model</span>
      </div>
      <div class="task-body">
        <p>Implement the character-level sequence-to-sequence model in Python. Train it to reverse short character strings (e.g. "hello" &rarr; "olleh") and verify the decoding output at inference.</p>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://tensorflow.org/tutorials/text/nmt_with_attention" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">TF Translation Tutorial</div>
        <div class="rc-sub">Encoder-Decoder Seq2Seq translation pipeline walkthrough</div>
      </a>
      <a class="resource-card" href="https://keras.io/examples/nlp/lstm_seq2seq/" target="_blank">
        <div class="rc-type">💻 PRACTICE</div>
        <div class="rc-title">Keras Seq2Seq character-level translation</div>
        <div class="rc-sub">Full character-level translation implementation code guide</div>
      </a>
    </div>
  </div>
  
  <button class="complete-btn" id="btn-day-72" onclick="completeDay(72, 300)">✅ Mark Day 72 Complete — Claim 300 XP</button>
</div>"""

if day72_start != -1 and day_toolkit_start != -1:
    content = content.replace(content[day72_start:day_toolkit_start], new_day72)
    print("Day 72 replaced in week10.html!")

# 5. Toolkit section replacement (RNN Graduate Resources)
print("Replacing Toolkit Section...")
day_toolkit_start = content.find('<div class="day-section" id="day-toolkit">')
# The toolkit section is the last day-section in week10.html, so it ends before the script tag
script_tag_start = content.find('<script>', day_toolkit_start)

new_toolkit = """<div class="day-section" id="day-toolkit">
  <div class="day-header">
    <div class="day-tag">WEEK 10 · TOOLKIT · MONTH 3 — RNNs & SEQUENTIAL DATA</div>
    <h1>RNN & Sequential Master Resource Kit</h1>
    <p>Welcome to the ultimate repository of advanced Recurrent Neural Network engineering resources. This dedicated module compiles the core mathematical formulations, BPTT vanishing gradient proofs, and a sequence execution timing benchmark utility to prepare you for senior ML research and deep sequence engineering positions.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ Reference</span>
      <span class="meta-badge o">🧠 Senior Master</span>
      <span class="meta-badge p">⚡ Specialized</span>
      <span class="meta-badge b">🔬 Recurrent Mathematics</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🔬 Graduate Mathematics & Derivations</h2>

    <h3 class="sh3">1. Vanishing Gradient in Recurrent Networks</h3>
    <p>
      Consider a SimpleRNN with state update:
      $$h_t = \\tanh(W_{hh} h_{t-1} + W_{xh} x_t + b)$$
      The loss gradient at step $T$ with respect to parameters $W_{hh}$ is calculated using Backpropagation Through Time (BPTT):
      $$\\frac{\\partial L}{\\partial W_{hh}} = \\sum_{t=1}^T \\frac{\\partial L}{\\partial h_T} \\frac{\\partial h_T}{\\partial h_t} \\frac{\\partial h_t}{\\partial W_{hh}}$$
      The term $\\frac{\\partial h_T}{\\partial h_t}$ is a product of Jacobian matrices:
      $$\\frac{\\partial h_T}{\\partial h_t} = \\prod_{k=t+1}^T \\frac{\\partial h_k}{\\partial h_{k-1}} = \\prod_{k=t+1}^T diag(1 - h_k^2) W_{hh}^T$$
      If the eigenvalues of $W_{hh}$ are less than 1, or if the activations saturate ($h_k \\approx \\pm 1$ making $1 - h_k^2 \\approx 0$), this product vanishes exponentially as $T-t$ grows, meaning the model cannot learn long-term dependencies.
    </p>

    <h3 class="sh3">2. LSTM Cell State Gradients</h3>
    <p>
      In LSTMs, the cell state update is:
      $$c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t$$
      Computing the gradient of cell state $c_t$ with respect to $c_{t-1}$ yields:
      $$\\frac{\\partial c_t}{\\partial c_{t-1}} = f_t$$
      If the forget gate $f_t \\approx 1$, the gradient propagates back indefinitely through time without exponential decay, solving the vanishing gradient problem.
    </p>

    <h3 class="sh3">3. Sequence Processing Speed & Latency Profiler</h3>
    <p>
      Below is a utility to benchmark processing speeds of SimpleRNN, GRU, and LSTM layers on synthetic sequences.
    </p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — rnn_benchmark.py</span><div class="cb-btns"><button class="run-btn" onclick="openRepl()">▶ try online</button><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> time
<span class="kw">import</span> numpy <span class="kw">as</span> np
<span class="kw">import</span> tensorflow <span class="kw">as</span> tf
<span class="kw">from</span> tensorflow.keras.layers <span class="kw">import</span> SimpleRNN, GRU, LSTM

X = np.random.randn(<span class="num">1000</span>, <span class="num">100</span>, <span class="num">64</span>).astype(np.float32)

<span class="kw">for</span> layer_class, name <span class="kw">in</span> [(SimpleRNN, <span class="str">'SimpleRNN'</span>), (GRU, <span class="str">'GRU'</span>), (LSTM, <span class="str">'LSTM'</span>)]:
    layer = layer_class(<span class="num">128</span>)
    <span class="cm"># Warm-up</span>
    _ = layer(X[:<span class="num">10</span>])
    
    t0 = time.time()
    _ = layer(X)
    t1 = time.time()
    
    <span class="bi">print</span>(f"{name} latency: {(t1 - t0)*1000:.2f} ms")</pre>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Senior Technical Interview Catalog</h2>
    <div class="task-block">
      <div class="task-header" onclick="toggleTask(this)">
        <span>Q1: Why does LSTM use addition in the cell state update rather than multiplication?</span>
      </div>
      <div class="task-body">
        <p>Adding the inputs allows the gradient to flow directly back through time without multiplication by weights, preventing exponential decay or explosion.</p>
      </div>
    </div>
    <div class="task-block">
      <div class="task-header" onclick="toggleTask(this)">
        <span>Q2: Contrast GRU and LSTM parameters and gate counts.</span>
      </div>
      <div class="task-body">
        <p>GRUs have 3 gates (Reset, Update, Candidate) while LSTMs have 4 gates (Input, Forget, Cell, Output). GRUs combine cell and hidden states, resulting in 25% fewer parameters and faster execution.</p>
      </div>
    </div>
  </div>
</div>"""

if day_toolkit_start != -1 and script_tag_start != -1:
    content = content.replace(content[day_toolkit_start:script_tag_start], new_toolkit)
    print("Toolkit replaced in week10.html!")

# 6. Replace r2rt.com card
print("Replacing r2rt.com link...")
old_r2rt = """  <a class="resource-card" href="http://r2rt.com/recurrent-neural-networks-in-tensorflow-i.html" target="_blank">
    <div class="rc-type">🌐 WEBSITE</div>
    <div class="rc-title">RNN Visual Guide — r2rt</div>
    <div class="rc-sub">Excellent step-by-step unrolling math & code</div>
  </a>"""

new_r2rt = """  <a class="resource-card" href="https://keras.io/guides/working_with_rnns/" target="_blank">
    <div class="rc-type">📖 OFFICIAL</div>
    <div class="rc-title">Working with RNNs — Keras Guide</div>
    <div class="rc-sub">The modern Keras RNN API walkthrough for LSTMs and GRUs</div>
  </a>"""
content = content.replace(old_r2rt, new_r2rt)

# 7. Add prerequisite to 2604.pdf
print("Updating LSTM paper description...")
old_lstm_paper = """  <a class="resource-card" href="https://www.bioinf.jku.at/publications/older/2604.pdf" target="_blank">
    <div class="rc-type">📖 OFFICIAL</div>
    <div class="rc-title">LSTM Paper — Hochreiter & Schmidhuber (1997)</div>
    <div class="rc-sub">The original LSTM paper that started it all</div>
  </a>"""

new_lstm_paper = """  <a class="resource-card" href="https://www.bioinf.jku.at/publications/older/2604.pdf" target="_blank">
    <div class="rc-type">📖 OFFICIAL</div>
    <div class="rc-title">LSTM Paper — Hochreiter & Schmidhuber (1997)</div>
    <div class="rc-sub">The original LSTM paper. (Prerequisite: Read Colah's blog post first!)</div>
  </a>"""
content = content.replace(old_lstm_paper, new_lstm_paper)

with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week10.html")
