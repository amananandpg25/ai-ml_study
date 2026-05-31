import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week5.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Populate Day 31 Quiz Q3–Q5 feedback placeholders
html = html.replace('<div class="quiz-feedback correct-fb" id="q31-3-correct">✅ Correct!</div>',
                    '<div class="quiz-feedback correct-fb" id="q31-3-correct">✅ Correct! High FP rate (15% legitimate flagged) hurts Precision. False Positives directly lower Precision = TP/(TP+FP). Precision is critical when the cost of a False Positive is high (like spam filters, where we don\'t want legitimate emails sent to junk).</div>')
html = html.replace('<div class="quiz-feedback wrong-fb" id="q31-3-wrong">❌ Incorrect.</div>',
                    '<div class="quiz-feedback wrong-fb" id="q31-3-wrong">❌ Incorrect. High FP rate (15% legitimate flagged hurts Precision). False Positives directly lower Precision = TP/(TP+FP). Precision is the ratio of true positives to total predicted positives.</div>')

html = html.replace('<div class="quiz-feedback correct-fb" id="q31-4-correct">✅ Correct!</div>',
                    '<div class="quiz-feedback correct-fb" id="q31-4-correct">✅ Correct! Parametric models assume a specific functional form (distribution/shape) for the data (e.g., Linear Regression assumes a straight line). Non-Parametric models make no such distribution assumptions (e.g., KNN makes classification decisions purely on local neighborhoods).</div>')
html = html.replace('<div class="quiz-feedback wrong-fb" id="q31-4-wrong">❌ Incorrect.</div>',
                    '<div class="quiz-feedback wrong-fb" id="q31-4-wrong">❌ Incorrect. Parametric models assume data distribution (e.g. Linear Regression assumes linearity). Non-Parametric models don\'t — KNN makes no distribution assumption.</div>')

html = html.replace('<div class="quiz-feedback correct-fb" id="q31-5-correct">✅ Correct!</div>',
                    '<div class="quiz-feedback correct-fb" id="q31-5-correct">✅ Correct! Check class distribution. If 95% of data is class 0, a model predicting 0 every time scores 95% accuracy while being completely useless for the minority class. Check precision, recall, or confusion matrix in such imbalanced cases.</div>')
html = html.replace('<div class="quiz-feedback wrong-fb" id="q31-5-wrong">❌ Incorrect.</div>',
                    '<div class="quiz-feedback wrong-fb" id="q31-5-wrong">❌ Incorrect. Check class distribution. If 95% of data is class 0, a model predicting 0 every time scores 95% accuracy while being completely useless for the minority class.</div>')

# 2. Week 5 Concept Map Reordering
old_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">ML Paradigms</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Train-Test Splits</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Bias & Variance</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Evaluation Metrics</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">KNN Classifier</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Hyperparameter Tuning</span>
    </div>
    <p style="font-size:12px; color:var(--muted); margin:0; line-height:1.5;">
      <strong>How it fits together:</strong> Splitting datasets allows measuring bias and variance, using standard evaluation metrics to optimize distance-based classifiers like K-Nearest Neighbors.
    </p>"""

new_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">ML Paradigms</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Train-Test Splits</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Evaluation Metrics</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Bias &amp; Variance</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">KNN &amp; Naive Bayes</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Hyperparameter Tuning</span>
    </div>
    <p style="font-size:12px; color:var(--muted); margin:0; line-height:1.5;">
      <strong>How it fits together:</strong> Splitting datasets allows measuring performance with evaluation metrics, finding bias-variance trade-offs to tune classifiers like KNN and Naive Bayes via hyperparameter tuning.
    </p>"""

html = html.replace(old_map, new_map)

# 3. Day 33 Multi-class warning for precision_score
old_d33_classification_eval_end = """<span class="bi">print</span>(f"  F1 Score  : {f1:.4f}")
<span class="bi">print</span>(f"  ROC AUC   : {auc:.4f}")</pre>
    </div>"""

