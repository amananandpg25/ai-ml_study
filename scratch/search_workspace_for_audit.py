import os

search_dir = "/Users/amananand/Downloads/SDE/ai:ml"
for root, dirs, files in os.walk(search_dir):
    for f in files:
        path = os.path.join(root, f)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if "Full Content Audit" in content:
                    print(f"Found in: {path}")
        except Exception as e:
            pass
