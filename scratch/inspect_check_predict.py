import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w1_path = os.path.join(base_dir, "week1.html")

if os.path.exists(w1_path):
    content = open(w1_path, 'r', encoding='utf-8').read()
    
    # Let's extract the checkPredict function definition
    idx = content.find('function checkPredict')
    if idx != -1:
        end_idx = content.find('}', idx)
        # expand end_idx to find matching closing brace if nested, or just print 30 lines
        print("--- checkPredict definition in week1.html ---")
        print(content[idx:idx+800])
    else:
        print("checkPredict function not found")
else:
    print("week1.html not found")
