import os
import re
import subprocess

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
scratch_dir = "/Users/amananand/Downloads/SDE/ai:ml/scratch"

def validate_js(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Extract script contents
    scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    
    for idx, script in enumerate(scripts):
        # Exclude scripts that just load libraries
        if 'function' not in script and 'const' not in script:
            continue
            
        temp_js_path = os.path.join(scratch_dir, f"temp_w{w}_{idx}.js")
        with open(temp_js_path, 'w', encoding='utf-8') as f:
            f.write(script)
            
        # Run node --check
        res = subprocess.run(['node', '--check', temp_js_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"week{w}.html Script {idx+1} has SYNTAX ERROR:")
            print(res.stderr)
        else:
            print(f"week{w}.html Script {idx+1} is syntactically valid!")
            
        # Clean up
        if os.path.exists(temp_js_path):
            os.remove(temp_js_path)

if __name__ == '__main__':
    for w in range(1, 18):
        validate_js(w)
