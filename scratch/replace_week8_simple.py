with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Biological vs Artificial Neuron replacement
print("Replacing neuron diagram...")
bio_start = content.find('<div class="mermaid">\n      graph LR\n      subgraph BiologicalNeuron')
bio_end = content.find('<div class="diagram-cap">Biological inspiration → mathematical model</div>')

if bio_start != -1 and bio_end != -1:
    old_part1 = content[bio_start:bio_end + len('<div class="diagram-cap">Biological inspiration → mathematical model</div>')]
    
    new_part1 = """<div class="callout" style="background:rgba(108,140,255,0.05);border:1px solid rgba(108,140,255,0.2);margin:1.5rem 0;padding:1.5rem;">
  <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--blue);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;text-align:center;">Artificial Neuron Model (The Perceptron)</div>
  <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
    <svg viewBox="0 0 600 240" width="100%" height="auto" style="background:transparent;overflow:visible;">
      <defs>
        <filter id="glow-neuron" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#4fd1a5" flood-opacity="0.3"/>
        </filter>
      </defs>

      <!-- Input Nodes -->
      <circle cx="80" cy="60" r="20" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="80" y="64" fill="var(--text)" font-family="var(--font-mono)" font-size="12" text-anchor="middle">x₁</text>

      <circle cx="80" cy="120" r="20" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="80" y="124" fill="var(--text)" font-family="var(--font-mono)" font-size="12" text-anchor="middle">x₂</text>

      <circle cx="80" cy="180" r="20" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="80" y="184" fill="var(--text)" font-family="var(--font-mono)" font-size="12" text-anchor="middle">x₃</text>

      <!-- Bias Node -->
      <circle cx="200" cy="40" r="16" fill="var(--bg3)" stroke="var(--border)" stroke-width="1.5" />
      <text x="200" y="44" fill="var(--orange)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">+b</text>

      <!-- Summation Node (Sigma) -->
      <circle cx="280" cy="120" r="30" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2.5" />
      <text x="280" y="125" fill="var(--blue)" font-family="var(--font-head)" font-size="22" text-anchor="middle">&Sigma;</text>
      <text x="280" y="165" fill="var(--muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">z = w·x + b</text>

      <!-- Activation Function Node (f) -->
      <circle cx="420" cy="120" r="30" fill="var(--bg3)" stroke="var(--green)" stroke-width="2.5" filter="url(#glow-neuron)" />
      <text x="420" y="125" fill="var(--green)" font-family="var(--font-head)" font-size="20" text-anchor="middle">&fnof;(z)</text>
      <text x="420" y="165" fill="var(--muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Step / Sigmoid</text>

      <!-- Output Indicator -->
      <line x1="450" y1="120" x2="520" y2="120" stroke="var(--green)" stroke-width="2" />
      <polygon points="520,116 530,120 520,124" fill="var(--green)" />
      <text x="545" y="124" fill="var(--green)" font-family="var(--font-mono)" font-size="13" font-weight="700">y&#770;</text>

      <!-- Connection Lines with weight labels -->
      <line x1="100" y1="60" x2="250" y2="120" stroke="var(--border)" stroke-width="1.5" />
      <text x="170" y="80" fill="var(--muted)" font-family="var(--font-mono)" font-size="10">w₁</text>

      <line x1="100" y1="120" x2="250" y2="120" stroke="var(--border)" stroke-width="1.5" />
      <text x="170" y="115" fill="var(--muted)" font-family="var(--font-mono)" font-size="10">w₂</text>

      <line x1="100" y1="180" x2="250" y2="120" stroke="var(--border)" stroke-width="1.5" />
      <text x="170" y="160" fill="var(--muted)" font-family="var(--font-mono)" font-size="10">w₃</text>

      <!-- Bias connection -->
      <line x1="216" y1="46" x2="265" y2="95" stroke="var(--border)" stroke-width="1" stroke-dasharray="3 3" />

      <!-- Connection between Sigma and f(z) -->
      <line x1="310" y1="120" x2="390" y2="120" stroke="var(--blue)" stroke-width="2" />
      <polygon points="385,116 395,120 385,124" fill="var(--blue)" />
    </svg>
  </div>
</div>
<div class="diagram-cap">Biological inspiration &rarr; mathematical artificial neuron</div>"""
    
    content = content.replace(old_part1, new_part1)
    print("  Replaced bio neuron diagram successfully!")
