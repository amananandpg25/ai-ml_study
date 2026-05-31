import re

with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ----------------- Day 33: Replace Confusion Matrix Mermaid Diagram -----------------
print("Updating Day 33 Confusion Matrix Diagram...")
old_mermaid_day33 = """    <div class="mermaid">
      graph TD
      subgraph ActualPositive [\"\"\"\"Actual Positive\"\"\"\"]
      P_TP["Predicted Positive: TP"]
      P_FN["Predicted Negative: FN"]
      end
      subgraph ActualNegative [\"\"\"\"Actual Negative\"\"\"\"]
      P_FP["Predicted Positive: FP"]
      P_TN["Predicted Negative: TN"]
      end
    </div>
    <div class="diagram-cap">TP: True Positive, TN: True Negative, FP: False Positive, FN: False Negative.</div>"""

new_grid_day33 = """<div style="margin: 1.5rem 0; display: flex; flex-direction: column; align-items: center;">
  <div style="display: grid; grid-template-columns: 80px 140px 140px; grid-template-rows: 40px 100px 100px; gap: 6px; font-family: var(--font-body); text-align: center; width: 100%; max-width: 400px;">
    <!-- Column headers -->
    <div></div>
    <div style="background: var(--bg3); border: 1px solid var(--border); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: var(--blue); letter-spacing: 0.5px; text-transform: uppercase;">Pred Positive</div>
    <div style="background: var(--bg3); border: 1px solid var(--border); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: var(--pink); letter-spacing: 0.5px; text-transform: uppercase;">Pred Negative</div>

    <!-- Row 1: Actual Positive -->
    <div style="background: var(--bg3); border: 1px solid var(--border); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: var(--green); letter-spacing: 0.5px; text-transform: uppercase; writing-mode: vertical-lr; transform: rotate(180deg); padding: 4px;">Act Positive</div>
    <!-- TP Card -->
    <div style="background: rgba(79, 209, 165, 0.08); border: 2px solid var(--green); border-radius: 8px; padding: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
      <div style="font-size: 9px; font-family: var(--font-mono); color: var(--muted); text-transform: uppercase;">True Positive</div>
      <div style="font-size: 20px; font-weight: 800; color: var(--green); margin: 2px 0;">TP</div>
      <div style="font-size: 10px; color: var(--text); line-height: 1.2;">Correctly identified positive class</div>
    </div>
    <!-- FN Card -->
    <div style="background: rgba(229, 107, 140, 0.08); border: 1px dashed var(--pink); border-radius: 8px; padding: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; opacity: 0.85;">
      <div style="font-size: 9px; font-family: var(--font-mono); color: var(--muted); text-transform: uppercase;">False Negative</div>
      <div style="font-size: 20px; font-weight: 800; color: var(--pink); margin: 2px 0;">FN</div>
      <div style="font-size: 10px; color: var(--text); line-height: 1.2;">Missed positive class (Type II Error)</div>
    </div>

    <!-- Row 2: Actual Negative -->
    <div style="background: var(--bg3); border: 1px solid var(--border); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: var(--orange); letter-spacing: 0.5px; text-transform: uppercase; writing-mode: vertical-lr; transform: rotate(180deg); padding: 4px;">Act Negative</div>
    <!-- FP Card -->
    <div style="background: rgba(247, 169, 75, 0.08); border: 1px dashed var(--orange); border-radius: 8px; padding: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; opacity: 0.85;">
      <div style="font-size: 9px; font-family: var(--font-mono); color: var(--muted); text-transform: uppercase;">False Positive</div>
      <div style="font-size: 20px; font-weight: 800; color: var(--orange); margin: 2px 0;">FP</div>
      <div style="font-size: 10px; color: var(--text); line-height: 1.2;">False Alarm (Type I Error)</div>
    </div>
    <!-- TN Card -->
    <div style="background: rgba(108, 140, 255, 0.08); border: 2px solid var(--blue); border-radius: 8px; padding: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
      <div style="font-size: 9px; font-family: var(--font-mono); color: var(--muted); text-transform: uppercase;">True Negative</div>
      <div style="font-size: 20px; font-weight: 800; color: var(--blue); margin: 2px 0;">TN</div>
      <div style="font-size: 10px; color: var(--text); line-height: 1.2;">Correctly identified negative class</div>
    </div>
  </div>
</div>
<div class="diagram-cap">Confusion Matrix: columns show model predictions, rows show actual targets.</div>"""

if old_mermaid_day33 in content:
    content = content.replace(old_mermaid_day33, new_grid_day33)
    print("  Successfully replaced Day 33 Confusion Matrix diagram!")
else:
    # Try with single quotes or different whitespace
    print("  Could not find Day 33 Mermaid diagram with exact string, trying regex...")
    pattern_day33 = re.compile(r'<div class="mermaid">\s*graph TD\s*subgraph ActualPositive.*?</fe[^-]+?div>\s*<div class="diagram-cap">TP: True Positive.*?</div>', re.DOTALL)
    content, count = re.subn(r'<div class="mermaid">\s*graph TD\s*subgraph ActualPositive.*?</div>\s*<div class="diagram-cap">TP: True Positive.*?</div>', new_grid_day33, content, flags=re.DOTALL)
    print(f"  Regex sub count for Day 33: {count}")

