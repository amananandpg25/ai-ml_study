import os
import re
import shutil

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(base_dir, "roadmap.html")
backup_path = os.path.join(base_dir, "_backup_gemini/roadmap.html")

print("1. Restoring roadmap.html from backup...")
if os.path.exists(backup_path):
    shutil.copyfile(backup_path, roadmap_path)
    print("  Restored cleanly.")
else:
    print("  Error: backup not found!")
    exit(1)

content = open(roadmap_path, 'r', encoding='utf-8').read()

# 2. Inject extra CSS styles (focus-visible, theme-btn, print, and start-week-btn)
print("2. Injecting CSS styles...")
extra_css = """
/* ── FOCUS VISIBLE ── */
:focus-visible{outline:2px solid #4fd1a5;outline-offset:2px;border-radius:4px;}

/* ── DARK/LIGHT MODE ── */
[data-theme="light"]:root,[data-theme="light"]{
  --bg:#f5f7fa; --bg2:#eaedf3; --bg3:#dde2ee; --card:#ffffff;
  --border:#c8cedc; --text:#1a1f35; --muted:#6b7590;
}
.theme-btn{background:none;border:1px solid var(--border);color:var(--muted);font-family:monospace;font-size:11px;padding:3px 9px;border-radius:20px;cursor:pointer;transition:all .2s;white-space:nowrap}
.theme-btn:hover{border-color:#6c8cff;color:#6c8cff}

/* ── PRINT ── */
@media print{
  body{background:#fff;color:#000;font-size:12px}
  #sidebar,.theme-btn{display:none!important}
  #main{padding:0;margin:0}
  .section{display:block!important;page-break-after:always}
}

.start-week-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, rgba(79, 214, 160, 0.1), rgba(108, 140, 255, 0.1));
  border: 1px solid rgba(79, 209, 165, 0.3);
  color: var(--accent2);
  text-decoration: none;
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 13px;
  padding: 8px 16px;
  border-radius: 8px;
  margin-top: 12px;
  transition: all 0.2s ease;
  cursor: pointer;
}
.start-week-btn:hover {
  background: linear-gradient(135deg, rgba(79, 214, 160, 0.2), rgba(108, 140, 255, 0.2));
  border-color: var(--accent1);
  color: var(--text);
  transform: translateY(-1px);
}
"""
content = content.replace("</style>", f"{extra_css}</style>")

# 3. Add favicon and meta description in head
print("3. Adding favicon and meta description...")
if "rel=\"icon\"" not in content:
    favicon_html = """<meta name="description" content="Complete 135-day AI/ML roadmap from beginner to job-ready. Covers Python, ML, Deep Learning, NLP, Transformers, LLMs, and deployment.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%230d0f14'/><text x='4' y='23' font-family='monospace' font-size='16' font-weight='bold' fill='%234fd1a5'>AI</text></svg>">"""
    content = content.replace("</title>", f"</title>\n{favicon_html}")

