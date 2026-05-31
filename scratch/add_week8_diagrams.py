import re

with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ----------------- Day 52 replacements -----------------
print("Replacing Day 52 diagrams...")

# Replace bio vs artificial neuron mermaid diagram
# Let's inspect index or block and replace using regex
pattern_bio = re.compile(
    r'<div class="mermaid">\s*graph LR\s*subgraph BiologicalNeuron.*?subgraph ArtificialNeuron.*?out\["Output y_hat"\]\s*end\s*end\s*</div>',
    re.DOTALL
)

day52_neuron_svg = """<div class="callout" style="background:rgba(108,140,255,0.05);border:1px solid rgba(108,140,255,0.2);margin:1.5rem 0;padding:1.5rem;">
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
</div>"""

content, count1 = pattern_bio.subn(day52_neuron_svg, content)
print(f"  Replaced bio neuron diagram: {count1} occurrence(s)")

# Replace AND vs XOR separable mermaid diagram
pattern_separable = re.compile(
    r'<div class="mermaid">\s*graph TD\s*subgraph AND.*?subgraph XOR.*?MLP.*?end\s*end\s*</div>',
    re.DOTALL
)

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
</div>"""

content, count2 = pattern_separable.subn(day52_separability_svg, content)
print(f"  Replaced XOR separable diagram: {count2} occurrence(s)")

# ----------------- Day 53 replacements -----------------
print("Replacing Day 53 diagrams...")
day53_start = content.find('id="day-53"')
day54_start = content.find('id="day-54"')

if day53_start != -1 and day54_start != -1:
    day53_block = content[day53_start:day54_start]
    
    # Let's find the duplicate mermaid diagram inside Day 53
    # graph LR\n      Forward["Forward Pass: Inputs -> Loss"] ...
    pattern_dup = re.compile(r'<div class="mermaid">\s*graph LR\s*Forward\[.*?\]\s*--.*?-->\s*Update\[.*?\]\s*</div>', re.DOTALL)
    
    day53_mlp_svg = """<div class="callout" style="background:rgba(180,124,252,0.05);border:1px solid rgba(180,124,252,0.2);margin:1.5rem 0;padding:1.5rem;">
  <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--purple);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;text-align:center;">Multi-Layer Perceptron (MLP) Architecture</div>
  <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
    <svg viewBox="0 0 600 280" width="100%" height="auto" style="background:transparent;overflow:visible;">
      <defs>
        <filter id="glow-mlp" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#b47cfc" flood-opacity="0.3"/>
        </filter>
      </defs>

      <!-- Labels for Layers -->
      <text x="100" y="20" fill="var(--muted)" font-family="var(--font-head)" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">INPUT LAYER</text>
      <text x="300" y="20" fill="var(--blue)" font-family="var(--font-head)" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">HIDDEN LAYER (&fnof;)</text>
      <text x="500" y="20" fill="var(--green)" font-family="var(--font-head)" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1">OUTPUT LAYER</text>

      <!-- Draw connections first -->
      <g stroke="rgba(255,255,255,0.08)" stroke-width="1">
        <!-- Input 1 to Hidden -->
        <line x1="100" y1="70" x2="300" y2="50" />
        <line x1="100" y1="70" x2="300" y2="110" />
        <line x1="100" y1="70" x2="300" y2="170" />
        <line x1="100" y1="70" x2="300" y2="230" />
        <!-- Input 2 to Hidden -->
        <line x1="100" y1="140" x2="300" y2="50" />
        <line x1="100" y1="140" x2="300" y2="110" />
        <line x1="100" y1="140" x2="300" y2="170" />
        <line x1="100" y1="140" x2="300" y2="230" />
        <!-- Input 3 to Hidden -->
        <line x1="100" y1="210" x2="300" y2="50" />
        <line x1="100" y1="210" x2="300" y2="110" />
        <line x1="100" y1="210" x2="300" y2="170" />
        <line x1="100" y1="210" x2="300" y2="230" />
      </g>

      <!-- Hidden to Output -->
      <g stroke="rgba(108,140,255,0.2)" stroke-width="1.5">
        <line x1="300" y1="50" x2="500" y2="140" />
        <line x1="300" y1="110" x2="500" y2="140" />
        <line x1="300" y1="170" x2="500" y2="140" />
        <line x1="300" y1="230" x2="500" y2="140" />
      </g>

      <!-- Input Nodes -->
      <circle cx="100" cy="70" r="16" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="100" y="74" fill="var(--text)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">x₁</text>

      <circle cx="100" cy="140" r="16" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="100" y="144" fill="var(--text)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">x₂</text>

      <circle cx="100" cy="210" r="16" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="100" y="214" fill="var(--text)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">x₃</text>

      <!-- Hidden Nodes -->
      <circle cx="300" cy="50" r="18" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2" />
      <text x="300" y="54" fill="var(--blue)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">h₁</text>

      <circle cx="300" cy="110" r="18" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2" />
      <text x="300" y="114" fill="var(--blue)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">h₂</text>

      <circle cx="300" cy="170" r="18" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2" />
      <text x="300" y="174" fill="var(--blue)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">h₃</text>

      <circle cx="300" cy="230" r="18" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2" />
      <text x="300" y="234" fill="var(--blue)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">h₄</text>

      <!-- Output Node -->
      <circle cx="500" cy="140" r="22" fill="var(--bg3)" stroke="var(--green)" stroke-width="2.5" filter="url(#glow-mlp)" />
      <text x="500" y="144" fill="var(--green)" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle">y&#770;</text>
    </svg>
  </div>
