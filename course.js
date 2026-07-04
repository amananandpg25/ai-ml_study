// ═══════════════════════════════════════════
//  CENTRALIZED COURSE STATE & GAMIFICATION ENGINE
// ═══════════════════════════════════════════

function migrateLegacy() {
  const stateKey = `w${WEEK}-state`;
  if (!localStorage.getItem(stateKey)) {
    const legacyXP   = parseInt(localStorage.getItem(`w${WEEK}-xp`) || localStorage.getItem(`w${WEEK}_xp`) || '0');
    const legacyDone = JSON.parse(localStorage.getItem(`w${WEEK}-done`) || localStorage.getItem(`w${WEEK}_done`) || '[]');
    const legacyStr  = parseInt(localStorage.getItem(`w${WEEK}-streak`) || localStorage.getItem(`w${WEEK}_streak`) || '0');
    const legacyDate = localStorage.getItem(`w${WEEK}-lastdate`) || localStorage.getItem(`w${WEEK}_lastDate`) || '';
    if (legacyXP || legacyDone.length) {
      localStorage.setItem(stateKey, JSON.stringify({ xp: legacyXP, done: legacyDone, streak: legacyStr, lastDate: legacyDate }));
    }
    [`w${WEEK}-xp`,`w${WEEK}-done`,`w${WEEK}-streak`,`w${WEEK}-lastdate`,
     `w${WEEK}_xp`,`w${WEEK}_done`,`w${WEEK}_streak`,`w${WEEK}_lastDate`].forEach(k => localStorage.removeItem(k));
  }
}

migrateLegacy();

let state = {};
function initializeState() {
  state = JSON.parse(localStorage.getItem(`w${WEEK}-state`) || '{}');
  state.xp     = state.xp     || 0;
  state.streak = state.streak || 0;
  state.done   = state.done   || [];
  state.lastDate = state.lastDate || '';
}
initializeState();

function saveState() {
  localStorage.setItem(`w${WEEK}-state`, JSON.stringify(state));
}

const LEVELS = [
  { min:0,    label:'🌱 Beginner' },
  { min:500,  label:'🔍 Explorer' },
  { min:1500, label:'⚙️ Practitioner' },
  { min:3000, label:'🤖 Engineer' },
  { min:6000, label:'🧠 Expert' },
  { min:10000,label:'🚀 Master' }
];

function getLevel(xp) {
  for (let i = LEVELS.length - 1; i >= 0; i--) {
    if (xp >= LEVELS[i].min) return LEVELS[i].label;
  }
  return LEVELS[0].label;
}

function syncUI() {
  const xpShow = document.getElementById('xp-show');
  if (xpShow) xpShow.textContent = `⚡ ${state.xp} XP`;
  
  const streakShow = document.getElementById('streak-show');
  if (streakShow) streakShow.textContent = `🔥 ${state.streak} day streak`;
  
  const sbXp = document.getElementById('sb-xp');
  if (sbXp) sbXp.textContent = `${state.xp} XP earned`;
  
  const sbStreak = document.getElementById('sb-streak');
  if (sbStreak) sbStreak.textContent = `${state.streak} day streak`;
  
  const lvlEl = document.getElementById('level-show');
  if (lvlEl) lvlEl.textContent = getLevel(state.xp || 0);

  const pct = Math.round((state.done.length / DAYS.length) * 100);
  const progBar = document.getElementById('prog-bar');
  if (progBar) {
    progBar.style.width = pct + '%';
    progBar.parentElement.setAttribute('aria-valuenow', pct);
  }
  const progText = document.getElementById('prog-text');
  if (progText) progText.textContent = `${state.done.length}/${DAYS.length} days`;

  DAYS.forEach(d => {
    const pill = document.getElementById('pill-' + d);
    const sb   = document.getElementById('sb-' + d);
    const btn  = document.getElementById('btn-day-' + d);
    if (state.done.includes(d)) {
      pill && pill.classList.add('done');
      sb && sb.classList.add('done');
      if (btn) { btn.classList.add('done'); btn.textContent = '✓ Day ' + d + ' Complete'; }
    }
  });
}

