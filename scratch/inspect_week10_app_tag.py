with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('Deep Vision Master Resource Kit')
if idx != -1:
    print(content[idx-200:idx])
