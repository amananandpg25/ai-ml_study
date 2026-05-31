import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    content = open(path, 'r', encoding='utf-8').read()
    count = content.count('checkPredict')
    print(f"week{w}.html: checkPredict appears {count} times in the file")
