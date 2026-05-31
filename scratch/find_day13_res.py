with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="resources-section"')
if idx != -1:
    print(repr(content[idx:idx+400]))
else:
    print("Not found resources-section")