function completeDay(day, xp) {
  if (state.done.includes(day)) return;
  state.done.push(day);
  state.xp += xp;
  const today = new Date().toDateString();
  const yesterday = new Date(Date.now() - 86400000).toDateString();
  if (state.lastDate !== today) {
    if (state.lastDate === yesterday) { state.streak++; }
    else { state.streak = 1; }
    state.lastDate = today;
  }
  saveState();
  syncUI();
  showXPToast(xp, day);
  const btn = document.getElementById('btn-day-' + day);
  if (btn) { btn.classList.add('done'); btn.textContent = '✓ Day ' + day + ' Complete'; }
}

function showXPToast(xp, day) {
  const t = document.getElementById('xp-toast');
  if (t) {
    t.textContent = `+${xp} XP ⚡ — Day ${day} Complete!`;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
  }
}

function goDay(n) {
  document.querySelectorAll('.day-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.sb-item').forEach(i => i.classList.remove('active'));
  document.querySelectorAll('.day-pill').forEach(p => { p.classList.remove('active'); p.setAttribute('aria-selected','false'); });
  
  const section = document.getElementById('day-' + n);
  if (section) { section.classList.add('active'); }
  const sbItem = document.getElementById('sb-' + n);
  if (sbItem) { sbItem.classList.add('active'); }
  const pill = document.getElementById('pill-' + n);
  if (pill) { pill.classList.add('active'); pill.setAttribute('aria-selected','true'); }
  
  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderMermaid('day-' + n);
}

function jumpTo(id) {
  const day = document.querySelector('.day-section.active');
  if (!day) return;
  const dayNum = day.id.replace('day-', '');
  const target = day.querySelector('#day-' + dayNum + '-' + id) || day.querySelector('#' + id);
  if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function toggleSidebar() {
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (!sb) return;
  const open = sb.classList.toggle('open');
  if (btn) btn.setAttribute('aria-expanded', String(open));
}

function closeSidebar() {
  const sb  = document.getElementById('sidebar');
  const btn = document.getElementById('sidebar-toggle');
  if (sb) sb.classList.remove('open');
  if (btn) btn.setAttribute('aria-expanded', 'false');
}

function quiz(optEl, result, qid) {
  const block = optEl.closest('.quiz-block');
  if (!block) return;
  block.querySelectorAll('.quiz-opt').forEach(o => {
    o.style.pointerEvents = 'none';
    if (o !== optEl) o.classList.add('dimmed');
  });
  optEl.classList.add(result === 'correct' ? 'correct' : 'wrong');
  const letter = optEl.querySelector('.quiz-letter');
  if (letter) letter.textContent = result === 'correct' ? '✓' : '✗';
  const correctFb = block.querySelector('.correct-fb') || block.querySelector('#' + qid + '-correct');
  const wrongFb   = block.querySelector('.wrong-fb') || block.querySelector('#' + qid + '-wrong');
  if (result === 'correct') {
    if (correctFb) correctFb.style.display = 'block';
    state.xp += 10;
    saveState();
    syncUI();
    showXPToast(10, 'quiz');
  } else {
    if (wrongFb) wrongFb.style.display = 'block';
  }
}

function toggleTask(header) {
  const body = header.nextElementSibling;
  if (!body) return;
  const isOpen = body.style.display === 'block';
  body.style.display = isOpen ? 'none' : 'block';
  header.setAttribute('aria-expanded', String(!isOpen));
}

function toggleSolution(id) {
  const box = document.getElementById(id);
  if (!box) return;
  const isOpen = box.style.display === 'block';
  box.style.display = isOpen ? 'none' : 'block';
}

function copyCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {
    navigator.clipboard.writeText(pre.innerText).then(() => {
      btn.textContent = 'copied!';
      setTimeout(() => btn.textContent = 'copy', 1500);
    });
  }
}

