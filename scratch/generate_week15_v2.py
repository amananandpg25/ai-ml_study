import re
import os

def generate_week15():
    week13_path = '/Users/amananand/Downloads/SDE/ai:ml/week13.html'
    week15_path = '/Users/amananand/Downloads/SDE/ai:ml/week15.html'
    
    with open(week13_path, 'r', encoding='utf-8') as f:
        week13_content = f.read()
        
    style_match = re.search(r'<style>(.*?)</style>', week13_content, re.DOTALL)
    if not style_match:
        print("CSS style block not found in week13.html!")
        return
    css_content = style_match.group(1)
    
    css_content = css_content.replace('--accent:var(--purple);', '--accent:var(--purple);')
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Week 15 — LLM Engineering & Agentic Systems | 135-Day AI/ML Roadmap</title>
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
    <div class="brand">Week 15 — LLM Engineering & Agents</div>
    <div class="xp-display" id="xp-show">⚡ 0 XP</div>
    <div class="streak-display" id="streak-show">🔥 0 day streak</div>
  </div>
  <div style="display:flex;align-items:center;gap:.8rem">
    <div class="prog-wrap">
      <div class="prog-outer"><div class="prog-inner" id="prog-bar"></div></div>
      <span id="prog-text">0/7 days</span>
    </div>
    <div class="day-pills">
      <div class="day-pill active" onclick="goDay(101)" id="pill-101">101</div>
      <div class="day-pill" onclick="goDay(102)" id="pill-102">102</div>
      <div class="day-pill" onclick="goDay(103)" id="pill-103">103</div>
      <div class="day-pill" onclick="goDay(104)" id="pill-104">104</div>
      <div class="day-pill" onclick="goDay(105)" id="pill-105">105</div>
      <div class="day-pill" onclick="goDay(106)" id="pill-106">106</div>
      <div class="day-pill" onclick="goDay(107)" id="pill-107">107</div>
    </div>
  </div>
</nav>

<div class="layout">

<aside class="sidebar" id="sidebar">
  <div class="sb-label">Week 15 — Days</div>
  <div class="sb-item active" onclick="goDay(101);closeSidebar()" id="sb-101"><span class="sb-dot" style="background:var(--purple)"></span>Day 101 — LLM Fundamentals</div>
  <div class="sb-item" onclick="goDay(102);closeSidebar()" id="sb-102"><span class="sb-dot" style="background:var(--pink)"></span>Day 102 — Prompt Engineering</div>
  <div class="sb-item" onclick="goDay(103);closeSidebar()" id="sb-103"><span class="sb-dot" style="background:var(--orange)"></span>Day 103 — LangChain & LCEL</div>
  <div class="sb-item" onclick="goDay(104);closeSidebar()" id="sb-104"><span class="sb-dot" style="background:var(--green)"></span>Day 104 — LLM APIs & Tool Use</div>
  <div class="sb-item" onclick="goDay(105);closeSidebar()" id="sb-105"><span class="sb-dot" style="background:var(--blue)"></span>Day 105 — Advanced RAG</div>
  <div class="sb-item" onclick="goDay(106);closeSidebar()" id="sb-106"><span class="sb-dot" style="background:var(--pink)"></span>Day 106 — LLM Agents</div>
  <div class="sb-item" onclick="goDay(107);closeSidebar()" id="sb-107"><span class="sb-dot" style="background:var(--yellow)"></span>Day 107 — Agentic Capstone</div>
  <div class="sb-divider"></div>
  <div class="sb-label">Progress</div>
  <div class="sb-item"><span class="sb-dot" style="background:var(--orange)"></span><span id="sb-xp">0 XP earned</span></div>
  <div class="sb-item"><span class="sb-dot" style="background:var(--pink)"></span><span id="sb-streak">0 day streak</span></div>
  <div class="sb-divider"></div>
  <div class="sb-label">Quick Jump</div>
  <div class="sb-item" onclick="jumpTo('theory')"><span class="sb-dot" style="background:var(--purple)"></span>Theory</div>
  <div class="sb-item" onclick="jumpTo('tasks-section')"><span class="sb-dot" style="background:var(--orange)"></span>Tasks</div>
  <div class="sb-item" onclick="jumpTo('quiz-section')"><span class="sb-dot" style="background:var(--blue)"></span>Quiz</div>
  <div class="sb-item" onclick="jumpTo('resources-section')"><span class="sb-dot" style="background:var(--green)"></span>Resources</div>
