import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week4.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Day 22 Rendering Bugs
old_percentile_line = "outliers = salaries[(salaries < lower_fence) | (salaries > upper_fence)]"
new_percentile_line = "outliers = salaries[(salaries &lt; lower_fence) | (salaries &gt; upper_fence)]"
html = html.replace(old_percentile_line, new_percentile_line)

old_skewness_comment = "# Platykurtic < 0 (thin tails, fewer extremes)</span>"
new_skewness_comment = "# Platykurtic &lt; 0 (thin tails, fewer extremes)</span>"
html = html.replace(old_skewness_comment, new_skewness_comment)

# 2. Day 22 Concept Map
old_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Vectors & Matrices</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Matrix Operations</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Eigenvalues</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Calculus Limits</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Derivatives</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Vector Calculus</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Optimization</span>
    </div>
    <p style="font-size:12px; color:var(--muted); margin:0; line-height:1.5;">
      <strong>How it fits together:</strong> Matrix mathematics models feature vectors and coordinates in space, while derivatives calculate the gradient slopes necessary for training and parameter optimization.
    </p>"""

new_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Raw Data</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Central Tendency</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Dispersion</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Shape (Skew/Kurtosis)</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Outlier Detection</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Standardization</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">ML Preprocessing</span>
    </div>
    <p style="font-size:12px; color:var(--muted); margin:0; line-height:1.5;">
      <strong>How it fits together:</strong> Descriptive statistics describe raw distributions, shape metrics guide transformation choices, and outliers are identified before standardization scales inputs for machine learning model training.
    </p>"""

html = html.replace(old_map, new_map)

# 3. Day 26 Vector Projection & Dot Product Diagram
old_d26_dot = """# --- Dot product: measures alignment / similarity ---
# a · b = a₁b₁ + a₂b₂ + a₃b₃"""

new_d26_dot = """  <div class="diagram">
    <pre>
    Vector Projection & Dot Product
    =================================
             b 
            /  ^
           /   |
          /    | (Orthogonal projection)
         /     v
        +----------> a
             p
        
        * a · b = |a| * |b| * cos(θ)
        * Proj of b onto a: p = (|b| * cos(θ)) * (a / |a|)
        * dot product > 0  --> vectors point in similar directions (θ < 90°)
        * dot product == 0 --> vectors are perpendicular (θ == 90°)
        * dot product < 0  --> vectors point in opposite directions (θ > 90°)
    </pre>
    <div class="diagram-cap">Geometric projection of vector b onto vector a and dot product interpretations.</div>
  </div>

  <span class="cm"># --- Dot product: measures alignment / similarity ---</span>
  <span class="cm"># a · b = a₁b₁ + a₂b₂ + a₃b₃</span>"""

# Wait, let's see if the comment had syntax highlights in raw html
# Yes, it did: <span class="cm"># --- Dot product: measures alignment / similarity ---</span>
# Let's search using the highlighted spans
old_d26_dot_highlighted = """<span class="cm"># --- Dot product: measures alignment / similarity ---</span>
<span class="cm"># a · b = a₁b₁ + a₂b₂ + a₃b₃</span>"""

html = html.replace(old_d26_dot_highlighted, new_d26_dot)

# 4. Day 27 Parabolic Loss Curve / Gradient Descent Diagram
old_d27_mermaid = """  <div class="mermaid">
      graph TD
      A["Matrix A (m × n)"] --> Mult["C = A × B"]
      B["Matrix B (n × p)"] --> Mult
      Mult --> C["Matrix C (m × p)"]
      style Mult fill:#4fd1a5,stroke:#2a3050,color:#141720
  </div>"""

new_d27_diagram = """  <div class="diagram">
    <pre>
    Gradient Descent Loss Minimisation
    ====================================
    Loss L
      ^
      |      * (Initial parameter w_0, high loss)
      |       \\
      |        \\  -- Gradient points right (positive slope)
      |         v    Take step left (w_1 = w_0 - η * gradient)
      |          *
      |           \\
      |            \\
      |             v   * (Close to minimum, smaller steps)
      |              \\ /
      |               *  &lt;--- Global Minimum (Gradient = 0)
      +----------------------------------------&gt; w
                                (Parameter weight)
    </pre>
    <div class="diagram-cap">Gradient descent steps down the parabolic loss curve to reach the minimum point.</div>
  </div>"""

