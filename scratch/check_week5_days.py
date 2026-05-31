with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for '<div id="tasks-section">' or '<h2 class="sh2">💻 Coding Tasks</h2>' inside each day block.
import re

days = ["day-31", "day-32", "day-33", "day-34", "day-35", "day-36", "day-37"]
for i in range(len(days)):
    start_tag = f'<div class="day-section" id="{days[i]}">' if i > 0 else f'<div class="day-section active" id="{days[i]}">'
    end_tag = f'<div class="day-section" id="{days[i+1]}">' if i < len(days)-1 else '<!-- ── FOOTER ── -->'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        print(f"=== {days[i]} ===")
        # Print coding task headers or sections
        task_headers = re.findall(r'<h2 class="sh2">💻 Coding Tasks</h2>|<div id="tasks-section">|<div class="tasks-section">', block)
        print("  Found task headers:", task_headers)
        # Check if already has flashcard block
        has_fc = "Flashcards" in block
        print("  Already has flashcards:", has_fc)
    else:
        print(f"Could not find start/end for {days[i]} using tags: {repr(start_tag)}, {repr(end_tag)}")
