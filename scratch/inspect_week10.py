with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<div\s+[^>]*id="(day-70|day-71|day-72)"', content)
print("Found days in week10.html:", matches)

# Find the appendix section
appendix_idx = content.find('Graduate Resources')
if appendix_idx == -1:
    appendix_idx = content.find('Deep Vision Master Resource Kit')
if appendix_idx != -1:
    print("Appendix found at index:", appendix_idx)
    print(content[appendix_idx:appendix_idx+800])
else:
    print("Appendix not found")

# Check for mermaid diagrams in week10.html
mermaid_blocks = re.findall(r'<div class="mermaid">.*?</div>', content, re.DOTALL)
print(f"Found {len(mermaid_blocks)} mermaid blocks in week10.html:")
for i, mb in enumerate(mermaid_blocks):
    print(f"--- Block {i} ---")
    print(mb[:200].strip())