new_d33_classification_eval_end = """<span class="bi">print</span>(f"  F1 Score  : {f1:.4f}")
<span class="bi">print</span>(f"  ROC AUC   : {auc:.4f}")</pre>
    </div>

  <div class="callout cw" style="margin-top: 1rem;">
    <strong>⚠️ Multi-class Warning:</strong>
    For multi-class classification, always pass <code>average='weighted'</code> (or <code>'macro'</code>/<code>'micro'</code>) to <code>precision_score</code>, <code>recall_score</code>, and <code>f1_score</code>. Binary classification is the ONLY case where the default works (it defaults to <code>average='binary'</code>, which raises a <code>ValueError</code> if there are more than 2 classes).
  </div>"""

html = html.replace(old_d33_classification_eval_end, new_d33_classification_eval_end)

# 4. Inject Day 31 Flashcards before Key Takeaways
old_d31_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 31 Key Takeaways</h3>"""

day31_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 31 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Supervised learning?</div><div class="fc-back">Algorithms trained on labeled data<br>e.g., house price prediction</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Unsupervised learning?</div><div class="fc-back">Algorithms find patterns in unlabeled data<br>e.g., customer segmentation</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Reinforcement learning?</div><div class="fc-back">Agent learns behavior by interacting<br>with environment via reward feedback</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is overfitting?</div><div class="fc-back">Model memorizes noise in training data<br>and fails to generalize to test data</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 31 Key Takeaways</h3>"""

html = html.replace(old_d31_takeaways, day31_flashcards)

# 5. Inject Day 32 Flashcards before Key Takeaways
old_d32_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 32 Key Takeaways</h3>"""

day32_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 32 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">MAE (Mean Absolute Error)?</div><div class="fc-back">Average of absolute error magnitudes<br>Robust to extreme outliers</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">MSE (Mean Squared Error)?</div><div class="fc-back">Average of squared error magnitudes<br>Penalizes large mistakes heavily</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">RMSE (Root Mean Squared Error)?</div><div class="fc-back">Square root of MSE<br>Same physical units as target variable</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">R² Score (Coeff of Determination)?</div><div class="fc-back">Proportion of target variance explained<br>by features. 1.0 is perfect fit.</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 32 Key Takeaways</h3>"""

html = html.replace(old_d32_takeaways, day32_flashcards)

# 6. Inject Day 33 Predict-the-Output before Quiz
old_d33_quiz = """  <h2 class="sh2">✅ Knowledge Check — Day 33 Quiz</h2>"""

day33_predict = """  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre>tp, fp, fn = 8, 2, 0
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print(f"P: {precision:.1f}, R: {recall:.1f}")</pre></div>
    <input class="predict-input" id="p33-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p33-1','P: 0.8, R: 1.0')">Check Answer</button>
    <div class="predict-result" id="p33-1-result"></div>
  </div>

  <h2 class="sh2">✅ Knowledge Check — Day 33 Quiz</h2>"""

html = html.replace(old_d33_quiz, day33_predict)

# 7. Inject Day 34 Predict-the-Output and Flashcards
old_d34_quiz = """  <h2 class="sh2">✅ Knowledge Check — Day 34 Quiz</h2>"""

day34_predict = """  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre># Model A: Train Loss = 0.01, Test Loss = 0.95
# Model B: Train Loss = 0.15, Test Loss = 0.17
# Which model represents high variance? Type A or B.
print("High Variance Model:", "A" if 0.95 - 0.01 > 0.17 - 0.15 else "B")</pre></div>
    <input class="predict-input" id="p34-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p34-1','High Variance Model: A')">Check Answer</button>
    <div class="predict-result" id="p34-1-result"></div>
  </div>

  <h2 class="sh2">✅ Knowledge Check — Day 34 Quiz</h2>"""

html = html.replace(old_d34_quiz, day34_predict)

old_d34_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 34 Key Takeaways</h3>"""

day34_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 34 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is Bias?</div><div class="fc-back">Error from simple assumptions<br>Causes underfitting (high train + test error)</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is Variance?</div><div class="fc-back">Error from sensitivity to train data swings<br>Causes overfitting (low train, high test error)</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Increasing model complexity effect?</div><div class="fc-back">Decreases Bias, but increases Variance<br>Risk of overfitting increases</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Reducing variance techniques?</div><div class="fc-back">Regularization, simplify model, gather more data</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 34 Key Takeaways</h3>"""

