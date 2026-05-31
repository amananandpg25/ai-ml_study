import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

BROKEN = """function runCode(btn) {
  const cb = btn.closest('.cb') || btn.closest('.solution-box');
  const pre = cb ? cb.querySelector('pre') : null;
  if (pre) {
    navigator.clipboard.writeText(pre.innerText).then(() => {
      btn.textContent = 'Copied & Opening...';
      setTimeout(() => btn.textContent = 'Run', 2000);
      window.open('https://www.programiz.com/python-programming/online-compiler/', '_blank');
    });
  }
});
  }
}"""

FIXED = """function runCode(btn) {
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

def fix_all():
    for w in range(1, 18):
        path = os.path.join(base_dir, f"week{w}.html")
        if os.path.exists(path):
            content = open(path, 'r', encoding='utf-8').read()
            if BROKEN in content:
                content = content.replace(BROKEN, FIXED)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed runCode syntax in week{w}.html")
            else:
                # Check if it was already fixed or slightly different
                if FIXED in content:
                    print(f"Already fixed in week{w}.html")
                else:
                    print(f"WARNING: Could not find broken runCode pattern in week{w}.html")

if __name__ == '__main__':
    fix_all()
