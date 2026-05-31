import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
target_file = os.path.join(base_dir, "scratch", "generate_missing_features.py")

if os.path.exists(target_file):
    content = open(target_file, 'r', encoding='utf-8').read()
    
    old_line = """        # --- 8. INJECT PREDICT THE OUTPUT ---
        if w >= 8:"""
        
    new_line = """        # --- 8. INJECT PREDICT THE OUTPUT ---
        if w >= 7:"""
        
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated generate_missing_features.py for week 7 predict block injection!")
    else:
        # Normalized check
        old_line_norm = old_line.replace('\r\n', '\n')
        new_line_norm = new_line.replace('\r\n', '\n')
        content_norm = content.replace('\r\n', '\n')
        if old_line_norm in content_norm:
            content_norm = content_norm.replace(old_line_norm, new_line_norm)
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content_norm)
            print("Successfully updated generate_missing_features.py (normalized line endings)!")
        else:
            print("ERROR: Predict block week check target not found in generate_missing_features.py")
else:
    print("generate_missing_features.py not found")
