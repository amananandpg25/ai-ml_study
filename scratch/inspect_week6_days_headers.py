with open('/Users/amananand/Downloads/SDE/ai:ml/week6.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
days = ["day-38", "day-39", "day-40", "day-41", "day-42", "day-43", "day-44"]
for i in range(len(days)):
    start_tag = f'<div class="day-section" id="{days[i]}">' if i > 0 else f'<div class="day-section active" id="{days[i]}">'
    end_tag = f'<div class="day-section" id="{days[i+1]}">' if i < len(days)-1 else '<!-- ── FOOTER ── -->'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        matches = re.findall(r'<h2 class="sh2">.*?(?:Flashcards|Resources).*?</h2>', block)
        print(f"=== {days[i]} ===")
        for m in matches:
            print("  -", m)
    else:
        print(f"Could not find start/end for {days[i]}")
