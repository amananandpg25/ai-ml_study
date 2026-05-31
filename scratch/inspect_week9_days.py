with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
days = ["day-59", "day-60", "day-61", "day-62", "day-63", "day-64", "day-65"]
for i in range(len(days)):
    start_tag = f'<div class="day-section" id="{days[i]}">' if i > 0 else f'<div class="day-section active" id="{days[i]}">'
    end_tag = f'<div class="day-section" id="{days[i+1]}">' if i < len(days)-1 else '<!-- ── FOOTER ── -->'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        print(f"=== {days[i]} ===")
        # Print first h3 in block
        h3s = re.findall(r'<h3 class="sh3">.*?</h3>', block)
        for h3 in h3s:
            print("  -", h3)
        # Check if it has mermaid block
        has_mer = "mermaid" in block
        print("  Has mermaid:", has_mer)
    else:
        print(f"Could not find start/end for {days[i]}")
