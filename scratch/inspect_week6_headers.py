with open('/Users/amananand/Downloads/SDE/ai:ml/week6.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<h2 class="sh2">.*?(?:Flashcards|Resources).*?</h2>', content)
print("Headers in week6.html:")
for m in matches:
    print("  -", m)
