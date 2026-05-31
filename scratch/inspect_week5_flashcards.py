with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
flashcards_headers = re.findall(r'<h2 class="sh2">.*?Flashcards.*?</h2>', content)
print("Flashcards headers found in week5.html:")
for h in flashcards_headers:
    print("  -", h)

# Let's check Day 31 flashcard block
idx = content.find("Flashcards")
if idx != -1:
    print("Context around first Flashcards:")
    print(content[idx-100:idx+600])
