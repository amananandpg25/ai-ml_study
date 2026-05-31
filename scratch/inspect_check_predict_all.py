import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    content = open(path, 'r', encoding='utf-8').read()
    
    idx = content.find('function checkPredict')
    if idx != -1:
        # print function header and first few lines of validation
        lines = content[idx:idx+350].splitlines()
        print(f"week{w}.html:")
        for line in lines[:8]:
            print(f"  {line}")
    else:
        print(f"week{w}.html: checkPredict not found")