else:
    print("  Could not find indices for bio neuron diagram!")

# 2. Separability (AND vs XOR) replacement
print("Replacing XOR separable diagram...")
sep_start = content.find('<div class="mermaid">\n      graph TD\n      subgraph AND')
sep_end = content.find('<div class="diagram-cap">The XOR problem — the original motivation for multi-layer networks</div>')

if sep_start != -1 and sep_end != -1:
    old_part2 = content[sep_start:sep_end + len('<div class="diagram-cap">The XOR problem — the original motivation for multi-layer networks</div>')]
    
    day52_separability_svg = """<div class="callout" style="background:rgba(247,169,75,0.05);border:1px solid rgba(247,169,75,0.2);margin:1.5rem 0;padding:1.5rem;">
  <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--orange);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;text-align:center;">Linear Separability: AND vs XOR</div>
  <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
    <svg viewBox="0 0 600 240" width="100%" height="auto" style="background:transparent;overflow:visible;">
      <!-- AND gate plot -->
      <g transform="translate(40, 20)">
        <text x="110" y="10" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">AND Gate (Separable)</text>
        <line x1="30" y1="180" x2="190" y2="180" stroke="var(--border)" stroke-width="1.5" />
        <line x1="30" y1="40" x2="30" y2="180" stroke="var(--border)" stroke-width="1.5" />
        
        <circle cx="50" cy="160" r="8" fill="var(--pink)" />
        <text x="50" y="180" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="middle">(0,0)</text>
        
        <circle cx="50" cy="70" r="8" fill="var(--pink)" />
        <text x="42" y="74" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="end">(0,1)</text>

        <circle cx="140" cy="160" r="8" fill="var(--pink)" />
        <text x="140" y="180" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="middle">(1,0)</text>

        <circle cx="140" cy="70" r="8" fill="var(--green)" />
        <text x="148" y="74" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="start">(1,1)</text>

        <line x1="90" y1="40" x2="180" y2="130" stroke="#f7a94b" stroke-width="2.5" stroke-dasharray="3 3" />
        <text x="150" y="55" fill="#f7a94b" font-family="var(--font-mono)" font-size="9">Decision Boundary</text>
      </g>

      <!-- XOR gate plot -->
      <g transform="translate(340, 20)">
        <text x="110" y="10" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">XOR Gate (Non-Separable)</text>
        <line x1="30" y1="180" x2="190" y2="180" stroke="var(--border)" stroke-width="1.5" />
        <line x1="30" y1="40" x2="30" y2="180" stroke="var(--border)" stroke-width="1.5" />
        
        <circle cx="50" cy="160" r="8" fill="var(--pink)" />
        <text x="50" y="180" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="middle">(0,0)</text>
        
        <circle cx="50" cy="70" r="8" fill="var(--green)" />
        <text x="42" y="74" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="end">(0,1)</text>

        <circle cx="140" cy="160" r="8" fill="var(--green)" />
        <text x="140" y="180" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="middle">(1,0)</text>

        <circle cx="140" cy="70" r="8" fill="var(--pink)" />
        <text x="148" y="74" fill="var(--muted)" font-family="var(--font-mono)" font-size="8" text-anchor="start">(1,1)</text>

        <path d="M 35 110 Q 95 125 155 110" fill="none" stroke="var(--pink)" stroke-width="1" stroke-dasharray="2 2" />
        <text x="100" y="145" fill="var(--pink)" font-family="var(--font-body)" font-size="9" text-anchor="middle" font-weight="600">No single straight line separates</text>
      </g>
    </svg>
  </div>
</div>
<div class="diagram-cap">The XOR problem &mdash; the original motivation for hidden layers & multi-layer networks</div>"""
    
    content = content.replace(old_part2, day52_separability_svg)
    print("  Replaced XOR separable diagram successfully!")
else:
    print("  Could not find indices for XOR separable diagram!")

with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished Simple Replacement for week8.html")