# 4. Replace the entire sidebar nav element
print("4. Replacing sidebar navigation...")
new_sidebar = """<nav id="sidebar">
  <div class="sidebar-logo">
    <div style="display:flex;justify-content:space-between;align-items:center;width:100%">
      <div class="logo-text">AI/ML Master<br>Roadmap 2026</div>
      <button class="theme-btn" onclick="toggleTheme()" id="theme-btn" aria-label="Toggle dark/light mode" style="margin-left:auto">☀️ Light</button>
    </div>
    <div class="logo-sub">135 DAYS · COMPLETE GUIDE</div>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Overview</div>
    <div class="nav-item active" onclick="showSection('overview', this)">
      <span class="dot" style="background:#6c8cff"></span> Master Overview
    </div>
    <div class="nav-item" onclick="showSection('techstack', this)">
      <span class="dot" style="background:#4fd1a5"></span> Tech Stack
    </div>
    <a class="nav-item" href="dashboard.html" style="text-decoration:none">
      <span class="dot" style="background:#f7a94b"></span> 📊 Global Dashboard
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Month 1 — Foundations</div>
    <a class="nav-item" href="week1.html" style="text-decoration:none">
      <span class="dot" style="background:#4fd1a5"></span> Week 1 — Python Foundations <span class="day-range">1–7</span>
    </a>
    <a class="nav-item" href="week2.html" style="text-decoration:none">
      <span class="dot" style="background:#4fd1a5"></span> Week 2 — Pandas + SQL + Git <span class="day-range">8–14</span>
    </a>
    <a class="nav-item" href="week3.html" style="text-decoration:none">
      <span class="dot" style="background:#4fd1a5"></span> Week 3 — Preprocessing + Visualisation <span class="day-range">15–21</span>
    </a>
    <a class="nav-item" href="week4.html" style="text-decoration:none">
      <span class="dot" style="background:#4fd1a5"></span> Week 4 — Math for AI/ML <span class="day-range">22–30</span>
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Month 2 — Machine Learning</div>
    <a class="nav-item" href="week5.html" style="text-decoration:none">
      <span class="dot" style="background:#6c8cff"></span> Week 5 — ML Fundamentals <span class="day-range">31–37</span>
    </a>
    <a class="nav-item" href="week6.html" style="text-decoration:none">
      <span class="dot" style="background:#6c8cff"></span> Week 6 — Regression <span class="day-range">38–44</span>
    </a>
    <a class="nav-item" href="week7.html" style="text-decoration:none">
      <span class="dot" style="background:#6c8cff"></span> Week 7 — Classification <span class="day-range">45–51</span>
    </a>
    <a class="nav-item" href="week8.html" style="text-decoration:none">
      <span class="dot" style="background:#6c8cff"></span> Week 8 — Neural Networks & Deep Learning <span class="day-range">52–58</span>
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Month 3 — Deep Learning</div>
    <a class="nav-item" href="week9.html" style="text-decoration:none">
      <span class="dot" style="background:#f7a94b"></span> Week 9 — CNNs & Computer Vision <span class="day-range">59–65</span>
    </a>
    <a class="nav-item" href="week10.html" style="text-decoration:none">
      <span class="dot" style="background:#f7a94b"></span> Week 10 — RNNs & Sequential Data <span class="day-range">66–72</span>
    </a>
    <a class="nav-item" href="week11.html" style="text-decoration:none">
      <span class="dot" style="background:#f7a94b"></span> Week 11 — GANs & PyTorch <span class="day-range">73–79</span>
    </a>
    <a class="nav-item" href="week12.html" style="text-decoration:none">
      <span class="dot" style="background:#f7a94b"></span> Week 12 — Attention & Image Captioning <span class="day-range">80–86</span>
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Month 4 — Modern AI Stack</div>
    <a class="nav-item" href="week13.html" style="text-decoration:none">
      <span class="dot" style="background:#e56b8c"></span> Week 13 — Natural Language Processing <span class="day-range">87–93</span>
    </a>
    <a class="nav-item" href="week14.html" style="text-decoration:none">
      <span class="dot" style="background:#e56b8c"></span> Week 14 — Transformers & Attention <span class="day-range">94–100</span>
    </a>
    <a class="nav-item" href="week15.html" style="text-decoration:none">
      <span class="dot" style="background:#e56b8c"></span> Week 15 — LLM Engineering <span class="day-range">101–107</span>
    </a>
    <a class="nav-item" href="week16.html" style="text-decoration:none">
      <span class="dot" style="background:#e56b8c"></span> Week 16 — Production AI Engineering <span class="day-range">108–117</span>
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Final 18 Days</div>
    <a class="nav-item" href="week17.html" style="text-decoration:none">
      <span class="dot" style="background:#b47cfc"></span> Week 17 — Deploy + Flask + Docker <span class="day-range">118–124</span>
    </a>
    <a class="nav-item" href="week18.html" style="text-decoration:none">
      <span class="dot" style="background:#b47cfc"></span> Week 18 — Capstone & Portfolio Polish <span class="day-range">125–135</span>
    </a>
  </div>

  <div class="nav-section">
    <div class="nav-section-label">Reference</div>
    <div class="nav-item" onclick="showSection('projects', this)">
      <span class="dot" style="background:#b47cfc"></span> All Projects
    </div>
    <div class="nav-item" onclick="showSection('resources', this)">
      <span class="dot" style="background:#4fd1a5"></span> Resource Master List
    </div>
    <div class="nav-item" onclick="showSection('interview', this)">
      <span class="dot" style="background:#6c8cff"></span> Interview Prep
    </div>
    <div class="nav-item" onclick="showSection('career', this)">
      <span class="dot" style="background:#f7a94b"></span> Career Roadmap
    </div>
    <div class="nav-item" onclick="showSection('advice', this)">
      <span class="dot" style="background:#e56b8c"></span> Final Advice
    </div>
  </div>
</nav>"""

