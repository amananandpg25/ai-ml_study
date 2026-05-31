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

# 1. Apply Styles
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
  color: var(--green);
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
  border-color: var(--green);
  color: var(--text);
  transform: translateY(-1px);
}
"""
content = content.replace("</style>", f"{extra_css}</style>")

# 2. Add favicon and description
favicon_html = """<meta name="description" content="Complete 135-day AI/ML roadmap from beginner to job-ready. Covers Python, ML, Deep Learning, NLP, Transformers, LLMs, and deployment.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%230d0f14'/><text x='4' y='23' font-family='monospace' font-size='16' font-weight='bold' fill='%234fd1a5'>AI</text></svg>">"""
content = content.replace("</title>", f"</title>\n{favicon_html}")

# 3. Add Theme Toggle Button
logo_block = """  <div class="sidebar-logo">
    <div class="logo-text">AI/ML Master<br>Roadmap 2026</div>
    <div class="logo-sub">135 DAYS · COMPLETE GUIDE</div>
  </div>"""
new_logo_block = """  <div class="sidebar-logo">
    <div style="display:flex;justify-content:space-between;align-items:center;width:100%">
      <div class="logo-text">AI/ML Master<br>Roadmap 2026</div>
      <button class="theme-btn" onclick="toggleTheme()" id="theme-btn" aria-label="Toggle dark/light mode" style="margin-left:auto">☀️ Light</button>
    </div>
    <div class="logo-sub">135 DAYS · COMPLETE GUIDE</div>
  </div>"""
content = content.replace(logo_block, new_logo_block)

# 4. Add Global Dashboard link
overview_sec = """  <div class="nav-section">
    <div class="nav-section-label">Overview</div>
    <div class="nav-item active" onclick="showSection('overview')">
      <span class="dot" style="background:#6c8cff"></span> Master Overview
    </div>
    <div class="nav-item" onclick="showSection('techstack')">
      <span class="dot" style="background:#4fd1a5"></span> Tech Stack
    </div>
  </div>"""
new_overview_sec = """  <div class="nav-section">
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
  </div>"""
content = content.replace(overview_sec, new_overview_sec)

# 5. Mapping for nav links
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
    "fin1": "week17.html"
}

for section_id, file_name in mapping.items():
    pattern = rf'(<div class="nav-item"\s+onclick="showSection\(\'{section_id}\'\)">)(.*?)(</div>)'
    def repl(m):
        _, inner, _ = m.groups()
        return f'<a class="nav-item" href="{file_name}" style="text-decoration:none">{inner}</a>'
    content = re.sub(pattern, repl, content)

content = re.sub(r'onclick="showSection\(\'([^\']*)\'\)"', r'onclick="showSection(\'\1\', this)', content)

# 6. Corrected Button Injection inside section-header
for section_id, file_name in mapping.items():
    # Target exactly the section header closing </div> right before .week-block
    sec_pattern = rf'(<div id="{section_id}"[^>]*>.*?<div class="section-header">.*?)(</div>\s*<div class="week-block)'
    
    week_num_str = re.search(r'\d+', file_name).group(0)
    btn_html = f'\n      <br><a href="{file_name}" class="start-week-btn">🚀 Open Week {week_num_str} Coursework →</a>'
    
    def sec_repl(m):
        return m.group(1) + btn_html + "\n    " + m.group(2)
        
    content, count = re.subn(sec_pattern, sec_repl, content, flags=re.DOTALL)
    print(f"  Injected button for {section_id} -> count={count}")

# 7. JavaScript showSection & toggleTheme functions
js_pattern = r'function showSection\(id\)\s*\{(.*?)\}'
new_js = """function showSection(id, el) {
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
});"""

content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

# Save changes
with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Roadmap buttons patching completed!")