</div>"""

    new_day53_block, count3 = pattern_dup.subn(day53_mlp_svg, day53_block)
    content = content.replace(day53_block, new_day53_block)
    print(f"  Replaced duplicate diagram in Day 53: {count3} occurrence(s)")
else:
    print("  Day 53 or 54 bounds not found!")

# ----------------- Day 54 replacements -----------------
print("Replacing Day 54 diagrams...")
day54_start = content.find('id="day-54"')
# Day 54 is the last day in week8.html, so we search up to resources or script
day54_end = content.find('id="day-55"')
if day54_end == -1:
    day54_end = content.find('</main>')

if day54_start != -1 and day54_end != -1:
    day54_block = content[day54_start:day54_end]
    
    pattern_dup54 = re.compile(r'<div class="mermaid">\s*graph LR\s*Forward\[.*?\]\s*--.*?-->\s*Update\[.*?\]\s*</div>', re.DOTALL)
    
    day54_backprop_svg = """<div class="callout" style="background:rgba(229,107,140,0.05);border:1px solid rgba(229,107,140,0.2);margin:1.5rem 0;padding:1.5rem;">
  <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--pink);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;text-align:center;">Backpropagation Dual-Dataflow</div>
  <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
    <svg viewBox="0 0 600 240" width="100%" height="auto" style="background:transparent;overflow:visible;">
      <defs>
        <filter id="glow-pink" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#ff4d6d" flood-opacity="0.3"/>
        </filter>
        <filter id="glow-blue-f" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#6c8cff" flood-opacity="0.3"/>
        </filter>
      </defs>

      <!-- Nodes -->
      <circle cx="80" cy="120" r="20" fill="var(--bg3)" stroke="var(--border)" stroke-width="2" />
      <text x="80" y="124" fill="var(--text)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Input X</text>

      <circle cx="260" cy="120" r="24" fill="var(--bg3)" stroke="var(--blue)" stroke-width="2" />
      <text x="260" y="124" fill="var(--blue)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Hidden H</text>

      <circle cx="420" cy="120" r="24" fill="var(--bg3)" stroke="var(--green)" stroke-width="2" />
      <text x="420" y="124" fill="var(--green)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Output Ŷ</text>

      <circle cx="530" cy="120" r="18" fill="var(--bg3)" stroke="var(--pink)" stroke-width="2" />
      <text x="530" y="124" fill="var(--pink)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Loss L</text>

      <!-- 1. Forward Pass -->
      <path d="M 105 105 Q 170 85 230 105" fill="none" stroke="#6c8cff" stroke-width="2.5" filter="url(#glow-blue-f)" />
      <polygon points="230,105 220,100 224,108" fill="#6c8cff" />
      
      <path d="M 285 105 Q 340 85 390 105" fill="none" stroke="#6c8cff" stroke-width="2.5" filter="url(#glow-blue-f)" />
      <polygon points="390,105 380,100 384,108" fill="#6c8cff" />

      <path d="M 445 110 Q 480 100 510 112" fill="none" stroke="#6c8cff" stroke-width="2" />
      <polygon points="510,112 500,108 504,115" fill="#6c8cff" />

      <text x="260" y="60" fill="#6c8cff" font-family="var(--font-head)" font-size="10" font-weight="700" text-anchor="middle">FORWARD PASS (ACTIVATE)</text>

      <!-- 2. Backward Pass -->
      <path d="M 510 130 Q 480 140 445 130" fill="none" stroke="#ff4d6d" stroke-width="2.5" filter="url(#glow-pink)" />
      <polygon points="445,130 455,135 451,127" fill="#ff4d6d" />

      <path d="M 390 135 Q 340 155 285 135" fill="none" stroke="#ff4d6d" stroke-width="2.5" filter="url(#glow-pink)" />
      <polygon points="285,135 295,140 291,132" fill="#ff4d6d" />

      <path d="M 235 135 Q 170 155 105 135" fill="none" stroke="#ff4d6d" stroke-width="2.5" filter="url(#glow-pink)" />
      <polygon points="105,135 115,140 111,132" fill="#ff4d6d" />

      <text x="260" y="195" fill="#ff4d6d" font-family="var(--font-head)" font-size="10" font-weight="700" text-anchor="middle">BACKWARD PASS (CHAIN RULE)</text>

      <!-- Math annotations -->
      <text x="475" y="160" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">&part;L/&part;Y&#770;</text>
      <text x="335" y="175" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">&part;L/&part;H = &part;L/&part;Y&#770; &middot; &part;Y&#770;/&part;H</text>
      <text x="170" y="175" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">&part;L/&part;X = &part;L/&part;H &middot; &part;H/&part;X</text>
    </svg>
  </div>
</div>"""
    
    new_day54_block, count4 = pattern_dup54.subn(day54_backprop_svg, day54_block)
    content = content.replace(day54_block, new_day54_block)
    print(f"  Replaced duplicate diagram in Day 54: {count4} occurrence(s)")
else:
    print("  Day 54 bounds not found!")

# Save back to file
with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week8.html")
