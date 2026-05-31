with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="day-87"')
idx_next = content.find('id="day-88"')
print("Day 87 block:")
print(repr(content[idx:idx+2500]))
print("=== Around Day 88 start ===")
print(repr(content[idx_next-300:idx_next+100]))
