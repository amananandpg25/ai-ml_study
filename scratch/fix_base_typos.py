import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# 1. Fix week6.html Day 39 typo and inject Day 44 Objectives
w6_path = os.path.join(base_dir, "week6.html")
if os.path.exists(w6_path):
    print("Fixing typos in week6.html...")
    content = open(w6_path, 'r', encoding='utf-8').read()
    
    # Day 39 typo
    old_typo = "Which performs best? Why might selecting interaction features help?</div>"
    new_fix = "Which performs best? Why might selecting interaction features help?</p>"
    if old_typo in content:
        content = content.replace(old_typo, new_fix)
        print("  Fixed Day 39 typo.")
    else:
        print("  Warning: Day 39 typo target not found.")
        
    # Day 44 objectives injection
    day44_header_end = """    <div class="meta-row">
      <span class="meta-badge g">⏱ 8+ hours</span>
      <span class="meta-badge b">🏆 Portfolio Project</span>
      <span class="meta-badge p">⚡ +500 XP on completion</span>
    </div>
  </div>"""
  
    objectives_block = """
  <div class="objectives">
    <h3>🎯 By end of Day 44 you will be able to:</h3>
    <ul>
      <li>Perform end-to-end Exploratory Data Analysis (EDA) on the Ames Housing dataset</li>
      <li>Construct a robust preprocessing pipeline dealing with missing data and outliers</li>
      <li>Implement feature engineering transformations including log-scaling and target encoding</li>
      <li>Train, cross-validate, and tune advanced tree ensembles (Random Forest, XGBoost)</li>
    </ul>
  </div>"""
  
    if day44_header_end in content:
        if '🎯 By end of Day 44 you will be able to:' not in content:
            content = content.replace(day44_header_end, day44_header_end + objectives_block)
            print("  Injected Day 44 Objectives.")
        else:
            print("  Day 44 Objectives already present.")
    else:
        print("  Warning: Day 44 header end target not found.")
        
    with open(w6_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Fix week7.html Day 47 and Day 51 unclosed theory divs
w7_path = os.path.join(base_dir, "week7.html")
if os.path.exists(w7_path):
    print("Fixing typos in week7.html...")
    content = open(w7_path, 'r', encoding='utf-8').read()
    
    # Day 47 unclosed theory
    interview_target = '<div class="interview">Interview favourite: "Why does Random Forest reduce variance compared to a single Decision Tree?" Answer: Each tree is trained on a different bootstrap sample (reduces correlation between trees) AND at each split only √p features are considered (further decorrelates trees). Since errors are uncorrelated, averaging many trees cancels out individual errors. Variance of the average of n correlated predictions = ρσ² + (1-ρ)σ²/n. RF minimises ρ (correlation).</div>'
    replacement = interview_target + '\n  </div><!-- /theory -->'
    
    if interview_target in content:
        if '</div>\n  </div><!-- /theory -->' not in content:
            content = content.replace(interview_target, replacement)
            print("  Closed Day 47 theory section.")
        else:
            print("  Day 47 theory section already closed.")
    else:
        print("  Warning: Day 47 interview target not found.")
        
    # Day 51 unclosed theory
    day51_target = """    <label class="checklist-item" onclick="toggleCheck(this)">
      <div class="chk-box"></div>
      <div class="chk-text">LinkedIn post written about the project (include SHAP plot image)</div>
    </label>
  </div>"""
    day51_replacement = day51_target + "\n  </div><!-- /theory -->"
    
    if day51_target in content:
        if 'LinkedIn post written about the project (include SHAP plot image)</div>\n    </label>\n  </div>\n  </div><!-- /theory -->' not in content:
            content = content.replace(day51_target, day51_replacement)
            print("  Closed Day 51 theory section.")
        else:
            print("  Day 51 theory section already closed.")
    else:
        print("  Warning: Day 51 checklist target not found.")
        
    with open(w7_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Deduplicate misconceptions in week16.html and week17.html
def deduplicate_misconceptions(file_path, day, search_str):
    if not os.path.exists(file_path):
        print(f"  Warning: {file_path} not found for deduplication.")
        return
    content = open(file_path, 'r', encoding='utf-8').read()
    
    day_marker = f'id="day-{day}"'
    if day_marker not in content:
        day_marker = f"id='day-{day}'"
    parts = content.split(day_marker, 1)
    if len(parts) < 2:
        print(f"  Warning: Day {day} not found in {file_path}.")
        return
    
    day_body = parts[1]
    next_marker = f'id="day-{day+1}"'
    next_marker_alt = f"id='day-{day+1}'"
    end_idx = day_body.find(next_marker)
    if end_idx == -1:
        end_idx = day_body.find(next_marker_alt)
    if end_idx == -1:
        end_idx = day_body.find("</div><!-- /day-")
    if end_idx == -1:
        end_idx = len(day_body)
        
    actual_body = day_body[:end_idx]
    remainder = day_body[end_idx:]
    
    count = actual_body.count(search_str)
    if count > 1:
        first_idx = actual_body.find(search_str)
        if first_idx != -1:
            clean_body = actual_body.replace(search_str, "")
            clean_body = clean_body[:first_idx] + search_str + clean_body[first_idx:]
            print(f"  Deduplicated {count} occurrences of misconception in {os.path.basename(file_path)} Day {day} to 1.")
            content = parts[0] + day_marker + clean_body + remainder
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

miscon16_str = """<div class="misconception">
    <strong>⚠️ Common Misconception:</strong> Deep models for MLOps, Flask APIs, Docker, Gradio, Model Serving always generalize better without regularization.
    <br><br>
    <strong>Fact:</strong> Deeper models have higher capacity to overfit. Regularization (dropout, weight decay, early stopping) is crucial to maintain test set accuracy.
  </div>"""

miscon17_str = """<div class="misconception">
    <strong>⚠️ Common Misconception:</strong> Deep models for Advanced Production Project, Deployment, Final Portfolio Polish always generalize better without regularization.
    <br><br>
    <strong>Fact:</strong> Deeper models have higher capacity to overfit. Regularization (dropout, weight decay, early stopping) is crucial to maintain test set accuracy.
  </div>"""

w16_path = os.path.join(base_dir, "week16.html")
deduplicate_misconceptions(w16_path, 109, miscon16_str)

w17_path = os.path.join(base_dir, "week17.html")
deduplicate_misconceptions(w17_path, 119, miscon17_str)

# 4. Final Audit & Typo Cleanups for Week 1, 3, 4, 8, 9, 10, 11, 12, 16, 17
# Fix title of week1.html
w1_path = os.path.join(base_dir, "week1.html")
if os.path.exists(w1_path):
    print("Fixing title in week1.html...")
    content = open(w1_path, 'r', encoding='utf-8').read()
    content = content.replace(
        "<title>Week 1 — Python Foundations v2 | 135-Day AI/ML Roadmap</title>",
        "<title>Week 1 — Python Foundations | 135-Day AI/ML Roadmap</title>"
    )
    with open(w1_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix duplicate ID q20-2-correct in week3.html
w3_path = os.path.join(base_dir, "week3.html")
if os.path.exists(w3_path):
    print("Fixing duplicate quiz ID in week3.html...")
    content = open(w3_path, 'r', encoding='utf-8').read()
    content = content.replace(
        'id="q20-2-correct">✅ Correct! Historically, families on Titanic',
        'id="q20-3-correct">✅ Correct! Historically, families on Titanic'
    )
    with open(w3_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix takeaways & Hinglish summary for Day 30 in week4.html
w4_path = os.path.join(base_dir, "week4.html")
if os.path.exists(w4_path):
    print("Adding takeaways and Hinglish summary for Day 30 in week4.html...")
    content = open(w4_path, 'r', encoding='utf-8').read()
    target_btn = '<button class="complete-btn" id="btn-day-30" onclick="completeDay(30, 300)">✓ Mark Day 30 Complete — Earn 300 XP & Finish Month 1! 🎉</button>'
    new_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 30 Key Takeaways</h3>
    <ol>
      <li>Month 1 capstone project is the culmination of all core Python, SQL, Pandas, and Math foundations.</li>
      <li>EDA & hypothesis testing form the scientific validation before modeling.</li>
      <li>ColumnTransformer pipeline is the professional standard for scaling and encoding.</li>
      <li>PCA is a powerful tool to compress and visually verify if clusters are linearly separable.</li>
    </ol>
  </div>

  <div class="hinglish">💡 Month 1 complete! Aapne Python, stats, preprocessing pipelines, aur dimension reduction (PCA) seekha aur unhe capstone project mein integrate kiya. Ab aap ML modeling ke liye bilkul ready hain.</div>

"""
    if 'Day 30 Key Takeaways' not in content:
        content = content.replace(target_btn, new_takeaways + target_btn)
    with open(w4_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix duplicate ID q57a-correct in week8.html
w8_path = os.path.join(base_dir, "week8.html")
if os.path.exists(w8_path):
    print("Fixing duplicate quiz ID in week8.html...")
    content = open(w8_path, 'r', encoding='utf-8').read()
    content = content.replace(
        'id="q57a-correct">✅ Correct! Wild oscillation = LR too high.',
        'id="q57b-correct">✅ Correct! Wild oscillation = LR too high.'
    )
    with open(w8_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix duplicate theory/math IDs in weeks 9, 10, 11, 12
for w, day, header, new_id in [
    (9, 65, "🔬 Graduate Mathematics & Derivations", "day-65-math"),
    (10, 72, "🔬 Graduate Mathematics & Derivations", "day-72-math"),
    (11, 79, "🧠 Graduate Mathematical Proofs", "day-79-math"),
    (12, 86, "🔬 Advanced Mathematical Derivations", "day-86-math")
]:
    w_path = os.path.join(base_dir, f"week{w}.html")
    if os.path.exists(w_path):
        print(f"Fixing duplicate math section ID in week{w}.html...")
        content = open(w_path, 'r', encoding='utf-8').read()
        target = f'<div id="theory">\n  <h2 class="sh2">{header}</h2>'
        replacement = f'<div id="{new_id}">\n  <h2 class="sh2">{header}</h2>'
        content = content.replace(target, replacement)
        with open(w_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Fix quiz typos in week12.html (Day 83 and 84)
w12_path = os.path.join(base_dir, "week12.html")
if os.path.exists(w12_path):
    print("Fixing quiz IDs in week12.html...")
    content = open(w12_path, 'r', encoding='utf-8').read()
    
    # Locate Day 83 section
    d83_idx = content.find('id="day-83"')
    d84_idx = content.find('id="day-84"')
    d85_idx = content.find('id="day-85"')
    
    if d83_idx != -1 and d84_idx != -1:
        d83_part = content[d83_idx:d84_idx]
        fixed_d83 = d83_part.replace("'q82b'", "'q83b'").replace('"q82b-correct"', '"q83b-correct"').replace('"q82b-wrong"', '"q83b-wrong"')
        content = content.replace(d83_part, fixed_d83)
        
    if d84_idx != -1 and d85_idx != -1:
        d84_part = content[d84_idx:d85_idx]
        fixed_d84 = d84_part.replace("'q83c'", "'q84c'").replace('"q83c-correct"', '"q84c-correct"').replace('"q83c-wrong"', '"q84c-wrong"')
        content = content.replace(d84_part, fixed_d84)
        
    with open(w12_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Clean up sidebar-toggle duplicates in all weeks
for w in range(1, 18):
    w_path = os.path.join(base_dir, f"week{w}.html")
    if os.path.exists(w_path):
        content = open(w_path, 'r', encoding='utf-8').read()
        import re
        pattern = r'<button class="mob-menu-btn"[^>]*>'
        replacement = '<button class="mob-menu-btn" onclick="toggleSidebar()" aria-label="Toggle navigation menu" aria-expanded="false" id="sidebar-toggle">'
        content = re.sub(pattern, replacement, content)
        with open(w_path, 'w', encoding='utf-8') as f:
            f.write(content)

