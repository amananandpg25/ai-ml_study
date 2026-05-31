import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def fix_mermaid_text(text):
    # We want to find all occurrences of NodeID[inner_text]
    # where NodeID matches [a-zA-Z0-9_]+
    # and wrap inner_text in double quotes if not already quoted.
    pattern_label = re.compile(r'\b([a-zA-Z0-9_]+)\[')
    
    pos = 0
    while True:
        match = pattern_label.search(text, pos)
        if not match:
            break
            
        node_id = match.group(1)
        start_bracket_idx = match.start() + len(node_id) # Index of '['
        
        # Parse characters to find matching ']'
        depth = 1
        idx = start_bracket_idx + 1
        inner_text_chars = []
        while idx < len(text) and depth > 0:
            char = text[idx]
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
                
            if depth > 0:
                inner_text_chars.append(char)
                idx += 1
            else:
                break
                
        if depth > 0:
            # Malformed bracket sequence, skip
            pos = start_bracket_idx + 1
            continue
            
        inner_text = "".join(inner_text_chars)
        full_match_len = len(node_id) + len(inner_text) + 2 # id + [ + inner_text + ]
        
        # Check if already quoted
        if not (inner_text.startswith('"') and inner_text.endswith('"')):
            # It is not quoted. Let's escape any double quotes inside and wrap in quotes
            escaped_text = inner_text.replace('"', '\\"')
            replacement = f'{node_id}["{escaped_text}"]'
            
            # Replace in text
            text = text[:match.start()] + replacement + text[match.start() + full_match_len:]
            # Advance position past the replacement
            pos = match.start() + len(replacement)
        else:
            pos = match.start() + full_match_len
    return text

def parse_and_fix_file(path):
    content = open(path, 'r', encoding='utf-8').read()
    orig = content
    
    # We want to find blocks: <div class="mermaid">...</div> or <pre class="mermaid">...</pre>
    pattern_block = re.compile(r'(<(div|pre)\s+class=["\']mermaid["\'][^>]*>)(.*?)(</\2>)', re.DOTALL)
    
    new_content = ""
    last_idx = 0
    modifications = 0
    for match in pattern_block.finditer(content):
        # Add everything before the match
        new_content += content[last_idx:match.start()]
        
        opening_tag = match.group(1)
        inner_content = match.group(3)
        closing_tag = match.group(4)
        
        fixed_inner = fix_mermaid_text(inner_content)
        if fixed_inner != inner_content:
            modifications += 1
            
        new_content += opening_tag + fixed_inner + closing_tag
        last_idx = match.end()
        
    new_content += content[last_idx:]
    
    if modifications > 0 or new_content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {modifications} mermaid diagrams with unquoted labels in {os.path.basename(path)}")

def fix_all():
    for w in range(1, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if os.path.exists(path):
            parse_and_fix_file(path)

if __name__ == '__main__':
    fix_all()
