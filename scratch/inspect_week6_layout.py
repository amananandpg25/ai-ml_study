import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w6_path = os.path.join(base_dir, "week6.html")

if os.path.exists(w6_path):
    content = open(w6_path, 'r', encoding='utf-8').read()
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
            
        # Find all opening and closing div tags
        tags = re.findall(r'(</?div\b[^>]*>)', line)
        if tags:
            for tag in tags:
                old_depth = depth
                if tag.startswith('</'):
                    depth -= 1
                else:
                    depth += 1
                
                # If depth goes negative or is very high/low, print it
                if depth < 0 or depth > 10:
                    print(f"Line {line_num:4d} | Depth {old_depth:2d} -> {depth:2d} | {tag} | line: {line.strip()}")
                
                # Let's also print around day headers or major boundaries to see where it changes unexpectedly
                if 'day-' in tag and not tag.startswith('</'):
                    print(f"Line {line_num:4d} | Day Section Start | Depth: {depth} | {tag}")
                if '<!-- /day-' in line:
                    print(f"Line {line_num:4d} | Day Section End | Depth: {depth} | {line.strip()}")
    print("Final depth:", depth)
else:
    print("week6.html not found")
