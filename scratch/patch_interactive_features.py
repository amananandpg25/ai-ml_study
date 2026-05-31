import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

NEW_CHECK_PREDICT = """function checkPredict(id, answer) {
  const input = document.getElementById(id + '-input');
  const result = document.getElementById(id + '-result');
  if (!input || !result) return;
  
  // Normalize whitespace, casing, quotes, brackets, and punctuation
  const normalize = (str) => {
    return str.replace(/\\s+/g, ' ')
              .replace(/['"()\\['\\]]/g, '')
              .replace(/[,;]/g, ' ')
              .replace(/\\s+/g, ' ')
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
    result.textContent = '✅ Correct! ' + answer.replace(/\\n/g, ' ');
    state.xp += 10; saveState(); syncUI();
  } else {
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer.replace(/\\n/g, ' ') + ' — try again';
  }
}"""

RUN_CODE_JS = """function copyCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {
    navigator.clipboard.writeText(pre.innerText).then(() => {
      btn.textContent = 'copied!';
      setTimeout(() => btn.textContent = 'copy', 1500);
    });
  }
}

function runCode(btn) {
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

def find_matching_brace(text, start_idx):
    # Find the first '{' after start_idx
    brace_start = text.find('{', start_idx)
    if brace_start == -1:
        return -1
    
    depth = 1
    idx = brace_start + 1
    while depth > 0 and idx < len(text):
        if text[idx] == '{':
            depth += 1
        elif text[idx] == '}':
            depth -= 1
        idx += 1
    return idx

def patch_file(path):
    content = open(path, 'r', encoding='utf-8').read()
    
    # 1. Replace checkPredict function using brace counter
    match_cp = re.search(r'function checkPredict\(id,\s*(?:answer|expected|correct)\)\s*\{', content)
    if match_cp:
        end_idx = find_matching_brace(content, match_cp.start())
        if end_idx != -1:
            content = content[:match_cp.start()] + NEW_CHECK_PREDICT + content[end_idx:]
            print(f"  Patched checkPredict JS in {os.path.basename(path)}")
        else:
            print(f"  WARNING: Could not find matching brace for checkPredict in {os.path.basename(path)}")
    else:
        # Inject at the beginning of the main script tag
        script_idx = content.rfind('<script>')
        if script_idx == -1:
            script_idx = content.rfind('<script type="text/javascript">')
        if script_idx == -1:
            match_script = re.search(r'<script[^>]*>', content)
            if match_script:
                script_idx = match_script.start()
        
        if script_idx != -1:
            tag_end = content.find('>', script_idx)
            if tag_end != -1:
                content = content[:tag_end+1] + "\n" + NEW_CHECK_PREDICT + "\n" + content[tag_end+1:]
                print(f"  Injected new checkPredict JS in {os.path.basename(path)}")
            else:
                print(f"  WARNING: Could not find end of script tag to inject in {os.path.basename(path)}")
        else:
            print(f"  WARNING: Could not find script tag to inject checkPredict in {os.path.basename(path)}")
        
    # 2. Replace copyCode function using brace counter
    match_cc = re.search(r'function copyCode\(btn\)\s*\{', content)
    if match_cc:
        end_idx = find_matching_brace(content, match_cc.start())
        if end_idx != -1:
            content = content[:match_cc.start()] + RUN_CODE_JS + content[end_idx:]
            print(f"  Injected runCode JS in {os.path.basename(path)}")
        else:
            print(f"  WARNING: Could not find matching brace for copyCode in {os.path.basename(path)}")
    else:
        # Fallback: if copyCode is slightly different, replace the exact match
        copy_exact = "function copyCode(btn) {\n  const cb = btn.closest('.cb') || btn.closest('.solution-box');\n  const pre = cb ? cb.querySelector('pre') : null;\n  if (pre) {\n    navigator.clipboard.writeText(pre.innerText).then(() => {\n      btn.textContent = 'copied!';\n      setTimeout(() => btn.textContent = 'copy', 1500);\n    });\n  }\n}"
        if copy_exact in content:
            content = content.replace(copy_exact, RUN_CODE_JS)
            print(f"  Injected runCode JS via fallback in {os.path.basename(path)}")
        else:
            print(f"  WARNING: Could not find copyCode JS in {os.path.basename(path)}")
            
    # 3. Add Run button in HTML next to Copy buttons
    copy_btn_html = '<button class="copy-btn" onclick="copyCode(this)">Copy</button>'
    new_btns_html = '<button class="copy-btn" onclick="copyCode(this)">Copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button>'
    
    if copy_btn_html in content:
        count = content.count(copy_btn_html)
        content = content.replace(copy_btn_html, new_btns_html)
        print(f"  Injected {count} Run buttons into HTML of {os.path.basename(path)}")
    else:
        copy_btn_html_alt = '<button class="copy-btn" onclick="copyCode(this)">copy</button>'
        new_btns_html_alt = '<button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button>'
        if copy_btn_html_alt in content:
            count = content.count(copy_btn_html_alt)
            content = content.replace(copy_btn_html_alt, new_btns_html_alt)
            print(f"  Injected {count} Run buttons into HTML (lowercase copy) of {os.path.basename(path)}")
        else:
            print(f"  WARNING: No Copy buttons found in {os.path.basename(path)}")
            
    # Save back to file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def patch_all():
    for w in range(1, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if os.path.exists(path):
            print(f"\nPatching {os.path.basename(path)}...")
            patch_file(path)

if __name__ == '__main__':
    patch_all()