sidebar_pattern = r'<nav id="sidebar">.*?</nav>'
content, sub_count = re.subn(sidebar_pattern, new_sidebar, content, flags=re.DOTALL)
print(f"  Replaced sidebar element count={sub_count}")

# 5. Inject "Open Week Coursework" button in section headers
print("5. Injecting week buttons into coursework sections...")
mapping = {
    "m1w1": "week1.html",
    "m1w2": "week2.html",
    "m1w3": "week3.html",
    "m1w4": "week4.html",
    "m2w5": "week5.html",
    "m2w6": "week6.html",
    "m2w7": "week7.html",
    "m2w8": "week8.html",
    "m3w9": "week9.html",
    "m3w10": "week10.html",
    "m3w11": "week11.html",
    "m3w12": "week12.html",
    "m4w13": "week13.html",
    "m4w14": "week14.html",
    "m4w15": "week15.html",
    "m4w16": "week16.html",
    "fin1": "week17.html",
    "fin2": "week18.html"
}

for section_id, file_name in mapping.items():
    sec_pattern = rf'(<div id="{section_id}"[^>]*>.*?<div class="section-header">.*?)(</div>\s*<div class="week-block)'
    week_num_str = re.search(r'\d+', file_name).group(0)
    btn_html = f'\n      <br><a href="{file_name}" class="start-week-btn">🚀 Open Week {week_num_str} Coursework →</a>'
    
    def sec_repl(m):
        return m.group(1) + btn_html + "\n    " + m.group(2)
        
    content, count = re.subn(sec_pattern, sec_repl, content, flags=re.DOTALL)
    print(f"  Injected button for {section_id} -> count={count}")

