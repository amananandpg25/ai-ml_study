import os, re

base = "/Users/amananand/Downloads/SDE/ai:ml"

THEME_BTN = '    <button id="theme-btn" class="theme-btn" onclick="toggleTheme()" aria-label="Toggle light/dark mode">☀️ Light</button>'

# The exact closing pattern of the topnav right-side flex div
# Line structure:  "    </div>\n  </div>\n</nav>"
# We insert the theme button BEFORE "  </div>\n</nav>"
ANCHOR = '  </div>\n</nav>'
INSERT_BEFORE = ANCHOR

fixed = []
skipped = []
failed = []

for w in range(1, 18):
    fn = f"week{w}.html"
    path = os.path.join(base, fn)
    content = open(path, "r", encoding="utf-8").read()

    if 'id="theme-btn"' in content:
        skipped.append(fn)
        continue

    # Find the last occurrence of "  </div>\n</nav>"
    idx = content.rfind(INSERT_BEFORE)
    if idx == -1:
        failed.append(fn)
        continue

    # Insert theme button before "  </div>\n</nav>"
    new_content = content[:idx] + THEME_BTN + '\n' + content[idx:]
    open(path, "w", encoding="utf-8").write(new_content)
    fixed.append(fn)

print(f"Fixed ({len(fixed)}): {fixed}")
print(f"Skipped-already-has ({len(skipped)}): {skipped}")
print(f"Failed ({len(failed)}): {failed}")

# Quick verify
print("\nVerifying id='theme-btn' presence:")
for w in range(1, 18):
    fn = f"week{w}.html"
    c = open(os.path.join(base, fn)).read()
    has = 'id="theme-btn"' in c
    print(f"  {'✅' if has else '❌'} {fn}")
