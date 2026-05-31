import sys
import re

def trace_file(filepath):
    print(f"=== Detailed trace of {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    stack = []
    in_style_or_script = False
    
    for line_num, line in enumerate(lines, 1):
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        # Match all div start and close tags
        tags = re.finditer(r'(</?div\b[^>]*>)', line)
        for m in tags:
            tag = m.group(1)
            pos = m.start()
            if tag.startswith('</'):
                if stack:
                    op_tag, op_line = stack.pop()
                    # print(f"  Line {line_num}: Popped {op_tag} (from line {op_line}) matching {tag}")
                else:
                    print(f"  Line {line_num}: EXTRA CLOSE {tag}! No matching open tag!")
            else:
                stack.append((tag, line_num))
                # print(f"  Line {line_num}: Pushed {tag}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        trace_file(sys.argv[1])