html = html.replace(old_d34_takeaways, day34_flashcards)

# 8. Inject Day 35 Predict-the-Output and Flashcards
old_d35_quiz = """  <h2 class="sh2">✅ Knowledge Check — Day 35 Quiz</h2>"""

day35_predict = """  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre># Grid Search: 2 hyperparameters, 3 values each, 5-fold CV.
# How many model fits are run in total?
fits = 2 * 3 # Wait, 3 values for H1, 3 for H2 -> 3 * 3 = 9 combinations
combinations = 3 * 3
fits = combinations * 5
print("Total fits:", fits)</pre></div>
    <input class="predict-input" id="p35-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p35-1','Total fits: 45')">Check Answer</button>
    <div class="predict-result" id="p35-1-result"></div>
  </div>

  <h2 class="sh2">✅ Knowledge Check — Day 35 Quiz</h2>"""

html = html.replace(old_d35_quiz, day35_predict)

old_d35_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 35 Key Takeaways</h3>"""

day35_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 35 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Grid Search?</div><div class="fc-back">Exhaustively tries all combinations of hyperparameters<br>Guarantees finding best combination in grid</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Random Search?</div><div class="fc-back">Randomly samples combinations from search space<br>Much faster, often finds close-to-best params</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Cross-Validation (CV)?</div><div class="fc-back">Splits train set into k folds to run evaluation<br>Prevents overfitting to training split</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is validation curves?</div><div class="fc-back">Plot of parameter values vs train/validation scores<br>Helps diagnose bias/variance trade-offs</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 35 Key Takeaways</h3>"""

html = html.replace(old_d35_takeaways, day35_flashcards)

# 9. Inject Day 36 Predict-the-Output and Flashcards
old_d36_quiz = """  <h2 class="sh2">✅ Knowledge Check — Day 36 Quiz</h2>"""

day36_predict = """  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre># Euclidean distance between p1=(1, 2) and p2=(4, 6)
import math
dist = math.sqrt((4 - 1)**2 + (6 - 2)**2)
print("Distance:", dist)</pre></div>
    <input class="predict-input" id="p36-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p36-1','Distance: 5.0')">Check Answer</button>
    <div class="predict-result" id="p36-1-result"></div>
  </div>

  <h2 class="sh2">✅ Knowledge Check — Day 36 Quiz</h2>"""

html = html.replace(old_d36_quiz, day36_predict)

old_d36_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 36 Key Takeaways</h3>"""

day36_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 36 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">KNN distance choice?</div><div class="fc-back">Euclidean distance (straight line)<br>or Manhattan distance (grid-like path)</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">KNN k selection?</div><div class="fc-back">Small k = overfitting (noisy decisions).<br>Large k = underfitting (smooth/simplistic).</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Naive Bayes assumption?</div><div class="fc-back">Features conditionally independent given class.<br>Rarely true in reality, but works surprisingly well!</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Laplace Smoothing?</div><div class="fc-back">Add 1 to count to prevent zero probability product<br>Handles unseen words in test data</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 36 Key Takeaways</h3>"""

html = html.replace(old_d36_takeaways, day36_flashcards)

# 10. Inject Day 37 Predict-the-Output before Quiz
old_d37_quiz = """  <h2 class="sh2">✅ Knowledge Check — Day 37 Quiz</h2>"""

day37_predict = """  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre># Pipeline sequential steps
# Step 1: scale (transforms inputs)
# Step 2: model (Logistic Regression)
# Predict applies step 1 transform first. True or False?
print("Applies Transform:", True)</pre></div>
    <input class="predict-input" id="p37-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p37-1','Applies Transform: True')">Check Answer</button>
    <div class="predict-result" id="p37-1-result"></div>
  </div>

  <h2 class="sh2">✅ Knowledge Check — Day 37 Quiz</h2>"""

html = html.replace(old_d37_quiz, day37_predict)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched week5.html!")