# 6. Align topics (Week 6 and Week 8)
print("6. Aligning topics for Week 6 and Week 8...")
old_w6_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 38</div>
            <div class="day-title">Logistic Regression — Theory</div>
            <ul class="day-list">
              <li>Sigmoid function: maps any value to 0–1</li>
              <li>Decision boundary, threshold tuning</li>
              <li>Log loss / Binary cross-entropy</li>
              <li>Multinomial logistic regression (softmax)</li>
              <li>Implement binary logistic regression from scratch</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 39</div>
            <div class="day-title">Logistic Regression — Applications</div>
            <ul class="day-list">
              <li>sklearn LogisticRegression with regularisation (C parameter)</li>
              <li>Multiclass classification (OvR, OvO)</li>
              <li>Credit risk / disease prediction project</li>
              <li>ROC curve and AUC analysis</li>
              <li>Interpret model coefficients (feature importance)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 40</div>
            <div class="day-title">Naive Bayes + KNN</div>
            <ul class="day-list">
              <li>Naive Bayes: Bayes theorem applied to classification</li>
              <li>GaussianNB, MultinomialNB (for text)</li>
              <li>K-Nearest Neighbours: vote by k nearest points</li>
              <li>Choosing optimal K with elbow method</li>
              <li>Practice: Spam email classification with Naive Bayes</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 41–44</div>
            <div class="day-title">Project: Disease Prediction App</div>
            <ul class="day-list">
              <li>Dataset: Pima Indians Diabetes (Kaggle)</li>
              <li>Full pipeline: EDA → preprocessing → Logistic Regression</li>
              <li>Compare: Logistic Reg vs Naive Bayes vs KNN</li>
              <li>Evaluate with precision, recall, F1, ROC-AUC</li>
              <li>Simple Flask API (return prediction as JSON)</li>
              <li>Push to GitHub with full README</li>
            </ul>
            <div class="day-hours">⏱ 5–6 hrs/day</div>
          </div>
        </div>"""

new_w6_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 38</div>
            <div class="day-title">Linear Regression — Deep Dive</div>
            <ul class="day-list">
              <li>OLS Equation derivation & residual analysis</li>
              <li>Gradient descent optimization assumptions check</li>
              <li>Practice: Simple linear regression from scratch in Python</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 39</div>
            <div class="day-title">Polynomial Regression & Bias-Variance</div>
            <ul class="day-list">
              <li>Non-linear relations & polynomial feature mapping</li>
              <li>Overfitting detection using train/val curves</li>
              <li>Practice: Fitting non-linear functions & degree selection</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 40</div>
            <div class="day-title">Ridge & Lasso Regularisation (L1/L2)</div>
            <ul class="day-list">
              <li>Shrinkage penalties (L1 Lasso vs L2 Ridge)</li>
              <li>Feature selection properties of Lasso</li>
              <li>Practice: House valuation regularisation tuning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 41–44</div>
            <div class="day-title">Cross-Validation & Capstone Project</div>
            <ul class="day-list">
              <li>ElasticNet compound regularization</li>
              <li>K-Fold cross-validation & regression metrics</li>
              <li>Capstone: House Price Predictor with scikit-learn</li>
              <li>Simple Flask API deployment with model serialization</li>
            </ul>
            <div class="day-hours">⏱ 5–6 hrs/day</div>
          </div>
        </div>"""

content = content.replace(old_w6_content, new_w6_content)