html = html.replace(old_d27_mermaid, new_d27_diagram)

# 5. Day 28 Resources Section
old_d28_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 28 Key Takeaways</h3>"""

new_d28_resources = """  <div id="day-28-resources-section">
  <h2 class="sh2">📚 Day 28 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://www.youtube.com/watch?v=ErfnhcEV1g8" target="_blank">
      <div class="rc-type">VIDEO · 3BLUE1BROWN</div>
      <div class="rc-title">Information Theory &amp; Entropy</div>
      <div class="rc-sub">Visual explainer on what entropy, information, and bits actually represent.</div>
    </a>
    <a class="resource-card" href="https://machinelearningmastery.com/what-is-information-entropy/" target="_blank">
      <div class="rc-type">ARTICLE · MLM</div>
      <div class="rc-title">A Gentle Introduction to Information Entropy</div>
      <div class="rc-sub">Detailed conceptual explanation with Python code examples.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 28 Key Takeaways</h3>"""

html = html.replace(old_d28_takeaways, new_d28_resources)

# 6. Day 29 Resources Section
old_d29_takeaways = """  <div class="takeaways">
    <h3>⭐ Day 29 Key Takeaways</h3>"""

new_d29_resources = """  <div id="day-29-resources-section">
  <h2 class="sh2">📚 Day 29 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://www.youtube.com/watch?v=FgakZw6K1QQ" target="_blank">
      <div class="rc-type">VIDEO · STATQUEST</div>
      <div class="rc-title">Principal Component Analysis (PCA) Step-by-Step</div>
      <div class="rc-sub">StatQuest's famous visual explanation of coordinates, projection, and PCA.</div>
    </a>
    <a class="resource-card" href="https://machinelearningmastery.com/calculate-principal-component-analysis-scratch-python/" target="_blank">
      <div class="rc-type">ARTICLE · MLM</div>
      <div class="rc-title">PCA From Scratch in Python</div>
      <div class="rc-sub">Detailed conceptual explanation and step-by-step matrix coding tutorial.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⭐ Day 29 Key Takeaways</h3>"""

html = html.replace(old_d29_takeaways, new_d29_resources)

# 7. Day 30 Prerequisites Callout
old_d30_header_end = """    <div class="meta-row">
      <span class="meta-badge g">⏱ 5 hours</span>
      <span class="meta-badge o">🏆 Portfolio Project</span>
      <span class="meta-badge p">⚡ +300 XP on completion</span>
    </div>"""

new_d30_header_end = """    <div class="meta-row">
      <span class="meta-badge g">⏱ 5 hours</span>
      <span class="meta-badge o">🏆 Portfolio Project</span>
      <span class="meta-badge p">⚡ +300 XP on completion</span>
    </div>
  </div>

  <div class="callout cw" style="margin-bottom: 1.5rem;">
    <strong>⚠️ Prerequisites:</strong>
    This capstone project requires concepts from Days 22–29 (Descriptive Statistics, Probability, Hypothesis Testing, Linear Algebra, Calculus, and PCA). If you skipped any math days, we highly recommend completing them first to understand the statistics and PCA steps.
  </div>"""

# Note: The raw HTML has a minor spacing difference or has the closing </div> differently in Day 30
# Let's inspect the match for line 2601-2605 in html
# <div class="meta-row">\n      <span class="meta-badge g">⏱ 5 hours</span>\n      <span class="meta-badge o">🏆 Portfolio Project</span>\n      <span class="meta-badge p">⚡ +300 XP on completion</span>\n    </div>
# Let's check if old_d30_header_end matches
if old_d30_header_end in html:
    html = html.replace(old_d30_header_end, new_d30_header_end)
else:
    # Try normalized match if whitespace differs
    html = html.replace("""    <div class="meta-row">
      <span class="meta-badge g">⏱ 5 hours</span>
      <span class="meta-badge o">🏆 Portfolio Project</span>
      <span class="meta-badge p">⚡ +300 XP on completion</span>
    </div>""", new_d30_header_end)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched week4.html!")