# ----------------- Day 34: Replace Bias-Variance Tradeoff Diagram -----------------
print("Updating Day 34 Bias-Variance Diagram...")
old_mermaid_day34 = """    <div class="mermaid">
      graph TD
      Low["Low Complexity <br/> Underfitting / High Bias"] --> Opt["Optimal Fit <br/> Low Generalization Error"]
      Opt --> High["High Complexity <br/> Overfitting / High Variance"]
    </div>"""

new_curve_day34 = """<div class="callout" style="background:rgba(108,140,255,0.05);border:1px solid rgba(108,140,255,0.2);margin:1.5rem 0;padding:1.5rem;">
  <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--blue);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;text-align:center;">Bias-Variance Tradeoff Curve</div>
  <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
    <svg viewBox="0 0 600 320" width="100%" height="auto" style="background:transparent;overflow:visible;">
      <defs>
        <filter id="glow-red-bv" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#ff4d6d" flood-opacity="0.3"/>
        </filter>
        <filter id="glow-orange-bv" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#f7a94b" flood-opacity="0.3"/>
        </filter>
        <filter id="glow-blue-bv" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#6c8cff" flood-opacity="0.3"/>
        </filter>
      </defs>

      <!-- Axes -->
      <line x1="60" y1="260" x2="540" y2="260" stroke="var(--border)" stroke-width="2" />
      <line x1="60" y1="40" x2="60" y2="260" stroke="var(--border)" stroke-width="2" />

      <!-- Axis Labels -->
      <text x="300" y="295" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">Model Complexity</text>
      <text x="25" y="150" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle" transform="rotate(-90 25 150)">Error</text>

      <!-- Curves -->
      <path d="M 80 60 Q 220 220 520 240" fill="none" stroke="#f7a94b" stroke-width="3" filter="url(#glow-orange-bv)" />
      <text x="450" y="225" fill="#f7a94b" font-family="var(--font-mono)" font-size="10" font-weight="600">Bias²</text>

      <path d="M 80 240 Q 380 220 520 60" fill="none" stroke="#ff4d6d" stroke-width="3" filter="url(#glow-red-bv)" />
      <text x="450" y="80" fill="#ff4d6d" font-family="var(--font-mono)" font-size="10" font-weight="600">Variance</text>

      <path d="M 80 80 Q 280 340 520 80" fill="none" stroke="#6c8cff" stroke-width="4" filter="url(#glow-blue-bv)" />
      <text x="360" y="110" fill="#6c8cff" font-family="var(--font-mono)" font-size="11" font-weight="700">Total Error</text>

      <!-- Sweet spot -->
      <line x1="280" y1="40" x2="280" y2="260" stroke="var(--green)" stroke-dasharray="3 3" stroke-width="1.5" />
      <circle cx="280" cy="190" r="6" fill="var(--green)" stroke="var(--bg)" stroke-width="2" />
      
      <text x="140" y="275" fill="var(--muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Underfitting (High Bias)</text>
      <text x="280" y="275" fill="var(--green)" font-family="var(--font-mono)" font-size="10" font-weight="700" text-anchor="middle">Optimal Fit</text>
      <text x="420" y="275" fill="var(--muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Overfitting (High Variance)</text>

      <!-- Irreducible Error -->
      <line x1="60" y1="230" x2="540" y2="230" stroke="var(--muted)" stroke-dasharray="4 4" stroke-width="1" />
      <text x="480" y="225" fill="var(--muted)" font-family="var(--font-mono)" font-size="9">Irreducible Error</text>
    </svg>
  </div>
</div>"""

if old_mermaid_day34 in content:
    content = content.replace(old_mermaid_day34, new_curve_day34)
    print("  Successfully replaced Day 34 Bias-Variance curve diagram!")
else:
    print("  Could not find Day 34 Mermaid diagram with exact string, trying regex...")
    content, count = re.subn(r'<div class="mermaid">\s*graph TD\s*Low\["Low Complexity.*?</div>', new_curve_day34, content, flags=re.DOTALL)
    print(f"  Regex sub count for Day 34: {count}")

