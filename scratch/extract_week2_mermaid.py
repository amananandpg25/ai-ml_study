import re

with open("/Users/amananand/Downloads/SDE/ai:ml/week2.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find all divs or elements with class="mermaid"
mermaid_blocks = re.findall(r'<div class=\"mermaid\">(.*?)</div>', content, re.DOTALL)
mermaid_blocks_alt = re.findall(r'<pre class=\"mermaid\">(.*?)</pre>', content, re.DOTALL)
blocks = mermaid_blocks + mermaid_blocks_alt

print(f"Total blocks in week2.html: {len(blocks)}")
for idx, b in enumerate(blocks):
    print(f"\n--- BLOCK {idx+1} ---")
    print(b.strip())
