import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(base_dir, "roadmap.html")

content = open(roadmap_path, 'r', encoding='utf-8').read()

# 1. Replace sidebar nav day ranges
content = content.replace(
    'Week 15 — LLMs + GenAI <span class="day-range">105–111</span>',
    'Week 15 — LLMs + GenAI <span class="day-range">101–107</span>'
)

content = content.replace(
    'Week 16 — RAG + Agents <span class="day-range">112–120</span>',
    'Week 16 — RAG + Agents <span class="day-range">108–117</span>'
)

content = content.replace(
    'Deploy + Flask+Docker <span class="day-range">121–127</span>',
    'Deploy + Flask+Docker <span class="day-range">118–124</span>'
)

# 2. Replace section headers tags
content = content.replace(
    '<div class="section-tag">MONTH 4 · DAYS 112–120</div>',
    '<div class="section-tag">MONTH 4 · DAYS 108–117</div>'
)

content = content.replace(
    '<div class="section-tag">FINAL · DAYS 121–127</div>',
    '<div class="section-tag">FINAL · DAYS 118–124</div>'
)

# Save changes
with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Roadmap day ranges aligned successfully!")