</aside>

<main class="main">

<!-- ═══════════════════════════════════════
     DAY 101
     ════════════════════════════════════════ -->
<div class="day-section active" id="day-101">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 101 · MONTH 5 — LLM ENGINEERING</div>
    <h1>LLM Fundamentals — How GPT Works</h1>
    <p>Understanding the inner mechanics of Large Language Models. We study the decoder-only architecture, autoregressive generation, logits sampling, and the alignment process (RLHF & DPO).</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
      <span class="meta-badge t">LLM Foundations</span>
    </div>
  </div>

  <div class="objectives">
    <h3>🎯 Objectives:</h3>
    <ul>
      <li>Explain the difference between encoder-only, decoder-only, and encoder-decoder architectures.</li>
      <li>Understand next-token prediction and next-token probability distributions.</li>
      <li>Formulate temperature scaling, top-k, and top-p sampling.</li>
      <li>Explain the alignment process: Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF).</li>
    </ul>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Decoder-only Transformers</h3>
    <p>Unlike BERT (encoder-only) or T5 (encoder-decoder), modern LLMs like GPT-4, LLaMA, and Claude are **decoder-only** transformers. They take a sequence of tokens and process them causal-masked, outputting a probability distribution for the *next* token over the vocabulary. Generating a paragraph is done autoregressively: predicting one word, appending it to the input, and passing it back into the model.</p>
    
    <h3 class="sh3">2. Logits Sampling Math</h3>
    <p>The model outputs raw scores (logits) $z_i$ for each word in the vocabulary. We convert these to probabilities using Softmax. To control creativity and diversity, we modify this distribution:</p>
    <ul>
      <li><strong>Temperature (T):</strong> Scales the logits before Softmax: $P(x_i) = \frac{\exp(z_i / T)}{\sum \exp(z_j / T)}$. Setting $T \to 0$ makes the model greedy and deterministic. Setting $T > 1.0$ flattens the distribution, leading to high creativity (and hallucinations).</li>
      <li><strong>Top-K:</strong> Truncates the vocabulary to only the top $K$ most likely tokens.</li>
      <li><strong>Top-P (Nucleus Sampling):</strong> Truncates the vocabulary to the smallest set of tokens whose cumulative probability exceeds threshold $P$ (e.g., $P=0.9$).</li>
    </ul>

    <h3 class="sh3">3. RLHF & DPO Alignment</h3>
    <p>Raw pre-trained models are next-token predictors and often output gibberish prompts or unsafe completions. Aligning models to follow instructions safely involves:</p>
    <ol>
      <li><strong>SFT (Supervised Fine-Tuning):</strong> Fine-tuning on high-quality instruction-following transcripts.</li>
      <li><strong>RLHF:</strong> Training a Reward Model on human preference choices, then updating the policy via PPO reinforcement learning.</li>
      <li><strong>DPO (Direct Preference Optimization):</strong> Bypassing the reward model by directly updating the model weights using binary cross-entropy on human preference pairs.</li>
    </ol>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — sampling.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> torch
<span class="kw">import</span> torch.nn.functional <span class="kw">as</span> F