// Visual running helper
function runCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (!pre) return;
  
  navigator.clipboard.writeText(pre.innerText);
  btn.textContent = 'Copied!';
  setTimeout(() => btn.textContent = 'Run', 2000);
  
  showCompilerModal();
}

function showCompilerModal() {
  let modal = document.getElementById('compiler-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'compiler-modal';
    modal.style.cssText = `
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(13, 15, 20, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      display: flex; align-items: center; justify-content: center;
      z-index: 10000;
      opacity: 0;
      transition: opacity 0.25s ease;
    `;
    
    const card = document.createElement('div');
    card.style.cssText = `
      background: var(--bg2, #141720);
      border: 1px solid var(--border, #252a40);
      border-radius: 16px;
      padding: 2.2rem;
      max-width: 440px;
      width: 90%;
      box-shadow: 0 20px 40px rgba(0,0,0,0.55);
      text-align: center;
      transform: scale(0.9);
      transition: transform 0.25s ease;
      color: var(--text, #dde2f0);
      font-family: var(--font-body, system-ui, sans-serif);
    `;
    
    card.innerHTML = `
      <div style="font-size: 2.8rem; margin-bottom: 0.8rem;">🚀</div>
      <h3 style="margin: 0 0 1rem 0; font-size: 1.35rem; color: var(--green, #4fd1a5); font-family: var(--font-head, sans-serif); font-weight: 800; letter-spacing: 0.5px;">Code Copied! Ready to Run</h3>
      <p style="margin: 0 0 1.8rem 0; font-size: 0.95rem; line-height: 1.6; color: var(--muted, #6b7590);">
        The code is now copied to your clipboard.
        <br><br>
        1. Click below to open the online compiler in a new tab.
        <br>
        2. <strong>Paste (Ctrl+V or Cmd+V)</strong> the code into the editor.
        <br>
        3. Click the <strong>Run</strong> button in the compiler tab to execute.
      </p>
      <div style="display: flex; gap: 12px; justify-content: center;">
        <button id="compiler-cancel" style="
          background: transparent;
          border: 1px solid var(--border, #252a40);
          color: var(--text, #dde2f0);
          padding: 10px 20px;
          border-radius: 8px;
          font-weight: 500;
          cursor: pointer;
          font-size: 0.9rem;
          transition: background var(--transition, 0.2s);
        ">Cancel</button>
        <button id="compiler-go" style="
          background: var(--green, #4fd1a5);
          border: none;
          color: var(--bg, #0d0f14);
          padding: 10px 24px;
          border-radius: 8px;
          font-weight: 700;
          cursor: pointer;
          font-size: 0.9rem;
          box-shadow: 0 4px 12px rgba(79, 209, 165, 0.2);
          transition: transform var(--transition, 0.2s), opacity var(--transition, 0.2s);
        ">Open Compiler</button>
      </div>
    `;
    
    modal.appendChild(card);
    document.body.appendChild(modal);
    
    const style = document.createElement('style');
    style.id = 'compiler-modal-styles';
    style.textContent = `
      #compiler-cancel:hover { background: var(--bg3, #1c2030); }
      #compiler-go:hover { transform: translateY(-1px); opacity: 0.95; }
    `;
    document.head.appendChild(style);

    document.getElementById('compiler-cancel').onclick = () => hide();
    document.getElementById('compiler-go').onclick = () => {
      window.open('https://www.programiz.com/python-programming/online-compiler/', '_blank');
      hide();
    };
    
    modal.onclick = (e) => {
      if (e.target === modal) hide();
    };
  }

  const modalElement = document.getElementById('compiler-modal');
  function show() {
    modalElement.style.display = 'flex';
    modalElement.offsetHeight; // force reflow
    modalElement.style.opacity = '1';
    modalElement.querySelector('div').style.transform = 'scale(1)';
  }

  function hide() {
    modalElement.style.opacity = '0';
    modalElement.querySelector('div').style.transform = 'scale(0.9)';
    setTimeout(() => {
      modalElement.style.display = 'none';
    }, 250);
  }

  show();
}

