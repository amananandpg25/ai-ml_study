import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

TARGET_FUNCTION = """function runCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {
    navigator.clipboard.writeText(pre.innerText).then(() => {
      btn.textContent = 'Copied & Opening...';
      setTimeout(() => btn.textContent = 'Run', 2000);
      window.open('https://www.programiz.com/python-programming/online-compiler/', '_blank');
    });
  }
}"""

IMPROVED_FUNCTION = """function runCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (!pre) return;
  
  // Copy code to clipboard
  navigator.clipboard.writeText(pre.innerText);
  
  // Visual feedback on the button
  btn.textContent = 'Copied!';
  setTimeout(() => btn.textContent = 'Run', 2000);
  
  // Show compiler instructions modal
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
    
    // Add hover styles
    const style = document.createElement('style');
    style.textContent = `
      #compiler-cancel:hover { background: var(--bg3, #1c2030); }
      #compiler-go:hover { transform: translateY(-1px); opacity: 0.95; }
    `;
    document.head.appendChild(style);

    // Event listeners
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
}"""

def improve_run_code():
    for w in range(1, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        content = open(path, 'r', encoding='utf-8').read()
        
        if TARGET_FUNCTION in content:
            new_content = content.replace(TARGET_FUNCTION, IMPROVED_FUNCTION)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"week{w}.html: Successfully upgraded runCode to show beautiful modal instruction.")
        else:
            # Normalized match (just in case of Windows line endings)
            norm_target = TARGET_FUNCTION.replace('\r\n', '\n')
            norm_improved = IMPROVED_FUNCTION.replace('\r\n', '\n')
            norm_content = content.replace('\r\n', '\n')
            
            if norm_target in norm_content:
                new_content = norm_content.replace(norm_target, norm_improved)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"week{w}.html: Successfully upgraded runCode (normalized path).")
            else:
                # Let's check if it is already improved
                if "showCompilerModal" in content:
                    print(f"week{w}.html: Already improved.")
                else:
                    print(f"week{w}.html: ERROR! TARGET_FUNCTION not found!")

if __name__ == '__main__':
    improve_run_code()