<span class="kw">def</span> <span class="fn">sample_with_temperature</span>(logits, temperature=0.7):
    <span class="cm"># logits shape: [vocab_size]</span>
    <span class="kw">if</span> temperature == 0:
        return torch.argmax(logits)
    scaled_logits = logits / temperature
    probs = F.softmax(scaled_logits, dim=-1)
    return torch.multinomial(probs, num_samples=1)[0]</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">QUESTION 1</div>
      <div class="quiz-q">How does decreasing the Temperature parameter to 0.1 affect LLM outputs?</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q101-1')"><span class="quiz-letter">A</span> It concentrates probability on the most likely tokens, making responses highly deterministic.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q101-1')"><span class="quiz-letter">B</span> It flattens the probability distribution, making outputs random and diverse.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q101-1')"><span class="quiz-letter">C</span> It increases the model's context window.</div>
      <div class="quiz-feedback correct-fb" id="q101-1-correct">✅ Correct! Lower temperature scales down the logits variance, making the highest logit exponentially dominant.</div>
      <div class="quiz-feedback wrong-fb" id="q101-1-wrong">❌ Incorrect. High temperature flattens distributions; low temperature sharpens them.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.06)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Implement Top-P (Nucleus) Sampling</span>
        <span class="task-time">⏱ 60 min</span>
      </div>
      <div class="task-body">
        <p>Implement a PyTorch function <code>top_p_sampling(logits, p=0.9)</code>. It must sort the logits in descending order, calculate cumulative probabilities, and zero-out any logit whose cumulative probability is outside the threshold.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d101t1')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d101t1">
          <pre><span class="kw">import</span> torch
<span class="kw">import</span> torch.nn.functional <span class="kw">as</span> F

<span class="kw">def</span> <span class="fn">top_p_sampling</span>(logits, p=0.9):
    sorted_logits, sorted_indices = torch.sort(logits, descending=<span class="bi">True</span>)
    cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
    
    # Remove tokens with cumulative probability above threshold
    sorted_indices_to_remove = cumulative_probs > p
    # Shift to keep the first token that crosses threshold
    sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
    sorted_indices_to_remove[..., 0] = 0
    
    indices_to_remove = sorted_indices[sorted_indices_to_remove]
    logits[indices_to_remove] = float('-inf')
    return logits</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://arxiv.org/abs/2005.14165" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">Language Models are Few-Shot Learners (GPT-3)</div>
        <div class="rc-sub">Brown et al. (2020)</div>
      </a>
      <a class="resource-card" href="https://huggingface.co/blog/rlhf" target="_blank">
        <div class="rc-type">📝 ARTICLE</div>
        <div class="rc-title">Illustrating Reinforcement Learning from Human Feedback (RLHF)</div>
        <div class="rc-sub">Hugging Face blog conceptual walkthrough.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-101" onclick="completeDay(101, 150)">✓ Mark Day 101 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 102
     ════════════════════════════════════════ -->
<div class="day-section" id="day-102">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 102 · MONTH 5 — LLM ENGINEERING</div>
    <h1>Prompt Engineering & ChatML Format</h1>
    <p>Mastering prompt templates, instruction formatting, few-shot conditioning, Chain-of-Thought (CoT) reasoning, and the ChatML markup structure.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. ChatML (Chat Markup Language)</h3>
    <p>Modern LLMs are fine-tuned on multi-turn conversations using specific boundary tags. The most common standard is ChatML, which segments text into explicit system, user, and assistant blocks using special tokens like <code>&lt;|im_start|&gt;</code> and <code>&lt;|im_end|&gt;</code>:</p>
    <pre>
