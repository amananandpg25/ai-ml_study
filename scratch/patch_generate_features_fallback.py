import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
target_file = os.path.join(base_dir, "scratch", "generate_missing_features.py")

if os.path.exists(target_file):
    content = open(target_file, 'r', encoding='utf-8').read()
    
    old_block = """            if 'class="predict-block"' not in day_body:
                tasks_idx = day_body.find('id="tasks-section"')
                if tasks_idx != -1:
                    div_idx = day_body.rfind('<div', 0, tasks_idx)
                    if div_idx != -1:
                        day_body = day_body[:div_idx] + pred_html + day_body[div_idx:]"""
                        
    new_block = """            if 'class="predict-block"' not in day_body:
                tasks_idx = day_body.find('id="tasks-section"')
                if tasks_idx == -1:
                    tasks_idx = day_body.find('⚡ Tasks')
                if tasks_idx == -1:
                    tasks_idx = day_body.find('class="task-block"')
                    
                if tasks_idx != -1:
                    div_idx = day_body.rfind('<div', 0, tasks_idx)
                    if div_idx != -1:
                        day_body = day_body[:div_idx] + pred_html + day_body[div_idx:]"""
                        
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated generate_missing_features.py with tasks fallback search!")
    else:
        # Check if Windows line endings or other variations exist
        old_block_norm = old_block.replace('\r\n', '\n')
        new_block_norm = new_block.replace('\r\n', '\n')
        content_norm = content.replace('\r\n', '\n')
        if old_block_norm in content_norm:
            content_norm = content_norm.replace(old_block_norm, new_block_norm)
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content_norm)
            print("Successfully updated generate_missing_features.py (normalized line endings)!")
        else:
            print("ERROR: Predict block injection target not found in generate_missing_features.py")
else:
    print("generate_missing_features.py not found")
