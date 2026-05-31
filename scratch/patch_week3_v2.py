import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week3.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Reorder Day 16 Target Encoding Methods
old_target_enc = """# Method 1: Manual Target Encoding (risky for data leakage)
city_target_mean = df.groupby('city')['churned'].mean()
df['city_encoded'] = df['city'].map(city_target_mean)

# Method 2: category_encoders library (Industry Standard, prevents leakage)
import category_encoders as ce
encoder = ce.TargetEncoder(cols=['city'])
# Fit on training data ONLY
df['city_ce_encoded'] = encoder.fit_transform(df['city'], df['churned'])"""

new_target_enc = """# Method 1: category_encoders library (Industry Standard, prevents leakage)
import category_encoders as ce
encoder = ce.TargetEncoder(cols=['city'])
# Fit on training data ONLY
df['city_ce_encoded'] = encoder.fit_transform(df['city'], df['churned'])

# Method 2: Manual Target Encoding (⚠️ DO NOT use in production)
# Doing groupby directly on target and mapping it causes severe data leakage!
city_target_mean = df.groupby('city')['churned'].mean()
df['city_encoded'] = df['city'].map(city_target_mean)"""

html = html.replace(old_target_enc, new_target_enc)

# 2. Add requires sklearn >= 1.2 comment to sparse_output=False
html = html.replace("sparse_output=False", "sparse_output=False)  # requires sklearn >= 1.2")
# Wait, let's look at the target in line 2437:
# ('encoder', OneHotEncoder(drop='first', sparse_output=False))
# If it is inside a tuple, replacing sparse_output=False might add a closing parenthesis if we are not careful.
# Let's restore and do it precisely for the two spots.
# Let's reload html first to avoid double replacement issues.
html = open(path, 'r', encoding='utf-8').read()
html = html.replace(old_target_enc, new_target_enc)

# First occurrence in Day 16
html = html.replace("ohe = OneHotEncoder(drop='first', sparse_output=False)",
                    "ohe = OneHotEncoder(drop='first', sparse_output=False)  # requires sklearn >= 1.2")

# Second occurrence in pipeline
html = html.replace("('encoder', OneHotEncoder(drop='first', sparse_output=False))",
                    "('encoder', OneHotEncoder(drop='first', sparse_output=False))  # requires sklearn >= 1.2")

# 3. Replace paywalled TDS links
# Day 15 TDS link
old_tds_15 = """    <a class="resource-card" href="https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4" target="_blank">
      <div class="rc-type">ARTICLE · TDS</div>
      <div class="rc-title">How to Handle Missing Data</div>
      <div class="rc-sub">Visual explanations of MCAR/MAR/MNAR with Python code</div>
    </a>"""

new_tds_15 = """    <a class="resource-card" href="https://machinelearningmastery.com/handle-missing-data-python/" target="_blank">
      <div class="rc-type">ARTICLE · MLM</div>
      <div class="rc-title">How to Handle Missing Data in Python</div>
      <div class="rc-sub">Practical guide to statistics, deletion, and imputation with scikit-learn.</div>
    </a>"""

html = html.replace(old_tds_15, new_tds_15)

# Day 17 TDS link
old_tds_17 = """    <a class="resource-card" href="https://towardsdatascience.com/feature-scaling-effect-of-different-scikit-learn-scalers-deep-dive-8dec775d4946" target="_blank">
      <div class="rc-type">ARTICLE · TDS</div>
      <div class="rc-title">Feature Scaling Deep Dive</div>
      <div class="rc-sub">Visual comparison of all sklearn scalers on different distributions</div>
    </a>"""

new_tds_17 = """    <a class="resource-card" href="https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/" target="_blank">
      <div class="rc-type">ARTICLE · MLM</div>
      <div class="rc-title">StandardScaler &amp; MinMaxScaler in Python</div>
      <div class="rc-sub">Detailed tutorial comparing standardization and normalization with code examples.</div>
    </a>"""

html = html.replace(old_tds_17, new_tds_17)

# 4. Inject Day 21 Predict-the-Output and Flashcards
old_d21_quiz_end = """    <div class="quiz-feedback wrong-fb" id="q21-4-wrong">❌ Start with Logistic Regression (classification) or Linear Regression (regression). Simple models are fast, interpretable, and give you a baseline to beat. If your fancy neural network only beats logistic regression by 0.5% accuracy, the simpler model wins (less latency, easier to debug, more interpretable). Start simple — add complexity only when the baseline isn't good enough.</div>
  </div>
  </div>"""

new_d21_quiz_end = """    <div class="quiz-feedback wrong-fb" id="q21-4-wrong">❌ Start with Logistic Regression (classification) or Linear Regression (regression). Simple models are fast, interpretable, and give you a baseline to beat. If your fancy neural network only beats logistic regression by 0.5% accuracy, the simpler model wins (less latency, easier to debug, more interpretable). Start simple — add complexity only when the baseline isn't good enough.</div>
  </div>
  </div>

  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
scaler = StandardScaler()
data = [[<span class="num">10</span>], [<span class="num">20</span>], [<span class="num">30</span>]]
scaler.fit(data)
<span class="bi">print</span>(scaler.transform([[<span class="num">20</span>]])[<span class="num">0</span>][<span class="num">0</span>])</pre></div>
    <input class="predict-input" id="p21-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p21-1','0.0')">Check Answer</button>
    <div class="predict-result" id="p21-1-result"></div>
  </div>

  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Week 3 Recap Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">MCAR vs MAR vs MNAR?</div><div class="fc-back">MCAR: completely random.<br>MAR: related to observed data.<br>MNAR: related to missing value itself.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">StandardScaler formula?</div><div class="fc-back">z = (x - mean) / std<br>Creates mean=0, variance=1.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">RobustScaler advantage?</div><div class="fc-back">Uses median and IQR (interquartile range)<br>Not influenced by extreme outliers.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">One-Hot Encoding dummy trap?</div><div class="fc-back">Multicollinearity from dummy columns.<br>Fixed by dropping first column.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is data leakage?</div><div class="fc-back">Information from test/validation set<br>leaking into training process.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Pipeline vs ColumnTransformer?</div><div class="fc-back">Pipeline: sequential transformations.<br>ColumnTransformer: parallel, column-specific.</div></div></div>
  </div>"""

html = html.replace(old_d21_quiz_end, new_d21_quiz_end)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched week3.html!")
