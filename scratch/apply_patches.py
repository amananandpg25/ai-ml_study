import os
import re
import shutil

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
backup_dir = os.path.join(base_dir, "_backup_gemini")
os.makedirs(backup_dir, exist_ok=True)

DAYS_MAP = {
    1: [1, 2, 3, 4, 5, 6, 7],
    2: [8, 9, 10, 11, 12, 13, 14],
    3: [15, 16, 17, 18, 19, 20, 21],
    4: [22, 23, 24, 25, 26, 27, 28, 29, 30],
    5: [31, 32, 33, 34, 35, 36, 37],
    6: [38, 39, 40, 41, 42, 43, 44],
    7: [45, 46, 47, 48, 49, 50, 51],
    8: [52, 53, 54, 55, 56, 57, 58],
    9: [59, 60, 61, 62, 63, 64, 65],
    10: [66, 67, 68, 69, 70, 71, 72],
    11: [73, 74, 75, 76, 77, 78, 79],
    12: [80, 81, 82, 83, 84, 85, 86],
    13: [87, 88, 89, 90, 91, 92, 93],
    14: [94, 95, 96, 97, 98, 99, 100],
    15: [101, 102, 103, 104, 105, 106, 107],
    16: [108, 109, 110, 111, 112, 113, 114, 115, 116, 117],
    17: [118, 119, 120, 121, 122, 123, 124],
    18: [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
}

def patch_styles(content, week_num):
    if ":focus-visible" not in content:
        extra_css = """
/* ── FOCUS VISIBLE ── */
:focus-visible{outline:2px solid var(--green);outline-offset:2px;border-radius:4px;}

/* ── DARK/LIGHT MODE ── */
[data-theme="light"]:root,[data-theme="light"]{
  --bg:#f5f7fa; --bg2:#eaedf3; --bg3:#dde2ee; --card:#ffffff;
  --border:#c8cedc; --text:#1a1f35; --muted:#6b7590;
}
[data-theme="light"] .cb{background:#1a1e2e}
[data-theme="light"] .cb pre{color:#c9d1e0}
.theme-btn{background:none;border:1px solid var(--border);color:var(--muted);font-family:var(--font-mono);font-size:11px;padding:3px 9px;border-radius:20px;cursor:pointer;transition:all .2s;white-space:nowrap}
.theme-btn:hover{border-color:var(--blue);color:var(--blue)}

/* ── XP LEVEL BADGE ── */
.level-badge{font-family:var(--font-mono);font-size:10px;padding:2px 8px;border-radius:20px;border:1px solid rgba(180,124,252,.4);color:var(--purple);white-space:nowrap}

/* ── WEEK NAVIGATION ── */
.week-nav-links{display:flex;gap:.6rem;padding:.8rem 1.1rem;margin-top:auto;border-top:1px solid var(--border)}
.week-nav-btn{display:flex;align-items:center;gap:.4rem;font-size:11px;color:var(--muted);text-decoration:none;border:1px solid var(--border);padding:4px 8px;border-radius:6px;transition:all var(--transition);flex:1;justify-content:center}
.week-nav-btn:hover{color:var(--green);border-color:var(--green)}

/* ── PRINT ── */
@media print{
  body{background:#fff;color:#000;font-size:12px}
  .topnav,.sidebar,.complete-btn,.xp-toast,.mob-menu-btn,.theme-btn{display:none!important}
  .layout{display:block}
  .day-section{display:block!important;padding:1rem 0;page-break-after:always}
  .cb{background:#f5f5f5;border:1px solid #ccc;color:#000}
  .cb pre,.kw,.fn,.str,.num,.cm,.bi,.op{color:#000!important}
  .callout,.misconception,.ml-connect,.analogy,.hinglish{border-left:3px solid #999;background:#f9f9f9}
}
"""
        content = content.replace("</style>", f"{extra_css}</style>")
    return content

def fix_xp_buttons(content, week_num):
    # Regex to find buttons like: <button class="complete-btn" id="btn-day-D" onclick="completeDay(D, X)">...Claim Y XP...</button>
    pattern = r'(<button class="complete-btn" id="btn-day-(\d+)" onclick="completeDay\(\d+,\s*)(\d+)(\)">.*?Claim\s+)(\d+)(\s+XP.*?</button>)'
    def repl(m):
        prefix, day_num, param_xp, mid, text_xp, suffix = m.groups()
        if param_xp != text_xp:
            print(f"  Fixing XP mismatch (Claim) for Day {day_num} in Week {week_num}: param={param_xp}, text={text_xp} -> changing param to {text_xp}")
            return f"{prefix}{text_xp}{mid}{text_xp}{suffix}"
        return m.group(0)
    content = re.sub(pattern, repl, content)
    
    # Also for "Earn"
    pattern2 = r'(<button class="complete-btn" id="btn-day-(\d+)" onclick="completeDay\(\d+,\s*)(\d+)(\)">.*?Earn\s+)(\d+)(\s+XP.*?</button>)'
    def repl2(m):
        prefix, day_num, param_xp, mid, text_xp, suffix = m.groups()
        if param_xp != text_xp:
            print(f"  Fixing XP mismatch (Earn) for Day {day_num} in Week {week_num}: param={param_xp}, text={text_xp} -> changing param to {text_xp}")
            return f"{prefix}{text_xp}{mid}{text_xp}{suffix}"
        return m.group(0)
    content = re.sub(pattern2, repl2, content)
    return content

def clean_and_add_aria(tag_html, role=None, tabindex=None, onkeydown=None, aria_expanded=None):
    # Remove existing attributes to prevent duplicates
    if role:
        tag_html = re.sub(r'\s*role=["\'][^"\']*["\']', '', tag_html)
    if tabindex:
        tag_html = re.sub(r'\s*tabindex=["\'][^"\']*["\']', '', tag_html)
    if onkeydown:
        tag_html = re.sub(r'\s*onkeydown=["\'][^"\']*["\']', '', tag_html)
    if aria_expanded:
        tag_html = re.sub(r'\s*aria-expanded=["\'][^"\']*["\']', '', tag_html)
        
    # Inject new attributes right before the closing '>' of the tag
    attrs = []
    if role:
        attrs.append(f'role="{role}"')
    if tabindex:
        attrs.append(f'tabindex="{tabindex}"')
    if onkeydown:
        attrs.append(f'onkeydown="{onkeydown}"')
    if aria_expanded:
        attrs.append(f'aria-expanded="{aria_expanded}"')
        
    attrs_str = " " + " ".join(attrs)
    if tag_html.endswith('/>'):
        return tag_html[:-2] + attrs_str + '/>'
    elif tag_html.endswith('>'):
        return tag_html[:-1] + attrs_str + '>'
    return tag_html

def patch_html_body(content, week_num, days):
    # 1. Favicon + description
    if "rel=\"icon\"" not in content:
        title_m = re.search(r"<title>(.*?)</title>", content)
        title_text = title_m.group(1) if title_m else f"Week {week_num} Coursework"
        simple_title = title_text.split('|')[0].strip()
        meta_desc = f"{simple_title} — Complete coursework, tasks, quizzes, and resources for Week {week_num} of the 135-Day AI/ML Roadmap."
        
        favicon_html = f"""<meta name="description" content="{meta_desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%230d0f14'/><text x='4' y='23' font-family='monospace' font-size='16' font-weight='bold' fill='%234fd1a5'>AI</text></svg>">"""
        content = content.replace("</title>", f"</title>\n{favicon_html}")

    # 2. Level show element in topnav-left
    if "level-show" not in content:
        streak_pattern = r'(<div class="streak-display"[^>]*>.*?</div>)'
        if re.search(streak_pattern, content):
            content = re.sub(streak_pattern, r'\1\n    <div class="level-badge" id="level-show">🌱 Beginner</div>', content)
        else:
            xp_pattern = r'(<div class="xp-display"[^>]*>.*?</div>)'
            content = re.sub(xp_pattern, r'\1\n    <div class="level-badge" id="level-show">🌱 Beginner</div>', content)

    # 3. Theme toggle button in topnav
    if 'id="theme-btn"' not in content:
        nav_close_idx = content.find("</nav>")
        if nav_close_idx != -1:
            theme_btn_html = '\n  <button class="theme-btn" onclick="toggleTheme()" id="theme-btn" aria-label="Toggle dark/light mode">☀️ Light</button>\n'
            content = content[:nav_close_idx] + theme_btn_html + content[nav_close_idx:]

    # 4. ARIA attributes for topnav
    content = re.sub(r'<nav class="topnav"([^>]*)(?<!role="navigation")>', r'<nav class="topnav"\1 role="navigation" aria-label="Week navigation">', content)
    content = re.sub(r'class="prog-outer"([^>]*)', r'class="prog-outer"\1 role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Week progress"', content)
    content = re.sub(r'class="day-pills"([^>]*)', r'class="day-pills"\1 role="tablist" aria-label="Day selector"', content)
    
    def day_pill_repl(m):
        tag = m.group(0)
        day_match = re.search(r'onclick="goDay\((\d+)\)"', tag)
        if not day_match:
            return tag
        d = int(day_match.group(1))
        is_active = 'active' in tag
        aria_sel = "true" if is_active else "false"
        
        # Clean up existing attributes
        tag = re.sub(r'\s*role=["\'][^"\']*["\']', '', tag)
        tag = re.sub(r'\s*aria-selected=["\'][^"\']*["\']', '', tag)
        tag = re.sub(r'\s*tabindex=["\'][^"\']*["\']', '', tag)
        tag = re.sub(r'\s*onkeydown=["\'][^"\']*["\']', '', tag)
        
        attrs_str = f' role="tab" aria-selected="{aria_sel}" tabindex="0" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay({d})"'
        if tag.endswith('>'):
            return tag[:-1] + attrs_str + '>'
        return tag
    content = re.sub(r'<div class="day-pill[^>]*>', day_pill_repl, content)

    # 5. ARIA menu button
    if 'id="sidebar-toggle"' not in content:
        content = re.sub(r'class="mob-menu-btn"\s+onclick="toggleSidebar\(\)"', r'class="mob-menu-btn" onclick="toggleSidebar()" aria-label="Toggle navigation menu" aria-expanded="false" id="sidebar-toggle"', content)

    # 6. Sidebar ARIA and nav buttons
    content = re.sub(r'<aside class="sidebar"([^>]*)(?<!role="complementary")>', r'<aside class="sidebar"\1 role="complementary" aria-label="Sidebar navigation">', content)

    def sb_item_repl(m):
        tag = m.group(0)
        day_match = re.search(r'onclick="goDay\((\d+)\)[^"]*"', tag)
        if not day_match:
            return tag
        d = int(day_match.group(1))
        
        # Clean up existing attributes
        tag = re.sub(r'\s*role=["\'][^"\']*["\']', '', tag)
        tag = re.sub(r'\s*tabindex=["\'][^"\']*["\']', '', tag)
        tag = re.sub(r'\s*onkeydown=["\'][^"\']*["\']', '', tag)
        
        attrs_str = f' role="button" tabindex="0" onkeydown="if(event.key===\'Enter\')goDay({d})"'
        if tag.endswith('>'):
            return tag[:-1] + attrs_str + '>'
        return tag
    content = re.sub(r'<div class="sb-item[^>]*>', sb_item_repl, content)

    # 7. Sidebar week navigation links
    # Remove existing week navigation block to force-update
    content = re.sub(r'<div class="week-nav-links">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="sb-divider"></div>\s*<div class="sb-label">Navigate</div>', '', content)
    
    prev_link = f'<a class="week-nav-btn" href="week{week_num-1}.html" aria-label="Go to Week {week_num-1}">← Week {week_num-1}</a>' if week_num > 1 else ''
    next_link = f'<a class="week-nav-btn" href="week{week_num+1}.html" aria-label="Go to Week {week_num+1}">Week {week_num+1} →</a>' if week_num < 18 else ''
    
    nav_html = f"""  <div class="sb-divider"></div>
  <div class="sb-label">Navigate</div>
  <div class="week-nav-links">
    <a class="week-nav-btn" href="roadmap.html" aria-label="Back to Roadmap">🗺 Roadmap</a>
    <a class="week-nav-btn" href="dashboard.html" aria-label="Open Dashboard">📊 Dashboard</a>
    <a class="week-nav-btn" href="resources.html" aria-label="Open Resources">📚 Resources</a>
    {prev_link}
    {next_link}
  </div>"""
    
    aside_close_idx = content.find("</aside>")
    if aside_close_idx != -1:
        content = content[:aside_close_idx] + nav_html + "\n" + content[aside_close_idx:]

    # 8. Quiz option ARIA attributes & onclick cleanup
    def quiz_opt_repl(m):
        tag = m.group(0)
        if 'onclick=' in tag:
            # Clean up double onclick issue if present: onclick="quiz-opt" onclick="..."
            tag = tag.replace('onclick="quiz-opt" ', '')
            return clean_and_add_aria(tag, role="button", tabindex="0", onkeydown="if(event.key===\'Enter\'||event.key===\' \')this.click()")
        return tag
    content = re.sub(r'<div class="quiz-opt"[^>]*>', quiz_opt_repl, content)

    # 9. Task headers ARIA attributes
    def task_header_repl(m):
        tag = m.group(0)
        if 'onclick=' in tag:
            return clean_and_add_aria(tag, role="button", tabindex="0", onkeydown="if(event.key===\'Enter\'||event.key===\' \')this.click()", aria_expanded="false")
        return tag
    content = re.sub(r'<div class="task-header"[^>]*>', task_header_repl, content)

    return content

def replace_script_block(content, week_num, days):
    pattern = r'<script[^>]*>(?:(?!</script>).)*?completeDay(?:(?!</script>).)*?</script>'
    days_str = ",".join(map(str, days))
    
    migration_js = ""
    if week_num == 1:
        migration_js = """
function migrateLegacy() {
  if (!localStorage.getItem('w1-state')) {
    const legacyXP   = parseInt(localStorage.getItem('w1-xp') || '0');
    const legacyDone = JSON.parse(localStorage.getItem('w1-done') || '[]');
    const legacyStr  = parseInt(localStorage.getItem('w1-streak') || '0');
    const legacyDate = localStorage.getItem('w1-lastdate') || '';
    if (legacyXP || legacyDone.length) {
      localStorage.setItem('w1-state', JSON.stringify({ xp: legacyXP, done: legacyDone, streak: legacyStr, lastDate: legacyDate }));
    }
    ['w1-xp','w1-done','w1-streak','w1-lastdate'].forEach(k => localStorage.removeItem(k));
  }
}
"""
    elif week_num == 2:
        migration_js = """
function migrateLegacy() {
  if (!localStorage.getItem('w2-state')) {
    const legacyXP   = parseInt(localStorage.getItem('w2_xp') || '0');
    const legacyDone = JSON.parse(localStorage.getItem('w2_done') || '[]');
    const legacyStr  = parseInt(localStorage.getItem('w2_streak') || '0');
    const legacyDate = localStorage.getItem('w2_lastDate') || '';
    if (legacyXP || legacyDone.length) {
      localStorage.setItem('w2-state', JSON.stringify({ xp: legacyXP, done: legacyDone, streak: legacyStr, lastDate: legacyDate }));
    }
    ['w2_xp','w2_done','w2_streak','w2_lastDate'].forEach(k => localStorage.removeItem(k));
  }
}
"""

    migration_call = "migrateLegacy();" if (week_num in [1, 2]) else ""

    new_script = f"""<script>
// ═══════════════════════════════════════════
//  WEEK {week_num} — STATE & GAMIFICATION ENGINE
// ═══════════════════════════════════════════
const WEEK = {week_num};
const DAYS = [{days_str}];

{migration_js}

{migration_call}

let state = JSON.parse(localStorage.getItem(`w${{WEEK}}-state`) || '{{}}');
state.xp     = state.xp     || 0;
state.streak = state.streak || 0;
state.done   = state.done   || [];
state.lastDate= state.lastDate || '';

function saveState() {{ localStorage.setItem(`w${{WEEK}}-state`, JSON.stringify(state)); }}

const LEVELS = [
  {{ min:0,    label:'🌱 Beginner' }},
  {{ min:500,  label:'🔍 Explorer' }},
  {{ min:1500, label:'⚙️ Practitioner' }},
  {{ min:3000, label:'🤖 Engineer' }},
  {{ min:6000, label:'🧠 Expert' }},
  {{ min:10000,label:'🚀 Master' }}
];
function getLevel(xp) {{
  for (let i = LEVELS.length - 1; i >= 0; i--) {{
    if (xp >= LEVELS[i].min) return LEVELS[i].label;
  }}
  return LEVELS[0].label;
}}

function syncUI() {{
  document.getElementById('xp-show').textContent   = `⚡ ${{state.xp}} XP`;
  document.getElementById('streak-show').textContent = `🔥 ${{state.streak}} day streak`;
  document.getElementById('sb-xp').textContent     = `${{state.xp}} XP earned`;
  document.getElementById('sb-streak').textContent  = `${{state.streak}} day streak`;
  const lvlEl = document.getElementById('level-show');
  if (lvlEl) lvlEl.textContent = getLevel(state.xp || 0);

  const pct = Math.round((state.done.length / DAYS.length) * 100);
  const progBar = document.getElementById('prog-bar');
  if (progBar) {{
    progBar.style.width = pct + '%';
    progBar.parentElement.setAttribute('aria-valuenow', pct);
  }}
  const progText = document.getElementById('prog-text');
  if (progText) progText.textContent = `${{state.done.length}}/${{DAYS.length}} days`;

  DAYS.forEach(d => {{
    const pill = document.getElementById('pill-' + d);
    const sb   = document.getElementById('sb-' + d);
    const btn  = document.getElementById('btn-day-' + d);
    if (state.done.includes(d)) {{
      pill && pill.classList.add('done');
      sb && sb.classList.add('done');
      if (btn) {{ btn.classList.add('done'); btn.textContent = '✓ Day ' + d + ' Complete'; }}
    }}
  }});
}}

function completeDay(day, xp) {{
  if (state.done.includes(day)) return;
  state.done.push(day);
  state.xp += xp;
  const today = new Date().toDateString();
  const yesterday = new Date(Date.now() - 86400000).toDateString();
  if (state.lastDate !== today) {{
    if (state.lastDate === yesterday) {{ state.streak++; }}
    else {{ state.streak = 1; }}
    state.lastDate = today;
  }}
  saveState();
  syncUI();
  showXPToast(xp, day);
  const btn = document.getElementById('btn-day-' + day);
  if (btn) {{ btn.classList.add('done'); btn.textContent = '✓ Day ' + day + ' Complete'; }}
}}

function showXPToast(xp, day) {{
  const t = document.getElementById('xp-toast');
  if (t) {{
    t.textContent = `+${{xp}} XP ⚡ — Day ${{day}} Complete!`;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
  }}
}}

function goDay(n) {{
  document.querySelectorAll('.day-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.sb-item').forEach(i => i.classList.remove('active'));
  document.querySelectorAll('.day-pill').forEach(p => {{ p.classList.remove('active'); p.setAttribute('aria-selected','false'); }});
  const section = document.getElementById('day-' + n);
  if (section) {{ section.classList.add('active'); }}
  const sbItem = document.getElementById('sb-' + n);
  if (sbItem) {{ sbItem.classList.add('active'); }}
  const pill = document.getElementById('pill-' + n);
  if (pill) {{ pill.classList.add('active'); pill.setAttribute('aria-selected','true'); }}
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
  renderMermaid('day-' + n);
}}

function jumpTo(id) {{
  const day = document.querySelector('.day-section.active');
  if (!day) return;
  const dayNum = day.id.replace('day-', '');
  const target = day.querySelector('#day-' + dayNum + '-' + id) || day.querySelector('#' + id);
  if (target) target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
}}

function toggleSidebar() {{
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (!sb) return;
  const open = sb.classList.toggle('open');
  if (btn) btn.setAttribute('aria-expanded', String(open));
}}
function closeSidebar() {{
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (sb) sb.classList.remove('open');
  if (btn) btn.setAttribute('aria-expanded', 'false');
}}

function quiz(optEl, result, qid) {{
  const block = optEl.closest('.quiz-block');
  if (!block) return;
  block.querySelectorAll('.quiz-opt').forEach(o => {{
    o.style.pointerEvents = 'none';
    if (o !== optEl) o.classList.add('dimmed');
  }});
  optEl.classList.add(result === 'correct' ? 'correct' : 'wrong');
  const letter = optEl.querySelector('.quiz-letter');
  if (letter) letter.textContent = result === 'correct' ? '✓' : '✗';
  const correctFb = block.querySelector('.correct-fb') || block.querySelector('#' + qid + '-correct');
  const wrongFb   = block.querySelector('.wrong-fb') || block.querySelector('#' + qid + '-wrong');
  if (result === 'correct') {{
    if (correctFb) {{
      correctFb.style.display = 'block';
    }}
    state.xp += 10;
    saveState();
    syncUI();
    showXPToast(10, 'quiz');
  }} else {{
    if (wrongFb) {{
      wrongFb.style.display = 'block';
    }}
  }}
}}

function toggleTask(header) {{
  const body = header.nextElementSibling;
  if (!body) return;
  const isOpen = body.style.display === 'block';
  body.style.display = isOpen ? 'none' : 'block';
  header.setAttribute('aria-expanded', String(!isOpen));
}}

// Add simple style fix for task header content if needed, but keeping toggleTask correct
function toggleSolution(id) {{
  const box = document.getElementById(id);
  if (!box) return;
  const isOpen = box.style.display === 'block';
  box.style.display = isOpen ? 'none' : 'block';
}}

function copyCode(btn) {{
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {{
    navigator.clipboard.writeText(pre.innerText).then(() => {{
      btn.textContent = 'copied!';
      setTimeout(() => btn.textContent = 'copy', 1500);
    }});
  }}
}}

function checkPredict(id, answer) {{
  const input = document.getElementById(id + '-input');
  const result = document.getElementById(id + '-result');
  if (!input || !result) return;
  const userVal = input.value.trim();
  const isCorrect = userVal === answer || userVal.includes(answer.replace(/[()]/g,''));
  result.style.display = 'block';
  if (isCorrect) {{
    result.style.background = 'rgba(79,209,165,.1)';
    result.style.border = '1px solid rgba(79,209,165,.3)';
    result.style.color = 'var(--green)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '✅ Correct! ' + answer;
    state.xp += 10; saveState(); syncUI();
  }} else {{
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer + ' — try again';
  }}
}}

function openRepl() {{
  window.open('https://replit.com/languages/python3', '_blank');
}}

function toggleTheme() {{
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') !== 'light';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
  const btn = document.getElementById('theme-btn');
  if (btn) btn.textContent = isDark ? '🌙 Dark' : '☀️ Light';
}}
(function() {{
  const saved = localStorage.getItem('theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
}})();

function renderMermaid(dayId) {{
  const run = () => {{
    const sec = document.getElementById(dayId);
    if (!sec) return;
    const nodes = sec.querySelectorAll('.mermaid:not([data-rendered])');
    if (!nodes.length) return;
    if (typeof mermaid !== 'undefined' && mermaid.run) {{
      mermaid.run({{ nodes }}).then(() => {{
        nodes.forEach(n => n.setAttribute('data-rendered','1'));
      }}).catch(() => {{}});
    }}
  }};
  if (typeof mermaid !== 'undefined') {{ run(); }}
  else {{ window.addEventListener('load', run, {{ once: true }}); }}
}}

function toggleCheck(lbl) {{
  let box = lbl.querySelector('.chk-box');
  if (!box) return;
  box.classList.toggle('checked');
  lbl.classList.toggle('done-item');
  if(box.classList.contains('checked')) box.innerText = '✓';
  else box.innerText = '';
}}

window.addEventListener('DOMContentLoaded', () => {{
  syncUI();
  DAYS.forEach(d => {{
    if (state.done.includes(d)) {{
      const btn = document.getElementById('btn-day-' + d);
      if (btn) {{ btn.classList.add('done'); btn.textContent = '✓ Day ' + d + ' Complete'; }}
    }}
  }});
  
  renderMermaid('day-' + DAYS[0]);
  
  const saved = localStorage.getItem('theme');
  const btn = document.getElementById('theme-btn');
  if (btn && saved === 'light') btn.textContent = '🌙 Dark';
}});
</script>"""

    modified, count = re.subn(pattern, new_script, content, flags=re.DOTALL)
    if count == 0:
        print(f"  Warning: inline script containing completeDay not found in Week {week_num}, appending before </body>")
        modified = content.replace("</body>", f"{new_script}\n</body>")
    return modified

# Run patching for all 18 weeks
for w in range(1, 19):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        print(f"Skipping week{w}.html: Does not exist")
        continue
    
    print(f"Patching week{w}.html...")
    
    # Backup original
    backup_path = os.path.join(backup_dir, f"week{w}.html")
    shutil.copyfile(path, backup_path)
    
    content = open(path, 'r', encoding='utf-8').read()
    
    # Apply CSS fixes
    content = patch_styles(content, w)
    
    # Apply HTML tags additions (favicon, level show, theme btn, ARIA attributes, sidebar buttons)
    content = patch_html_body(content, w, DAYS_MAP[w])
    
    # Apply XP mismatches fixes on completeDay buttons
    content = fix_xp_buttons(content, w)
    
    # Apply global resource-grid normalization
    content = content.replace("resource-grid", "resources-grid")
    
    # Apply Javascript replacements
    content = replace_script_block(content, w, DAYS_MAP[w])
    
    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"  Successfully patched week{w}.html!")

print("\nAll week files successfully patched!")
