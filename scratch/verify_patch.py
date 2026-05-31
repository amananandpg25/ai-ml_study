import os
import glob
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
html_files = glob.glob(os.path.join(workspace_dir, "week*.html"))

print(f"Verifying {len(html_files)} files...")
all_valid = True

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check 1: Wrapped initialization check
    # We should have the wrapped version:
    # if (typeof mermaid !== 'undefined') { mermaid.initialize({ ... }); }
    has_wrapped_init = re.search(r"if\s*\(\s*typeof\s+mermaid\s*!==\s*['\"]undefined['\"]\s*\)\s*\{\s*mermaid\.initialize", content)
    
    # Check 2: Has renderMermaid function with window.mermaidInitialized
    has_robust_render = "window.mermaidInitialized" in content and "function renderMermaid" in content
    
    # Check 3: Has script tag for mermaid
    has_script_tag = "mermaid.min.js" in content
    
    # Count total mermaid.initialize occurrences
    num_inits = content.count("mermaid.initialize")
    
    # Report errors
    errors = []
    if not has_wrapped_init:
        errors.append("wrapped initialization missing in script block")
    if not has_robust_render:
        errors.append("robust renderMermaid function missing or incorrect")
    if not has_script_tag:
        errors.append("mermaid.min.js script tag missing")
    if num_inits != 2:
        errors.append(f"expected exactly 2 mermaid.initialize calls, found {num_inits}")
        
    if errors:
        print(f"❌ {filename}: {', '.join(errors)}")
        all_valid = False
    else:
        print(f"✅ {filename} is valid!")

if all_valid:
    print("\n🎉 All checks passed! All files successfully verified.")
else:
    print("\n⚠️ Some validation errors were found.")
