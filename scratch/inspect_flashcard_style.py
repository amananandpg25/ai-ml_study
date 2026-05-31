with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<h2 class="sh2">🃏 Revision Flashcards — Day 33</h2>')
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Not found Day 33 flashcards")
