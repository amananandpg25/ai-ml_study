import os
import glob

brain_dir = "/Users/amananand/.gemini/antigravity/brain"
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if 'audit' in f.lower() or 'report' in f.lower():
            path = os.path.join(root, f)
            print(f"Found audit/report file: {path} (size: {os.path.getsize(path)} bytes)")
            # print first line
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    print("  First line:", file.readline().strip())
            except Exception as e:
                pass
