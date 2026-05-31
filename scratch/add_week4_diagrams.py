import os
import re

file_path = "/Users/amananand/Downloads/SDE/ai:ml/week4.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the diagrams for days 22 to 29
diagrams = {
    22: """
  <div class="mermaid">
      graph TD
      Stats["Descriptive Statistics"] --> CT["Central Tendency"]
      Stats --> Disp["Dispersion"]
      CT --> Mean["Mean (Sensitive to Outliers)"]
      CT --> Median["Median (Robust to Outliers)"]
      CT --> Mode["Mode"]
      Disp --> Var["Variance (σ²)"]
      Disp --> SD["Standard Deviation (σ)"]
      Disp --> IQR["Interquartile Range"]
  </div>
""",
    23: """
  <div class="mermaid">
      graph LR
      P["Probability P(A)"] --> Value["Range: [0, 1]"]
      P --> Cond["Conditional: P(A|B) = P(A∩B)/P(B)"]
      P --> Ind["Independent: P(A∩B) = P(A) × P(B)"]
      P --> Dep["Dependent: P(A∩B) = P(A) × P(B|A)"]
  </div>
""",
    24: """
  <div class="mermaid">
      graph TD
      Prior["Prior: P(A) <br> Initial belief"] --> Posterior["Posterior: P(A|B) <br> Updated belief"]
      Likelihood["Likelihood: P(B|A) <br> Evidence probability"] --> Posterior
      Normalizer["Normalizer: P(B) <br> Total probability"] --> Posterior
  </div>
""",
    25: """
  <div class="mermaid">
      graph TD
      Dist["Probability Distributions"] --> Disc["Discrete (PMF / CDF)"]
      Dist --> Cont["Continuous (PDF / CDF)"]
      Disc --> Bin["Binomial (n trials, success prob p)"]
      Disc --> Pois["Poisson (count of events in interval)"]
      Cont --> Norm["Normal / Gaussian (Bell curve, μ & σ)"]
      Cont --> Unif["Uniform (Equal probability everywhere)"]
  </div>
""",
    26: """
  <div class="mermaid">
      graph LR
      Vec["Vector x"] --> Mat["Matrix A"]
      Mat --> Out["Transformed Vector Ax"]
      style Mat fill:#6c8cff,stroke:#2a3050,color:#fff
  </div>
""",
    27: """
  <div class="mermaid">
      graph TD
      A["Matrix A (m × n)"] --> Mult["C = A × B"]
      B["Matrix B (n × p)"] --> Mult
      Mult --> C["Matrix C (m × p)"]
      style Mult fill:#4fd1a5,stroke:#2a3050,color:#141720
  </div>
""",
    28: """
  <div class="mermaid">
      graph LR
      High["High-Dim Data"] --> Cov["Covariance Matrix"]
      Cov --> Eigen["Eigenvalues / Eigenvectors"]
      Eigen --> Proj["Project onto Top Components"]
      Proj --> Low["Low-Dim PCA Space"]
  </div>
""",
    29: """
  <div class="mermaid">
      graph TD
      Loss["Loss Function J(w)"] --> Grad["Compute Gradient ∇J"]
      Grad --> Dir["Gradient Points UPHILL"]
      Dir --> Update["Update: w = w - η × ∇J"]
      Update --> Loop["Repeat to Convergence"]
  </div>
"""
}

modified = False
for day, diagram in diagrams.items():
    # We want to find the tag: <div id="day-N-theory"> followed by <h2 class="sh2">🧠 Theory</h2>
    # Note: we need to match spaces and potential newlines.
    pattern = rf'(<div\s+id="day-{day}-theory"[^>]*>\s*<h2\s+class="sh2">🧠\s+Theory</h2>)'
    match = re.search(pattern, content)
    if match:
        matched_str = match.group(1)
        replacement = matched_str + "\n" + diagram
        # Check if diagram is already in this section to prevent duplicate injection
        if "class=\"mermaid\"" not in content[match.start():match.start()+500]:
            content = content.replace(matched_str, replacement, 1)
            modified = True
            print(f"Injected Mermaid diagram for Day {day}")
        else:
            print(f"Mermaid diagram already present for Day {day}, skipping.")
    else:
        print(f"Warning: Could not find theory section header for Day {day}")

if modified:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated week4.html with Mermaid diagrams!")
else:
    print("No changes made to week4.html")
