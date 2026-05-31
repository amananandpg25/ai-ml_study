import os
import glob
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
html_files = glob.glob(os.path.join(workspace_dir, "week*.html"))

new_render_mermaid = """function renderMermaid(dayId) {
  const run = () => {
    if (typeof mermaid === 'undefined') {
      setTimeout(run, 100);
      return;
    }
    if (!window.mermaidInitialized) {
      mermaid.initialize({ startOnLoad: false, theme: 'dark', securityLevel: 'loose' });
      window.mermaidInitialized = true;
    }
    const sec = document.getElementById(dayId);
    if (!sec) return;
    const nodes = sec.querySelectorAll('.mermaid:not([data-rendered])');
    if (!nodes.length) return;
    if (mermaid.run) {
      mermaid.run({ nodes }).then(() => {
        nodes.forEach(n => n.setAttribute('data-rendered','1'));
      }).catch((err) => { console.error('Mermaid render error:', err); });
    } else if (mermaid.init) {
      mermaid.init(undefined, nodes);
      nodes.forEach(n => n.setAttribute('data-rendered','1'));
    }
  };
  run();
}"""

def replace_render_mermaid(content, new_func):
    idx = content.find("function renderMermaid(dayId)")
    if idx == -1:
        idx = content.find("function renderMermaid (dayId)")
    if idx == -1:
        return content, False
    
    # Find matching closing brace
    start_brace = content.find("{", idx)
    if start_brace == -1:
        return content, False
    
    brace_count = 1
    curr = start_brace + 1
    while brace_count > 0 and curr < len(content):
        if content[curr] == "{":
            brace_count += 1
        elif content[curr] == "}":
            brace_count -= 1
        curr += 1
        
    if brace_count == 0:
        return content[:idx] + new_func + content[curr:], True
    return content, False

print(f"Auditing and patching {len(html_files)} files...")

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    modified = False
    
    # 1. Check if week4.html needs mermaid scripts added
    if filename == "week4.html":
        # check if script tag is missing
        if "mermaid.min.js" not in content:
            target_str = '<script defer="" onload="renderMathInElement(document.body, {delimiters:[{left:\'$$\',right:\'$$\',display:true},{left:\'$\',right:\'$\',display:false}]});" src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>'
            if target_str in content:
                mermaid_scripts = '\\n<script src="https://cdn.jsdelivr.net/npm/mermaid@10.2.0/dist/mermaid.min.js"></script>\\n<script>\\n  if (typeof mermaid !== \'undefined\') {\\n    mermaid.initialize({ startOnLoad: false, theme: \'dark\', securityLevel: \'loose\' });\\n  }\\n</script>'
                content = content.replace(target_str, target_str + mermaid_scripts.replace('\\n', '\n'))
                print(f"  Inserted mermaid loader scripts into {filename}")
                modified = True
            else:
                print(f"  Warning: Katex script tag not found in {filename}, could not insert mermaid loader.")
    
    # 2. Make inline initialization preview-safe (if mermaid.initialize exists)
    # We find any pattern like: mermaid.initialize({ ... });
    # and wrap it in: if (typeof mermaid !== 'undefined') { ... }
    # but check if it's already wrapped
    init_matches = list(re.finditer(r'mermaid\.initialize\(\{.*?\}\);?', content))
    for match in reversed(init_matches): # process from back to front to preserve indices
        match_str = match.group(0)
        start_idx = match.start()
        end_idx = match.end()
        
        # Check if it's already wrapped in if (typeof mermaid !== 'undefined')
        # Look back 50 characters
        lookback = content[max(0, start_idx - 60):start_idx]
        if "typeof mermaid" in lookback:
            continue
            
        wrapped_str = f"if (typeof mermaid !== 'undefined') {{ {match_str} }}"
        content = content[:start_idx] + wrapped_str + content[end_idx:]
        print(f"  Wrapped mermaid.initialize in {filename}")
        modified = True

    # 3. Replace renderMermaid function
    content, replaced_render = replace_render_mermaid(content, new_render_mermaid)
    if replaced_render:
        print(f"  Replaced renderMermaid in {filename}")
        modified = True
    else:
        print(f"  renderMermaid function not found or could not be replaced in {filename}")
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved {filename}")
    else:
        print(f"No changes needed for {filename}")
