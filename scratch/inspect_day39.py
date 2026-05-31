import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w6_path = os.path.join(base_dir, "week6.html")

if os.path.exists(w6_path):
    content = open(w6_path, 'r', encoding='utf-8').read()
    
    idx = content.find('id="day-39"')
    next_idx = content.find('id="day-40"')
    
    if idx != -1 and next_idx != -1:
        day39_body = content[idx:next_idx]
        print("Day 39 length:", len(day39_body))
        
        # Trace line numbers relative to the file
        lines = content.splitlines()
        day39_start_line = content[:idx].count('\n') + 1
        day39_end_line = content[:next_idx].count('\n') + 1
        
        depth = 1 # inside day-section (which is index 1 inside layout/main)
        print(f"Tracing Day 39 from line {day39_start_line} to {day39_end_line}")
        for i in range(day39_start_line, day39_end_line):
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
        print("Could not find day-39 or day-40")
else:
    print("week6.html not found")
