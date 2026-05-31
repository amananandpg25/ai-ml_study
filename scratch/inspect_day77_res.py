with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find index of Day 77 Resources
idx = content.find('Day 77 Resources')
if idx == -1:
    idx = content.find('📚 Resources')
if idx != -1:
    print(content[idx:idx+1500])
