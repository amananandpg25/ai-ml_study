import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def inspect_tasks(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
    content = open(path, 'r', encoding='utf-8').read()
    
    print(f"\n=== week{w}.html tasks search ===")
    tasks_secs = re.findall(r'(<div\s+id=["\']tasks-section["\'].*?>)', content)
    print("  id='tasks-section' occurrences:", tasks_secs)
    
    tasks_classes = re.findall(r'(class=["\']tasks-section["\'])', content)
    print("  class='tasks-section' occurrences:", tasks_classes)
    
    tasks_h2 = re.findall(r'(<h2[^>]*>.*?tasks.*?</h2>)', content, re.IGNORECASE)
    print("  h2 with tasks occurrences:", tasks_h2)

inspect_tasks(15)
inspect_tasks(16)
inspect_tasks(17)
inspect_tasks(13)
inspect_tasks(14)
