with open('/Users/amananand/Downloads/SDE/ai:ml/week3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to find the first occurrence of:
# rs = RobustScaler()
# data_rob = rs.fit_transform(data)
# and then find the closing </pre>\n  </div> that comes right after it.

import re
pattern = re.compile(
    r'rs\s*=\s*RobustScaler\(\)\s*[\r\n]+'
    r'data_rob\s*=\s*rs\.fit_transform\(data\)\s*[\r\n]+'
    r'.*?</pre>\s*</div>',
    re.DOTALL
)

match = pattern.search(content)
if match:
    matched_text = match.group(0)
    print("Found match:")
    print(repr(matched_text))
    
    # Let's append our SVG diagram after it
    replacement = matched_text + """

  <div class="callout" style="background:rgba(180,124,252,0.05);border:1px solid rgba(180,124,252,0.2);margin:1.5rem 0;">
    <div style="font-family:var(--font-head);font-weight:700;font-size:13px;color:var(--purple);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.5px;">Visualizing scaling transformations</div>
    <div style="display:flex;justify-content:center;align-items:center;background:var(--bg2);padding:1.5rem;border-radius:8px;border:1px solid var(--border);">
      <svg viewBox="0 0 700 220" width="100%" height="auto" style="background:transparent;overflow:visible;">
        <defs>
          <filter id="glow-purple" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#b47cfc" flood-opacity="0.3"/>
          </filter>
          <filter id="glow-green" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#4fd1a5" flood-opacity="0.3"/>
          </filter>
          <filter id="glow-orange" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#f7a94b" flood-opacity="0.3"/>
          </filter>
        </defs>

        <!-- 1. Raw Distribution -->
        <g transform="translate(10, 20)">
          <text x="90" y="20" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">1. Raw Data (Skewed / Varying)</text>
          <line x1="20" y1="140" x2="160" y2="140" stroke="var(--border)" stroke-width="1.5" />
          <line x1="20" y1="40" x2="20" y2="140" stroke="var(--border)" stroke-width="1" stroke-dasharray="2 2" />
          <path d="M 20 140 Q 60 40 100 110 T 160 140" fill="none" stroke="#f7a94b" stroke-width="3" filter="url(#glow-orange)" />
          <text x="20" y="155" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Min (e.g. 20)</text>
          <text x="160" y="155" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Max (e.g. 200k)</text>
        </g>

        <!-- Arrow 1 -->
        <g transform="translate(195, 20)">
          <line x1="0" y1="70" x2="30" y2="70" stroke="var(--border)" stroke-width="2" />
          <path d="M 20 65 L 30 70 L 20 75 Z" fill="var(--border)" />
        </g>

        <!-- 2. StandardScaler Output -->
        <g transform="translate(245, 20)">
          <text x="90" y="20" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">2. StandardScaler</text>
          <line x1="20" y1="140" x2="160" y2="140" stroke="var(--border)" stroke-width="1.5" />
          <line x1="90" y1="35" x2="90" y2="140" stroke="rgba(79, 209, 165, 0.4)" stroke-dasharray="3 3" stroke-width="1" />
          <path d="M 20 140 Q 90 30 160 140" fill="none" stroke="#4fd1a5" stroke-width="3" filter="url(#glow-green)" />
          <text x="90" y="155" fill="#4fd1a5" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Mean = 0</text>
          <text x="25" y="155" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">-3 &sigma;</text>
          <text x="155" y="155" fill="var(--muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">+3 &sigma;</text>
        </g>

        <!-- Arrow 2 -->
        <g transform="translate(430, 20)">
          <line x1="0" y1="70" x2="30" y2="70" stroke="var(--border)" stroke-width="2" />
          <path d="M 20 65 L 30 70 L 20 75 Z" fill="var(--border)" />
        </g>

        <!-- 3. MinMaxScaler Output -->
        <g transform="translate(480, 20)">
          <text x="90" y="20" fill="var(--text)" font-family="var(--font-head)" font-size="12" font-weight="700" text-anchor="middle">3. MinMaxScaler</text>
          <line x1="20" y1="140" x2="160" y2="140" stroke="var(--border)" stroke-width="1.5" />
          <line x1="30" y1="40" x2="30" y2="140" stroke="rgba(180, 124, 252, 0.3)" stroke-width="1" stroke-dasharray="2 2" />
          <line x1="150" y1="40" x2="150" y2="140" stroke="rgba(180, 124, 252, 0.3)" stroke-width="1" stroke-dasharray="2 2" />
          <path d="M 30 140 Q 70 40 100 110 T 150 140" fill="none" stroke="#b47cfc" stroke-width="3" filter="url(#glow-purple)" />
          <text x="30" y="155" fill="#b47cfc" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Min = 0</text>
          <text x="150" y="155" fill="#b47cfc" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Max = 1</text>
        </g>
      </svg>
    </div>
  </div>"""
    
    content = content.replace(matched_text, replacement)
    with open('/Users/amananand/Downloads/SDE/ai:ml/week3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added side-by-side distribution diagram using regex!")
else:
    print("Pattern not matched!")