&lt;|im_start|&gt;system
You are a helpful math tutor.&lt;|im_end|&gt;
&lt;|im_start|&gt;user
What is 2+2?&lt;|im_end|&gt;
&lt;|im_start|&gt;assistant
4.&lt;|im_end|&gt;
    </pre>

    <h3 class="sh3">2. Prompting paradigms</h3>
    <ul>
      <li><strong>Zero-Shot:</strong> Direct instruction without examples.</li>
      <li><strong>Few-Shot:</strong> Providing 3-5 structural examples inside the prompt to align formatting and target behavior.</li>
      <li><strong>Chain-of-Thought (CoT):</strong> Adding `Let's think step by step` to force the model to compute intermediate reasoning steps, decreasing logic errors.</li>
    </ul>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">What is the main role of the 'system' prompt in ChatML formatting?</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q102-1')"><span class="quiz-letter">A</span> Enforcing global behavior, safety guidelines, and persona constraints across the conversation.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q102-1')"><span class="quiz-letter">B</span> Loading document embeddings.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q102-1')"><span class="quiz-letter">C</span> Training the model's weights.</div>
      <div class="quiz-feedback correct-fb" id="q102-1-correct">✅ Correct! System prompts establish the guardrails and style guidelines.</div>
      <div class="quiz-feedback wrong-fb" id="q102-1-wrong">❌ Incorrect. System prompt dictates model rules and behavior patterns.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Tasks</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(247,169,75,.05);border-left:3px solid var(--orange)" onclick="toggleTask(this)">
        <span class="task-badge tb-med">🟡 MEDIUM</span>
        <span class="task-title">Design Few-Shot JSON Extraction Prompt</span>
        <span class="task-time">⏱ 30 min</span>
      </div>
      <div class="task-body">
        <p>Write a system prompt and a few-shot user prompt that extracts Entity, Category, and Sentiment from a text string and returns a raw, parseable JSON dictionary. Include 2 examples.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d102t1')">👁 Show Prompt Design</button>
        <div class="solution-box" id="sol-d102t1">
          <pre>System: You extract entities, categories, and sentiments in JSON.
User: Text: "Tesla stock soared today"
Assistant: {{"entity": "Tesla", "category": "finance", "sentiment": "positive"}}
User: Text: "My laptop battery died in 10 mins"
Assistant: {{"entity": "laptop battery", "category": "hardware", "sentiment": "negative"}}</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/" target="_blank">
        <div class="rc-type">🌐 COURSE</div>
        <div class="rc-title">ChatGPT Prompt Engineering for Developers — DeepLearning.AI</div>
        <div class="rc-sub">The classic short course detailing standard prompting guidelines and patterns.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-102" onclick="completeDay(102, 150)">✓ Mark Day 102 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 103
     ════════════════════════════════════════ -->
<div class="day-section" id="day-103">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 103 · MONTH 5 — LLM ENGINEERING</div>
    <h1>LangChain & LCEL (LangChain Expression Language)</h1>
    <p>Exploring LLM application frameworks. We learn how to build modular chains, construct PromptTemplates, parse outputs, and chain them cleanly using LCEL.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Orchestration Frameworks</h3>
    <p>Building complex AI systems requires combining prompting, APIs, databases, and custom Python functions. Frameworks like LangChain orchestrate this complexity, making components reusable.</p>

    <h3 class="sh3">2. LCEL (LangChain Expression Language)</h3>
    <p>LCEL is a declarative language to compose chains. It uses the Python pipe operator <code>|</code> to chain inputs and outputs together, supporting async streams and parallel executions natively:</p>
    <div class="math-block">
      <span class="formula">Chain = PromptTemplate | LLM | OutputParser</span>
    </div>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — lcel_chain.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">from</span> langchain_core.prompts <span class="kw">import</span> ChatPromptTemplate
<span class="kw">from</span> langchain_core.output_parsers <span class="kw">import</span> StrOutputParser
<span class="kw">from</span> langchain_community.chat_models <span class="kw">import</span> ChatOpenAI

prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

# LCEL composition
chain = prompt | model | parser
# response = chain.invoke({{"topic": "artificial intelligence"}})</pre>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://python.langchain.com/docs/introduction/" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">LangChain Introduction Documentation</div>
        <div class="rc-sub">Official LangChain v0.3 documentation landing page.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-103" onclick="completeDay(103, 150)">✓ Mark Day 103 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 104
     ════════════════════════════════════════ -->