# ----------------- Flashcard Content definitions -----------------
flashcards = {
    31: """  <h2 class="sh2">🃏 Revision Flashcards — Day 31</h2>
  <p class="flashcard-hint">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Scikit-learn Design?</div><div class="fc-back">Built around Estimators (fit), Transformers (transform), and Predictors (predict).</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">fit() vs transform()?</div><div class="fc-back">fit() calculates parameters. transform() applies them to the data.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">fit_transform()?</div><div class="fc-back">Combines fit() and transform() in a single, optimized step.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Hyperparameters?</div><div class="fc-back">Configuration settings set before training (e.g. K in KNN) that aren't learned from data.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Model Parameters?</div><div class="fc-back">Internal weights or parameters learned by the model during training.</div></div></div>
  </div>""",
    32: """  <h2 class="sh2">🃏 Revision Flashcards — Day 32</h2>
  <p class="flashcard-hint">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Supervised Learning?</div><div class="fc-back">Training with labeled data (inputs + correct answers) for classification or regression.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Unsupervised Learning?</div><div class="fc-back">Finding hidden patterns, clusters, or distributions in unlabeled data.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Semisupervised Learning?</div><div class="fc-back">Training using a small amount of labeled data alongside a large pool of unlabeled data.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Inductive Bias?</div><div class="fc-back">The set of assumptions an algorithm uses to predict outputs for unseen inputs.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Feature vs Label?</div><div class="fc-back">Feature (X): input variable/predictor. Label (y): target output/dependent variable.</div></div></div>
  </div>""",
    34: """  <h2 class="sh2">🃏 Revision Flashcards — Day 34</h2>
  <p class="flashcard-hint">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Underfitting (High Bias)?</div><div class="fc-back">Model is too simple to capture patterns. Low training and validation accuracy.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Overfitting (High Variance)?</div><div class="fc-back">Model memorizes training noise. High training accuracy, low validation accuracy.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Optimal Fit (Sweet Spot)?</div><div class="fc-back">The complexity level where total generalization error is minimized.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Reduce High Variance?</div><div class="fc-back">Get more data, simplify model, use regularization, or dropout/feature selection.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Reduce High Bias?</div><div class="fc-back">Increase model complexity, engineer better features, or decrease regularization.</div></div></div>
  </div>""",
    35: """  <h2 class="sh2">🃏 Revision Flashcards — Day 35</h2>
  <p class="flashcard-hint">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">k-Fold Cross-Validation?</div><div class="fc-back">Splitting data into k folds, training k times on k-1 folds, validating on the remaining fold.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Stratified k-Fold?</div><div class="fc-back">Preserves class proportions in each fold. Critical for imbalanced datasets.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Data Leakage?</div><div class="fc-back">Validation/test set info leaks into training (e.g. scaling whole dataset before split).</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Prevent Data Leakage?</div><div class="fc-back">Fit transformers (scalers, encoders) ONLY on training fold, e.g. using Sklearn Pipelines.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Train-Val-Test Split?</div><div class="fc-back">Train: fits model. Val: tunes hyperparameters. Test: final unbiased accuracy check.</div></div></div>
  </div>""",
    36: """  <h2 class="sh2">🃏 Revision Flashcards — Day 36</h2>
  <p class="flashcard-hint">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">K-Nearest Neighbors?</div><div class="fc-back">Classifier/regressor that predicts based on the K closest data points in the feature space.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Lazy Learner?</div><div class="fc-back">KNN has zero training phase; it stores data and performs all distance calculations at inference.</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Effect of K value?</div><div class="fc-back">Small K: noisy boundaries (high variance). Large K: smoother boundaries (high bias).</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Distance Metrics?</div><div class="fc-back">Euclidean (straight line), Manhattan (grid distance), Minkowski (generalized distance).</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Why Feature Scaling?</div><div class="fc-back">KNN is distance-based, so unscaled larger range features dominate distance calculations.</div></div></div>
  </div>"""
}

# We will search for '<div id="tasks-section">' inside each day's block, and insert the flashcards right before it.
for day_num in [31, 32, 34, 35, 36]:
    day_id = f"day-{day_num}"
    print(f"Adding flashcards to Day {day_num}...")
    
    # We find where this day section starts
    day_start_tag = f'<div class="day-section" id="{day_id}">' if day_num > 31 else f'<div class="day-section active" id="{day_id}">'
    day_idx = content.find(day_start_tag)
    
    if day_idx != -1:
        # Find the next day-section start or the end of the sections to bound the search
        next_day_id = f"day-{day_num+1}"
        next_day_tag = f'<div class="day-section" id="{next_day_id}">'
        next_day_idx = content.find(next_day_tag)
        
        if next_day_idx == -1:
            # If it's the last day or next day isn't found, search up to main script / footer
            next_day_idx = content.find('<script>')
            
        day_block = content[day_idx:next_day_idx]
        
        # We find <div id="tasks-section"> inside this block
        task_idx = day_block.find('<div id="tasks-section">')
        if task_idx != -1:
            old_tasks_str = day_block[task_idx:task_idx+40] # just a small prefix for safe replacement
            new_tasks_str = flashcards[day_num] + "\n\n  " + old_tasks_str
            
            new_day_block = day_block.replace(old_tasks_str, new_tasks_str, 1)
            content = content.replace(day_block, new_day_block)
            print(f"  Successfully added flashcards to Day {day_num}!")
        else:
            print(f"  tasks-section not found in Day {day_num} block!")
    else:
        print(f"  Day {day_num} start tag not found!")

# Save the updated content
with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week5.html")
