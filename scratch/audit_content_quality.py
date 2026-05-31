import os
import re
from bs4 import BeautifulSoup

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def audit_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        return None
        
    html = open(path, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Day sections
    day_sections = soup.find_all(class_=re.compile(r'\bday-section\b'))
    day_ids = [d.get('id') for d in day_sections]
    
    days_data = []
    
    for day_sec in day_sections:
        day_id = day_sec.get('id', 'unknown')
        
        # Check elements inside this day section
        # Theory/code examples
        code_blocks = day_sec.find_all('pre')
        has_code = len(code_blocks) > 0
        
        # Check imports in code blocks
        missing_imports = []
        code_text = " ".join([c.get_text() for c in code_blocks])
        # If code contains pandas/np/tf/torch/plt but no import, flag it
        if 'pd.' in code_text and 'import pandas' not in code_text:
            missing_imports.append('pandas')
        if 'np.' in code_text and 'import numpy' not in code_text:
            missing_imports.append('numpy')
        if 'plt.' in code_text and 'matplotlib.pyplot' not in code_text:
            missing_imports.append('matplotlib')
        if 'torch.' in code_text and 'import torch' not in code_text:
            missing_imports.append('torch')
        if 'tf.' in code_text and 'import tensorflow' not in code_text:
            missing_imports.append('tensorflow')
            
        # Quiz
        quiz_blocks = day_sec.find_all(class_=re.compile(r'\bquiz-block\b'))
        has_quiz = len(quiz_blocks) > 0
        quiz_count = len(quiz_blocks)
        
        # Flashcards
        flashcard_grid = day_sec.find_all(class_=re.compile(r'\bflashcard-grid\b'))
        flashcards = day_sec.find_all(class_=re.compile(r'\bflashcard\b'))
        has_flashcards = len(flashcards) > 0
        flashcard_count = len(flashcards)
        
        # Tasks
        task_blocks = day_sec.find_all(class_=re.compile(r'\btask-block\b'))
        has_tasks = len(task_blocks) > 0
        task_count = len(task_blocks)
        
        # Resources
        resources_grid = day_sec.find_all(class_=re.compile(r'\b(resources-grid|res-grid)\b'))
        resources = day_sec.find_all(class_=re.compile(r'\b(resource-card|res-card)\b'))
        # also tables
        res_tables = day_sec.find_all(class_=re.compile(r'\b(resource-table|res-table)\b'))
        has_resources = len(resources) > 0 or len(res_tables) > 0
        resource_count = len(resources) + len(res_tables)
        
        # Predict the output
        predict_blocks = day_sec.find_all(class_=re.compile(r'\bpredict-block\b'))
        has_predict = len(predict_blocks) > 0
        
        # Misconception
        misconception_blocks = day_sec.find_all(class_=re.compile(r'\bmisconception\b'))
        has_misconception = len(misconception_blocks) > 0
        
        # Hinglish
        hinglish_blocks = day_sec.find_all(class_=re.compile(r'\bhinglish\b'))
        has_hinglish = len(hinglish_blocks) > 0
        
        # Mermaid
        mermaid_blocks = day_sec.find_all(class_=re.compile(r'\bmermaid\b'))
        has_mermaid = len(mermaid_blocks) > 0
        mermaid_count = len(mermaid_blocks)
        
        # XP value
        complete_btn = day_sec.find(class_='complete-btn')
        xp_value = None
        if complete_btn:
            xp_match = re.search(r'completeDay\(\d+,\s*(\d+)\)', complete_btn.get('onclick', ''))
            if xp_match:
                xp_value = int(xp_match.group(1))
            else:
                # search text
                xp_text_match = re.search(r'(\d+)\s*XP', complete_btn.get_text())
                if xp_text_match:
                    xp_value = int(xp_text_match.group(1))
        
        # Git commit message check
        commit_msg_match = re.search(r'(Git commit message|Commit message|Suggested commit):?\s*`([^`]+)`', day_sec.get_text(), re.IGNORECASE)
        commit_msg = commit_msg_match.group(2) if commit_msg_match else None
        
        days_data.append({
            'day_id': day_id,
            'has_code': has_code,
            'missing_imports': missing_imports,
            'has_quiz': has_quiz,
            'quiz_count': quiz_count,
            'has_flashcards': has_flashcards,
            'flashcard_count': flashcard_count,
            'has_tasks': has_tasks,
            'task_count': task_count,
            'has_resources': has_resources,
            'resource_count': resource_count,
            'has_predict': has_predict,
            'has_misconception': has_misconception,
            'has_hinglish': has_hinglish,
            'has_mermaid': has_mermaid,
            'mermaid_count': mermaid_count,
            'xp_value': xp_value,
            'commit_msg': commit_msg
        })
        
    # Get all external links in resources
    links = []
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('http'):
            # Find parent section
            parent = a.find_parent(class_=re.compile(r'\b(day-section|resources-grid|res-grid|resource-table|res-table)\b'))
            parent_id = 'global'
            if parent:
                parent_id = parent.get('id', 'unknown')
            links.append({'url': href, 'text': a.get_text().strip(), 'day': parent_id})
            
    return {
        'days': days_data,
        'links': links
    }

print("Running quality check on all weeks...")
results = {}
for w in range(1, 19):
    fn = f"week{w}.html"
    res = audit_file(fn)
    if res:
        results[w] = res
        print(f"Audited {fn}: found {len(res['days'])} days, {len(res['links'])} external links.")

# Write a quick JSON report
import json
with open(os.path.join(base_dir, "scratch/audit_report.json"), "w") as f:
    json.dump(results, f, indent=2)
print("Saved raw audit data to scratch/audit_report.json")