function checkPredict(id, answer) {
  const input = document.getElementById(id + '-input');
  const result = document.getElementById(id + '-result');
  if (!input || !result) return;
  
  const normalize = (str) => {
    return String(str).replace(/\\n/g, ' ')
              .replace(/\n/g, ' ')
              .replace(/['\"()\[\]]/g, '')
              .replace(/[,;]/g, ' ')
              .replace(/\s+/g, ' ')
              .trim()
              .toLowerCase();
  };
  
  const userVal = normalize(input.value);
  const correctVal = normalize(answer);
  const isCorrect = userVal === correctVal || userVal.includes(correctVal);
  
  result.style.display = 'block';
  if (isCorrect) {
    result.style.background = 'rgba(79,209,165,.1)';
    result.style.border = '1px solid rgba(79,209,165,.3)';
    result.style.color = 'var(--green)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '✅ Correct! ' + answer.replace(/\n/g, ' ');
    state.xp += 10; saveState(); syncUI();
  } else {
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer.replace(/\n/g, ' ') + ' — try again';
  }
}

function openRepl() {
  window.open('https://replit.com/languages/python3', '_blank');
}

function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') !== 'light';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
  const btn = document.getElementById('theme-btn');
  if (btn) btn.textContent = isDark ? '🌙 Dark' : '☀️ Light';
}

function renderMermaid(dayId) {
  const run = () => {
    if (typeof mermaid === 'undefined') {
      setTimeout(run, 100);
      return;
    }
    if (!window.mermaidInitialized) {
      mermaid.initialize({ startOnLoad: false, theme: 'dark', securityLevel: 'loose' });
      window.mermaidInitialized = true;
    }
    const sec = document.getElementById(dayId);
    if (!sec) return;
    const nodes = sec.querySelectorAll('.mermaid:not([data-rendered])');
    if (!nodes.length) return;
    if (mermaid.run) {
      mermaid.run({ nodes }).then(() => {
        nodes.forEach(n => n.setAttribute('data-rendered','1'));
      }).catch((err) => { console.error('Mermaid render error:', err); });
    } else if (mermaid.init) {
      mermaid.init(undefined, nodes);
      nodes.forEach(n => n.setAttribute('data-rendered','1'));
    }
  };
  run();
}

function toggleCheck(lbl) {
  let box = lbl.querySelector('.chk-box');
  if (!box) return;
  box.classList.toggle('checked');
  lbl.classList.toggle('done-item');
  if(box.classList.contains('checked')) box.innerText = '✓';
  else box.innerText = '';
}

// ── DOM CONTENT LOADED EVENT BINDINGS ──
window.addEventListener('DOMContentLoaded', () => {
  syncUI();
  
  DAYS.forEach(d => {
    const btn = document.getElementById('btn-day-' + d);
    if (state.done.includes(d)) {
      if (btn) { btn.classList.add('done'); btn.textContent = '✓ Day ' + d + ' Complete'; }
    }
  });
  
  if (DAYS.length > 0) {
    renderMermaid('day-' + DAYS[0]);
  }
  
  document.querySelectorAll('.predict-input').forEach(input => {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const btn = input.nextElementSibling;
        if (btn && btn.classList.contains('predict-btn')) {
          btn.click();
        }
      }
    });
  });

  const saved = localStorage.getItem('theme');
  if (saved) {
    document.documentElement.setAttribute('data-theme', saved);
    const btn = document.getElementById('theme-btn');
    if (btn && saved === 'light') btn.textContent = '🌙 Dark';
  }
});
