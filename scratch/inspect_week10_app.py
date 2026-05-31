with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find index of 'Graduate Resources' or 'Deep Vision Master Resource Kit'
idx = content.find('Deep Vision Master Resource Kit')
if idx != -1:
    print("Found starting at:", idx)
    print(content[idx:idx+1500])
    # Let's print the last 1500 chars of the file to see how it ends
    print("=== File End ===")
    print(content[-1500:])
else:
    print("Not found")
