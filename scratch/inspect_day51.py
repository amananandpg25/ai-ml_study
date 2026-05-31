import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w7_path = os.path.join(base_dir, "week7.html")

if os.path.exists(w7_path):
    content = open(w7_path, 'r', encoding='utf-8').read()
    
    idx = content.find('id="day-51"')
    # Find next day section, or if none, look for the closing main/layout/body tags
    # Wait, day-51 is the last day of week 7 (days 45-51). So it's followed by </main>
    next_idx = content.find('</main>', idx)
    
    if idx != -1 and next_idx != -1:
        day51_body = content[idx:next_idx]
        print("Day 51 length:", len(day51_body))
        
        lines = content.splitlines()
        day51_start_line = content[:idx].count('\n') + 1
        day51_end_line = content[:next_idx].count('\n') + 1
        
        depth = 1 # inside day-section (depth starts at 1 relative to layout/main)
        print(f"Tracing Day 51 from line {day51_start_line} to {day51_end_line}")
        for i in range(day51_start_line, day51_end_line):
            line = lines[i-1]
            tags = re.findall(r'(</?div\b[^>]*>)', line)
            if tags:
                for tag in tags:
                    old_depth = depth
                    if tag.startswith('</'):
                        depth -= 1
                    else:
                        depth += 1
                    print(f"Line {i:4d} | Depth {old_depth:2d} -> {depth:2d} | {tag} | {line.strip()[:60]}")
    else:
        print("Could not find day-51 or </main>")
else:
    print("week7.html not found")
