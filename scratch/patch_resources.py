import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
resources_path = os.path.join(base_dir, "resources.html")

content = open(resources_path, 'r', encoding='utf-8').read()

# Replace fonts stylesheet link and styles import
old_fonts = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root {"""

new_fonts = """<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {"""

content = content.replace(old_fonts, new_fonts)

# Replace the variables block in :root
old_vars = """  --bg: #09090f;
  --bg2: #0f0f1a;
  --bg3: #141426;
  --card: #12121e;
  --border: #1e1e32;
  --border2: #252540;
  --text: #e8e8f0;
  --muted: #5a5a80;
  --dim: #3a3a60;"""

new_vars = """  --bg: #0d0f14;
  --bg2: #141720;
  --bg3: #1c2030;
  --card: #1e2235;
  --border: #2a3050;
  --border2: #353b65;
  --text: #e8ecf5;
  --muted: #7a84a0;
  --dim: #2e3556;"""

content = content.replace(old_vars, new_vars)

# Replace font definitions
content = content.replace("--font-head: 'Epilogue', sans-serif;", "--font-head: 'Syne', sans-serif;")
content = content.replace("--font-body: 'Outfit', sans-serif;", "--font-body: 'DM Sans', sans-serif;")
content = content.replace("--font-mono: 'JetBrains Mono', monospace;", "--font-mono: 'IBM Plex Mono', monospace;")

with open(resources_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("resources.html styling variables successfully updated!")
