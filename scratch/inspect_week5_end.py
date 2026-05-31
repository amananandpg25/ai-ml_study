with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's print the last 1000 characters of the file
print(repr(content[-1000:]))
