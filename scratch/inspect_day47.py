import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w7_path = os.path.join(base_dir, "week7.html")

if os.path.exists(w7_path):
    content = open(w7_path, 'r', encoding='utf-8').read()
    
    idx_theory = content.find('<div id="theory">', content.find('id="day-47"'))
    idx_tasks = content.find('<div id="tasks-section">', idx_theory)
    
    if idx_theory != -1 and idx_tasks != -1:
        print("--- CONTENT BETWEEN THEORY AND TASKS-SECTION ---")
        print(content[idx_theory:idx_tasks + 100])
    else:
        print("Could not find theory or tasks-section in Day 47")
else:
    print("week7.html not found")