<div class="day-section" id="day-104">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 104 · MONTH 5 — LLM ENGINEERING</div>
    <h1>LLM APIs: Function Calling, Tool Use & Streaming</h1>
    <p>Deep dive into production LLM serving. We explore function binding schemas, structured output parsing, streaming chunked responses, and asynchronous API architectures.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
      <span class="meta-badge t">Tool Binding API</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Function Calling & Tool Use</h3>
    <p>LLMs cannot fetch live data or interact with databases natively. **Function Calling** allows developers to describe local Python functions to the model using a JSON Schema (names, parameter types, descriptions). The model does *not* execute the function; instead, it outputs a JSON string containing the arguments to call. The developer parses this, runs the function locally, and returns the result to the model.</p>
    
    <div class="mermaid">
      graph TD
      User["User Query"] --> Model["Model + Tool Schema"]
      Model -->|"Decides to call tool"| ToolCall["JSON: functionName, arguments"]
      ToolCall -->|"Developer parses & executes"| Exec["Run local function / API"]
      Exec -->|"Return results"| ToolResp["Tool Observation Response"]
      ToolResp --> Model2["Model final response synthesis"]
      Model2 --> Final["User Output"]
    </div>
    <div class="diagram-cap">Function Calling multi-turn coordination loop</div>

    <h3 class="sh3">2. Streaming Tokens (Server-Sent Events)</h3>
    <p>API responses can take seconds to complete. **Streaming** returns tokens chunk-by-chunk using SSE protocols, letting UIs render text instantly and reducing perceived latency.</p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — tool_call.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> json

# JSON Schema mapping calculator tool
calculator_tool = {{
    "type": "function",
    "function": {{
        "name": "calculate",
        "description": "Performs basic math arithmetic",
        "parameters": {{
            "type": "object",
            "properties": {{
                "expression": {{"type": "string", "description": "Math expression, e.g. 2 + 2"}}
            }},
            "required": ["expression"]
        }}
    }}
}}</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">Does an LLM execute the function itself during a function call?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q104-1')"><span class="quiz-letter">A</span> Yes, the model runs the python code inside its sandboxed context.</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q104-1')"><span class="quiz-letter">B</span> No, the model only outputs the structured parameters to call; the client application executes the tool.</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q104-1')"><span class="quiz-letter">C</span> Yes, but only if the function is hosted on the cloud.</div>
      <div class="quiz-feedback correct-fb" id="q104-1-correct">✅ Correct! Function calling is purely coordinator generation. The developer is responsible for executing the code.</div>
      <div class="quiz-feedback wrong-fb" id="q104-1-wrong">❌ Incorrect. Think about the isolation of the model API from your local machine.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Tasks</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Build a Tool Calling Execution Loop</span>
        <span class="task-time">⏱ 90 min</span>
      </div>
      <div class="task-body">
        <p>Write a mock client application that:
        <br>1. Receives a tool-call request from the model.
        <br>2. Dispatches it to a local calculator dictionary matching function name to function reference.
        <br>3. Executes the calculator tool safely and prints the resulting JSON message back.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d104t1')">👁 Show Solution</button>
        <div class="solution-box" id="sol-d104t1">
          <pre><span class="kw">def</span> <span class="fn">calculate</span>(expression):
    try:
        return str(eval(expression, {{"__builtins__": None}}, {{}}))
    except Exception as e:
        return f"Error: {e}"

tool_registry = {{"calculate": calculate}}

# Mock response from LLM
tool_calls = [
    {{"name": "calculate", "args": {{"expression": "4 * 5"}}}}
]

# Client execution loop
for call in tool_calls:
    func = tool_registry[call["name"]]
    result = func(**call["args"])
    print(f"Result returned to model: {result}")</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/" target="_blank">
        <div class="rc-type">🌐 COURSE</div>
        <div class="rc-title">Functions, Tools, and Agents with LangChain — DeepLearning.AI</div>
        <div class="rc-sub">Deep dive into API function calling and building agents in production.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-104" onclick="completeDay(104, 150)">✓ Mark Day 104 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 105
     ════════════════════════════════════════ -->
