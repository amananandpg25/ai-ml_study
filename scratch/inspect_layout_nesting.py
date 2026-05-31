import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def inspect_file(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    lines = content.splitlines()
    
    print(f"\n=== week{w}.html layout tags ===")
    for line_num, line in enumerate(lines, 1):
        if 'class="layout"' in line or "class='layout'" in line:
            print(f"Line {line_num:4d}: {line.strip()}")
        if 'class="sidebar"' in line or "class='sidebar'" in line:
            print(f"Line {line_num:4d}: {line.strip()}")
        if 'class="main"' in line or "class='main'" in line or '<main>' in line or '<main ' in line:
            print(f"Line {line_num:4d}: {line.strip()}")
        if '</main>' in line:
            print(f"Line {line_num:4d}: {line.strip()}")
        if '/layout' in line:
            print(f"Line {line_num:4d}: {line.strip()}")

inspect_file(15)
inspect_file(16)
inspect_file(17)
inspect_file(6)
inspect_file(7)
