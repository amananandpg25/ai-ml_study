import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w7_path = os.path.join(base_dir, "week7.html")

if os.path.exists(w7_path):
    content = open(w7_path, 'r', encoding='utf-8').read()
    lines = content.splitlines()
    depth = 0
    in_style_or_script = False
    
    for line_num, line in enumerate(lines, 1):
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        tags = re.findall(r'(</?div\b[^>]*>)', line)
        if tags:
            for tag in tags:
                old_depth = depth
                if tag.startswith('</'):
                    depth -= 1
                else:
                    depth += 1
                
                if depth < 0 or depth > 10:
                    print(f"Line {line_num:4d} | Depth {old_depth:2d} -> {depth:2d} | {tag} | line: {line.strip()}")
                
                if 'day-' in tag and not tag.startswith('</'):
                    print(f"Line {line_num:4d} | Day Section Start | Depth: {depth} | {tag}")
                if '<!-- /day-' in line:
                    print(f"Line {line_num:4d} | Day Section End | Depth: {depth} | {line.strip()}")
    print("Final depth:", depth)
else:
    print("week7.html not found")