<div class="day-section" id="day-105">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 105 · MONTH 5 — LLM ENGINEERING</div>
    <h1>Advanced RAG — Query Translation & Re-ranking</h1>
    <p>Solving naive RAG limits. We explore query rewrite/expansion techniques, cross-encoder re-ranking algorithms, and semantic hybrid search structures.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. Naive RAG Limitations</h3>
    <p>Naive retrieval often misses context because the user's query is short or phrased poorly, resulting in low vector match overlap. Additionally, retrieving 10 large chunks can clutter the LLM context window with irrelevant information.</p>

    <h3 class="sh3">2. Query Expansion & Translation</h3>
    <p>Before querying the database, we pass the question into an LLM, asking it to generate 3 different formulations of the same search intent. We run vector searches for all 4 queries, merging and deduplicating the results. This increases the chance of matching the target information.</p>

    <h3 class="sh3">3. Cross-Encoder Re-ranking</h3>
    <p>Bi-Encoders (Sentence-Transformers) embed queries and documents separately, allowing fast index search. However, they do not capture the token-level interaction between the query and the documents.</p>
    <p>To fix this, we retrieve a larger list of candidates (e.g., Top 50) using the fast Bi-Encoder. We then pass these 50 candidates through a **Cross-Encoder Re-ranker** (which processes the query and document together to compute relevance scores). We take the top 3 outputs to feed into the final prompt, maximizing precision.</p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — rerank.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">from</span> sentence_transformers <span class="kw">import</span> CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
query = "What is reinforcement learning?"
candidates = [
    "Reinforcement learning is learning by interacting with environment.",
    "BERT is trained on Masked Language Modeling.",
    "Supervised learning trains on labeled data pairs."
]

# Predict compatibility scores
pairs = [[query, doc] for doc in candidates]
scores = reranker.predict(pairs)
# print(scores)</pre>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-105" onclick="completeDay(105, 150)">✓ Mark Day 105 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 106
     ════════════════════════════════════════ -->
<div class="day-section" id="day-106">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 106 · MONTH 5 — LLM ENGINEERING</div>
    <h1>LLM Agents & ReAct Reasoning Loop</h1>
    <p>Structuring autonomous loops. We explore the ReAct (Reason + Action) paradigm, agent state machines, tool routing, and loop exit conditions.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 6 hours</span>
      <span class="meta-badge b">📈 Advanced</span>
      <span class="meta-badge p">⚡ +150 XP</span>
    </div>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory</h2>
    <h3 class="sh3">1. The ReAct (Reason-Action) Loop</h3>
    <p>A standard LLM is a single-shot generator. An **LLM Agent** operates iteratively. The **ReAct** prompting paradigm instructs the model to alternate between generating reasoning steps ("Thoughts"), selecting tools ("Actions"), and receiving outputs from those tools ("Observations") until a final answer is resolved.</p>

    <div class="mermaid">
      graph TD
      Prompt["User Goal / Query"] --> Loop["1. Generate Thought: Analyze goal"]
      Loop --> Action["2. Choose Action: Pick Tool & Args"]
      Action --> Tool["3. Execute Tool: Run local script / API"]
      Tool --> Obs["4. Receive Observation: Capture output"]
      Obs --> Check{"5. Done?"}
      Check -->|No| Loop
      Check -->|Yes| Answer["6. Return Final Answer"]
    </div>
    <div class="diagram-cap">ReAct Agent iterative reasoning-acting execution sequence</div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">What does ReAct stand for in LLM orchestration?</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q106-1')"><span class="quiz-letter">A</span> Reasoning and Acting</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q106-1')"><span class="quiz-letter">B</span> Reactive Activation</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q106-1')"><span class="quiz-letter">C</span> Recurrent Action</div>
      <div class="quiz-feedback correct-fb" id="q106-1-correct">✅ Correct! ReAct combines thought steps and tool calls iteratively.</div>
      <div class="quiz-feedback wrong-fb" id="q106-1-wrong">❌ Incorrect. Review the ReAct paradigm paper title.</div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://arxiv.org/abs/2210.03629" target="_blank">
        <div class="rc-type">📄 PAPER</div>
        <div class="rc-title">ReAct: Synergizing Reasoning and Acting in Language Models</div>
        <div class="rc-sub">Yao et al. (2022)</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-106" onclick="completeDay(106, 150)">✓ Mark Day 106 Complete</button>
