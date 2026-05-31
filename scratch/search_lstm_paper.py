with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('2604.pdf')
if idx != -1:
    print("Found 2604.pdf at index:", idx)
    print(repr(content[idx-100:idx+400]))
else:
    print("2604.pdf not found")
