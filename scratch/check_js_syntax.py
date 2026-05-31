import os
import re
import subprocess
import tempfile

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

files = [f"week{w}.html" for w in range(1, 19)] + ["roadmap.html", "dashboard.html", "resources.html"]

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
    
    content = open(path, "r", encoding="utf-8").read()
    
    # Extract script tag content
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", content, re.DOTALL)
    for i, script_text in enumerate(scripts):
        # Write script to temporary file and run node --check
        with tempfile.NamedTemporaryFile(suffix=".js", delete=False) as tmp:
            tmp.write(script_text.encode('utf-8'))
            tmp_path = tmp.name
        
        try:
            # We use node --check to check syntax
            res = subprocess.run(["node", "--check", tmp_path], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"❌ {filename} (script #{i+1}) has JS syntax error:")
                print(res.stderr)
            else:
                pass
        finally:
            os.remove(tmp_path)
print("Syntax check finished.")