</div>

<!-- ═══════════════════════════════════════
     DAY 107
     ════════════════════════════════════════ -->
<div class="day-section" id="day-107">
  <div class="day-header">
    <div class="day-tag">WEEK 15 · DAY 107 · MONTH 5 — LLM ENGINEERING</div>
    <h1>Capstone: Production-Ready ReAct Agentic System</h1>
    <p>Applying agentic patterns to a production-grade project. Today, we write a complete, self-contained Python script to build a ReAct Agent loop, register multiple tools, implement safety guards, and trace the agent's thought-action steps.</p>
    <div class="meta-row">
      <span class="meta-badge g">⏱ 8 hours</span>
      <span class="meta-badge o">🔥 Capstone Project</span>
      <span class="meta-badge p">⚡ +300 XP</span>
      <span class="meta-badge b">💻 PyTorch & APIs</span>
    </div>
  </div>

  <div class="objectives">
    <h3>🎯 Objectives:</h3>
    <ul>
      <li>Implement a structured ReAct agent execution loop in Python.</li>
      <li>Create a safe local execution tool registry.</li>
      <li>Incorporate error handling to prevent agents from crashing on tool execution errors.</li>
      <li>Construct safety limits (max iterations) to stop infinite loops.</li>
    </ul>
  </div>

  <div id="theory">
    <h2 class="sh2">🧠 Theory & Agent Safety</h2>
    <h3 class="sh3">1. Agent Guardrails</h3>
    <p>When deploying agents, two safety issues emerge:
    <br>1. **Infinite Loops:** If the model gets confused by an observation, it might call the same tool with the same arguments repeatedly. We must enforce a <code>max_iterations</code> hard limit.
    <br>2. **Malicious Tool Execution:** If the agent has access to a code execution block (e.g., Python shell), it can run arbitrary system commands. We must sandbox the execution environment and strictly sanitize inputs.</p>

    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — react_agent.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre><span class="kw">import</span> re

# Define local tools
<span class="kw">def</span> <span class="fn">get_weather</span>(location):
    if "mumbai" in location.lower():
        return "Weather in Mumbai: 30°C, Humidity 80%."
    return "Weather in location unknown."

<span class="kw">def</span> <span class="fn">calculate</span>(expression):
    try:
        # Safe evaluation without arbitrary commands
        allowed_chars = "0123456789+-*/() "
        if not all(c in allowed_chars for c in expression):
            return "Invalid expression"
        return str(eval(expression, {{"__builtins__": None}}, {{}}))
    except Exception as e:
        return f"Error: {e}"

tools = {{"get_weather": get_weather, "calculate": calculate}}

