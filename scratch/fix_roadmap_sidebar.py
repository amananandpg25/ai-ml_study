import re

roadmap_path = "/Users/amananand/Downloads/SDE/ai:ml/roadmap.html"

with open(roadmap_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace showSection(\'xxx\', with showSection('xxx',
new_content = content.replace("showSection(\\'", "showSection('").replace("\\', this)", "', this)")

with open(roadmap_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done clean replace!")
