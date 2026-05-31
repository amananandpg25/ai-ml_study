import re

def debug_week4():
    with open('week4.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    stack = []
    in_style_or_script = False
    
    # We trace lines 700 to 1025
    for line_num, line in enumerate(lines, 1):
        if line_num < 715:
            # Still process tags to keep stack accurate
            pass
        if line_num > 1025:
            break
            
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        tags = re.finditer(r'(</?div\b[^>]*>)', line)
        for m in tags:
            tag = m.group(1)
            if tag.startswith('</'):
                if stack:
                    op_tag, op_line = stack.pop()
                    if line_num >= 715:
                        print(f"Line {line_num:4d}: Pop {op_tag} (from line {op_line}) using {tag}. Stack depth={len(stack)}")
                else:
                    if line_num >= 715:
                        print(f"Line {line_num:4d}: EXTRA CLOSE {tag}!")
            else:
                stack.append((tag, line_num))
                if line_num >= 715:
                    print(f"Line {line_num:4d}: Push {tag}. Stack depth={len(stack)}")

if __name__ == '__main__':
    debug_week4()
