with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="btn-day-87"')
idx2 = content.find('id="day-88"')
print(repr(content[idx:idx2]))
