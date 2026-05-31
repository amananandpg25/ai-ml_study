import re
import glob
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
standard_funcs = {
    'saveState', 'loadState', 'completeDay', 'syncUI', 'updateUI', 'goDay',
    'toggleTask', 'toggleSidebar', 'closeSidebar', 'quiz', 'toggleSolution',
    'copyCode', 'checkPredict', 'openRepl', 'renderMermaid', 'toggleTheme',
    'getLevel', 'showXPToast', 'showXpToast'
}

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    content = open(path, 'r', encoding='utf-8').read()
    
    # Extract script tag content
    scripts = re.findall(r"<script>(.*?)</script>", content, re.DOTALL)
    if not scripts:
        print(f"week{w}.html: No script tag")
        continue
    
    script_text = scripts[-1]
    # find all function declarations: function name(...) or const name = (...) =>
    funcs = re.findall(r"function\s+(\w+)", script_text)
    const_funcs = re.findall(r"const\s+(\w+)\s*=\s*(?:function|\([^)]*\)\s*=>)", script_text)
    
    all_funcs = set(funcs + const_funcs)
    custom = all_funcs - standard_funcs
    
    if custom:
        print(f"week{w}.html: Found custom functions: {custom}")
    else:
        print(f"week{w}.html: Only standard functions")
