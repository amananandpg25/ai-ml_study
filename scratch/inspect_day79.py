with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="day-79"')
if idx != -1:
    print("Found day-79 at index:", idx)
    print(repr(content[idx:idx+1000]))
else:
    print("day-79 not found")