# Simple ReAct Prompt Template
prompt_template = """Answer the user question. You can use these tools:
- get_weather: takes a location string
- calculate: takes a math expression

Use this format:
Thought: your reasoning steps
Action: tool_name(arguments)
Observation: tool output
... (repeat Thought/Action/Observation)
Thought: I know the final answer
Final Answer: your response

Question: {question}
"""</pre>
    </div>
  </div>

  <div id="quiz-section">
    <h2 class="sh2">✅ Knowledge Check</h2>
    <div class="quiz-block">
      <div class="quiz-num">Q1 OF 3</div>
      <div class="quiz-q">Why is it critical to validate inputs in a calculation tool used by an LLM agent?</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q107-1')"><span class="quiz-letter">A</span> To save token usage.</div>
      <div class="quiz-opt" onclick="quiz(this,'correct','q107-1')"><span class="quiz-letter">B</span> To prevent command execution exploits (e.g. running system commands via eval).</div>
      <div class="quiz-opt" onclick="quiz(this,'wrong','q107-1')"><span class="quiz-letter">C</span> To speed up the arithmetic execution time.</div>
      <div class="quiz-feedback correct-fb" id="q107-1-correct">✅ Correct! Arbitrary code execution can allow prompt injections to read/write files on the host server.</div>
      <div class="quiz-feedback wrong-fb" id="q107-1-wrong">❌ Incorrect. Think about the security implications of running code sent by an LLM interface.</div>
    </div>
  </div>

  <div id="tasks-section">
    <h2 class="sh2">💻 Capstone Project Task</h2>
    <div class="task-block">
      <div class="task-header" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink)" onclick="toggleTask(this)">
        <span class="task-badge tb-hard">🔴 HARD</span>
        <span class="task-title">Construct the ReAct Agent Loop</span>
        <span class="task-time">⏱ 180 min</span>
      </div>
      <div class="task-body">
        <p>Build a fully functional Agent Loop in Python:
        <br>1. Write a parser function that extracts <code>Action: tool_name(args)</code> and <code>Final Answer: message</code> from a model response.
        <br>2. Build the execution state loop that passes the Observation back into the model prompt recursively.
        <br>3. Implement a safety guard stopping execution after 5 iterations, returning a fallback response.</p>
        <button class="solution-toggle" onclick="toggleSolution('sol-d107t1')">👁 Show Loop Solution</button>
        <div class="solution-box" id="sol-d107t1">
          <pre><span class="kw">def</span> <span class="fn">run_agent_loop</span>(question, max_iters=5):
    current_prompt = prompt_template.format(question=question)
    
    for i in range(max_iters):
        print(f"\n--- Iteration {i+1} ---")
        # In production, call the LLM API here.
        # We mock a model output requesting a tool call
        if i == 0:
            model_output = "Thought: I need to check the weather in Mumbai.\nAction: get_weather('Mumbai')"
        elif i == 1:
            model_output = "Thought: Now I need to calculate the humidity index.\nAction: calculate('30 * 2')"
        else:
            model_output = "Thought: I have calculated the values.\nFinal Answer: The humidity indexing factor is 60."
            
        print("Model:", model_output)
        
        # Check for final answer
        if "Final Answer:" in model_output:
            return model_output.split("Final Answer:")[-1].strip()
            
        # Parse Action
        match = re.search(r"Action:\s*(\w+)\('(.*?)'\)", model_output)
        if not match:
            return "Failed to parse action"
            
        tool_name, args = match.groups()
        tool_result = tools[tool_name](args)
        print("Tool Output:", tool_result)
        
        current_prompt += f"\n{model_output}\nObservation: {tool_result}"
        
    return "Reached maximum iterations without answer."

ans = run_agent_loop("Check weather in Mumbai and compute twice the value.")
print("\nFinal Result:", ans)</pre>
        </div>
      </div>
    </div>
  </div>

  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://github.com/langchain-ai/langgraph" target="_blank">
        <div class="rc-type">💻 GITHUB</div>
        <div class="rc-title">LangGraph Repository</div>
        <div class="rc-sub">Stateful multi-agent orchestration framework.</div>
      </a>
      <a class="resource-card" href="https://docs.crewai.com/" target="_blank">
        <div class="rc-type">📖 DOCS</div>
        <div class="rc-title">CrewAI Orchestration Framework</div>
        <div class="rc-sub">Role-playing autonomous agent collaboration framework documentation.</div>
      </a>
    </div>
  </div>

  <button class="complete-btn" id="btn-day-107" onclick="completeDay(107, 300)">✓ Mark Day 107 Complete</button>
</div>

</main>
</div>

<script>
// State Management
const STATE_KEY = 'w15-state';
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

    with open(week15_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("week15.html successfully generated with advanced content and updated days!")

if __name__ == '__main__':
    generate_week15()