old_w8_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 52</div>
            <div class="day-title">Perceptron & Multi-Layer Networks</div>
            <ul class="day-list">
              <li>Algorithm: init centroids → assign → update → repeat</li>
              <li>Choosing K: Elbow method, Silhouette score</li>
              <li>K-Means++ for better initialisation</li>
              <li>Limitations: spherical clusters, sensitive to outliers</li>
              <li>Practice: Customer segmentation project</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 54–55</div>
            <div class="day-title">Other Clustering + Association Rules</div>
            <ul class="day-list">
              <li>Hierarchical clustering (dendrograms)</li>
              <li>DBSCAN for arbitrary shapes + noise</li>
              <li>Association rule mining: Apriori algorithm</li>
              <li>Support, Confidence, Lift metrics</li>
              <li>Practice: Market basket analysis (grocery dataset)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 56–57</div>
            <div class="day-title">Reinforcement Learning Fundamentals</div>
            <ul class="day-list">
              <li>Agent, Environment, State, Action, Reward</li>
              <li>Markov Decision Process (MDP)</li>
              <li>Q-Learning algorithm (tabular)</li>
              <li>OpenAI Gym basics</li>
              <li>Practice: CartPole with Q-learning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 58–60</div>
            <div class="day-title">Month 2 Capstone: ML Portfolio Project</div>
            <ul class="day-list">
              <li>Project: End-to-end ML pipeline on real problem</li>
              <li>Options: Stock prediction, movie recommendation, fraud detection</li>
              <li>Include: EDA, preprocessing, 3+ models, evaluation, Flask API</li>
              <li>Deploy on Render.com (free tier)</li>
              <li>Full README with methodology and results</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>
        <div class="milestone">
          <div class="milestone-icon">🎉</div>
          <div class="milestone-content">
            <h4>Month 2 Complete — Machine Learning Mastered!</h4>
            <div class="milestone-checks">
              <span class="check-item">✓ All ML algorithms</span>
              <span class="check-item">✓ Precision/Recall/F1 mastered</span>
              <span class="check-item">✓ Bias-Variance understood</span>
              <span class="check-item">✓ K-Means clustering</span>
              <span class="check-item">✓ RL basics</span>
              <span class="check-item">✓ 3+ ML projects deployed</span>
              <span class="check-item">✓ First Kaggle submission</span>
            </div>
          </div>
        </div>"""

new_w8_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 52</div>
            <div class="day-title">Perceptron & Activation Functions</div>
            <ul class="day-list">
              <li>Single-layer perceptron threshold updates</li>
              <li>Activations: Sigmoid, Tanh, ReLU, Softmax</li>
              <li>Vanishing gradients & non-linear mappings</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 53-54</div>
            <div class="day-title">Backpropagation & Autograd Tensors</div>
            <ul class="day-list">
              <li>Math: Chain rule & weight gradient updates</li>
              <li>PyTorch tensors, dynamic computation graphs, autograd</li>
              <li>Accelerating calculations with CUDA GPUs</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 55-57</div>
            <div class="day-title">PyTorch Multi-Layer Perceptron (MLP)</div>
            <ul class="day-list">
              <li>Building an MLP using nn.Module & nn.Sequential</li>
              <li>Loss functions & optimizers (SGD, Adam, learning rates)</li>
              <li>Regularisation: Dropout, weight decay, early stopping</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 58</div>
            <div class="day-title">Capstone NN: MNIST Digit Classification</div>
            <ul class="day-list">
              <li>Digit classifier pipeline: load, scale, model, train</li>
              <li>Evaluate accuracy, draw confusion matrices</li>
              <li>Deploy digit recognition spaces on GitHub portfolios</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>
        <div class="milestone">
          <div class="milestone-icon">🎉</div>
          <div class="milestone-content">
            <h4>Month 2 Complete — Machine Learning Mastered!</h4>
            <div class="milestone-checks">
              <span class="check-item">✓ All classical ML algorithms</span>
              <span class="check-item">✓ Precision/Recall/F1 classification metrics</span>
              <span class="check-item">✓ Regularisation (Ridge/Lasso/ElasticNet)</span>
              <span class="check-item">✓ PyTorch MLP & autograd networks</span>
              <span class="check-item">✓ Backpropagation calculus</span>
              <span class="check-item">✓ Digit recognition Capstone</span>
              <span class="check-item">✓ ML APIs deployed</span>
            </div>
          </div>
        </div>"""

content = content.replace(old_w8_content, new_w8_content)

# 7. Align day ranges in sections
print("7. Aligning day ranges in section tags and headers...")
# Week 16 section tag
content = content.replace(
    '<div class="section-tag">MONTH 4 · DAYS 112–120</div>',
    '<div class="section-tag">MONTH 4 · DAYS 108–117</div>'
)
# Week 17 section tag
content = content.replace(
    '<div class="section-tag">FINAL · DAYS 121–127</div>',
    '<div class="section-tag">FINAL · DAYS 118–124</div>'
)

# 8. Align titles in sections (Week 15, 16, 17)
print("8. Aligning week section headers...")
content = content.replace(
    '<h2 style="color:var(--m4)">Week 15 — LLMs + GenAI</h2>',
    '<h2 style="color:var(--m4)">Week 15 — LLM Engineering</h2>'
)
content = content.replace(
    '<h2 style="color:var(--m4)">Week 16 — Production AI Engineering &amp; RAG + Agents</h2>',
    '<h2 style="color:var(--m4)">Week 16 — Production AI Engineering</h2>'
)
content = content.replace(
    '<h2 style="color:var(--mfin)">Days 121–127 — Flask + Docker + Kubernetes + Deployment</h2>',
    '<h2 style="color:var(--mfin)">Week 17 — Days 118–124 — Flask + Docker + Kubernetes + Deployment</h2>'
)

