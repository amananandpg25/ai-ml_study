with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="day-87"')
grid_idx = content.find('<div class="resources-grid">', idx)
print(repr(content[grid_idx:grid_idx+800]))
