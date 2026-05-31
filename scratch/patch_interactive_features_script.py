import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
target_file = os.path.join(base_dir, "scratch", "patch_interactive_features.py")

if os.path.exists(target_file):
    content = open(target_file, 'r', encoding='utf-8').read()
    
    # 1. We want to replace the first checkPredict replacement part (lines 71-79)
    old_block = """    # 1. Replace checkPredict function
    # Match function checkPredict(id, answer) { ... }
    # Using regex to find the start and end of the function
    match_cp = re.search(r'function checkPredict\\(id,\\s*answer\\)\\s*\\{.*?\\}', content, re.DOTALL)
    if match_cp:
        content = content[:match_cp.start()] + NEW_CHECK_PREDICT + content[match_cp.end():]
        print(f"  Patched checkPredict JS in {os.path.basename(path)}")
    else:
        print(f"  WARNING: Could not find checkPredict function in {os.path.basename(path)}")"""
        
    new_block = """    # 1. Replace checkPredict function
    # Match function checkPredict(id, answer) { ... }
    # Using regex to find the start and end of the function (matching answer, expected, or correct)
    match_cp = re.search(r'function checkPredict\\(id,\\s*(?:answer|expected|correct)\\)\\s*\\{.*?\\}', content, re.DOTALL)
    if match_cp:
        content = content[:match_cp.start()] + NEW_CHECK_PREDICT + content[match_cp.end():]
        print(f"  Patched checkPredict JS in {os.path.basename(path)}")
    else:
        # Inject it at the beginning of the main script tag
        script_idx = content.rfind('<script>')
        if script_idx == -1:
            script_idx = content.rfind('<script type="text/javascript">')
        if script_idx == -1:
            # Match any script tag
            match_script = re.search(r'<script[^>]*>', content)
            if match_script:
                script_idx = match_script.start()
        
        if script_idx != -1:
            # Find the closing tag of this script tag block to insert it right after the opening tag
            tag_end = content.find('>', script_idx)
            if tag_end != -1:
                content = content[:tag_end+1] + "\\n" + NEW_CHECK_PREDICT + "\\n" + content[tag_end+1:]
                print(f"  Injected new checkPredict JS in {os.path.basename(path)}")
            else:
                print(f"  WARNING: Could not find end of script tag to inject in {os.path.basename(path)}")
        else:
            print(f"  WARNING: Could not find script tag to inject checkPredict in {os.path.basename(path)}")"""

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated patch_interactive_features.py!")
    else:
        # Try normalized line endings
        old_block_norm = old_block.replace('\r\n', '\n')
        new_block_norm = new_block.replace('\r\n', '\n')
        content_norm = content.replace('\r\n', '\n')
        if old_block_norm in content_norm:
            content_norm = content_norm.replace(old_block_norm, new_block_norm)
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content_norm)
            print("Successfully updated patch_interactive_features.py (normalized line endings)!")
        else:
            print("ERROR: checkPredict replacement target not found in patch_interactive_features.py")
else:
    print("patch_interactive_features.py not found")