# 9. Inject/replace the entire javascript block cleanly
print("9. Replacing JS block...")
js_pattern = r'<script>.*?</script>'
new_js_block = """<script>
function showSection(id, el) {
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const section = document.getElementById(id);
  if (section) {
    section.classList.add('active');
    section.scrollIntoView({behavior: 'smooth', block: 'start'});
  }
  const targetEl = el || (window.event ? window.event.currentTarget : null);
  if (targetEl) {
    targetEl.classList.add('active');
  }
  closeSidebar();
}

function toggleSidebar() {
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (!sb) return;
  const open = sb.classList.toggle('open');
  if (btn) btn.setAttribute('aria-expanded', String(open));
}

function closeSidebar() {
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (sb) sb.classList.remove('open');
  if (btn) btn.setAttribute('aria-expanded', 'false');
}

function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') !== 'light';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
  const btn = document.getElementById('theme-btn');
  if (btn) btn.textContent = isDark ? '🌙 Dark' : '☀️ Light';
}

(function() {
  const saved = localStorage.getItem('theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
})();

window.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('theme');
  const btn = document.getElementById('theme-btn');
  if (btn && saved === 'light') btn.textContent = '🌙 Dark';
  
  // Initialize search filtering
  initSearch();
  
  // Initialize global progress bar
  initGlobalProgress();
});

// Client-side Search Implementation
function initSearch() {
  const searchInput = document.getElementById('roadmap-search');
  if (!searchInput) return;
  
  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    const dayCards = document.querySelectorAll('.day-card');
    
    dayCards.forEach(card => {
      const title = card.querySelector('.day-title').textContent.toLowerCase();
      const listItems = Array.from(card.querySelectorAll('.day-list li')).map(li => li.textContent.toLowerCase()).join(' ');
      const label = card.querySelector('.day-label').textContent.toLowerCase();
      
      if (title.includes(query) || listItems.includes(query) || label.includes(query)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

// Global Progress Aggregation
function initGlobalProgress() {
  let totalDays = 0;
  let completedDays = 0;
  let totalXp = 0;
  
  // Accumulate from all 18 weeks
  for (let w = 1; w <= 18; w++) {
    const stateStr = localStorage.getItem(`w${w}-state`);
    if (stateStr) {
      try {
        const state = JSON.parse(stateStr);
        if (state.done && Array.isArray(state.done)) {
          completedDays += state.done.length;
        }
        if (state.xp) {
          totalXp += state.xp;
        }
      } catch (e) {}
    }
  }
  
  // Update progress bar
  const progressPct = Math.round((completedDays / 135) * 100) || 0;
  const bar = document.getElementById('global-progress-bar-inner');
  const text = document.getElementById('global-progress-text');
  
  if (bar) bar.style.width = `${progressPct}%`;
  if (text) text.textContent = `${completedDays}/135 Days Completed (${progressPct}%) | Total XP: ${totalXp}`;
}
</script>"""

content, js_sub_count = re.subn(js_pattern, new_js_block, content, flags=re.DOTALL)
print(f"  Replaced script tag count={js_sub_count}")

# Make sure mob-menu-btn and sidebar-toggle markup are present
if "sidebar-toggle" not in content:
    print("  Adding mobile menu button markup...")
    content = content.replace("<body>", '<body>\n\n<button class="mob-menu-btn" onclick="toggleSidebar()" aria-label="Toggle navigation menu" aria-expanded="false" id="sidebar-toggle">☰ Menu</button>')


# 11. Write out the final master roadmap.html
print("11. Saving completed roadmap.html...")
with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Master roadmap fixing script completed successfully!")
