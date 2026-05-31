with open('/Users/amananand/Downloads/SDE/ai:ml/week12.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 81 start and end
day81_start = content.find('id="day-81"')
day82_start = content.find('id="day-82"')

if day81_start != -1 and day82_start != -1:
    day81_block = content[day81_start:day82_start]
    # Find all mermaid blocks
    import re
    mermaid_blocks = re.findall(r'<div class="mermaid">.*?</div>', day81_block, re.DOTALL)
    print(f"Found {len(mermaid_blocks)} mermaid blocks in Day 81:")
    for mb in mermaid_blocks:
        print(mb)
else:
    print("Day 81 start/end not found")
