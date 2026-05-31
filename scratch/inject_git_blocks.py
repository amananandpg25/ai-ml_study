import os
import re
from bs4 import BeautifulSoup

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def inject_git_blocks():
    print("Starting git-block injection...")
    
    capstones = {
        30: "math & prep mastery capstone project",
        58: "cifar-10 classification flask endpoint capstone",
        65: "end-to-end visual classification pipeline capstone",
        72: "movie review sentiment classifier deployment capstone",
        79: "dcgan model checkpointing and generation capstone",
        86: "seq2seq attention image captioning gradio capstone",
        93: "extractive text summarization pipeline capstone",
        100: "fastapi and docker model serving capstone",
        111: "agentic retrieval and execution pipeline capstone",
        117: "next.js full-stack production rag deployment capstone",
        124: "production flask docker compose ml stack capstone",
        135: "kubernetes cluster deployment and system graduation capstone"
    }

    for w in range(1, 19):
        fn = f"week{w}.html"
        path = os.path.join(base_dir, fn)
        if not os.path.exists(path):
            continue
            
        html = open(path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(html, 'html.parser')
        
        day_sections = soup.find_all(class_=re.compile(r'\bday-section\b'))
        modified = False
        
        for day_sec in day_sections:
            day_id = day_sec.get('id', 'unknown')
            if day_id == 'unknown' or 'toolkit' in day_id:
                continue
                
            # Extract day number
            day_num_match = re.search(r'\d+', day_id)
            if not day_num_match:
                continue
            day_num = int(day_num_match.group())
            
            git_blocks = day_sec.find_all(class_=re.compile(r'\bgit-block\b'))
            if git_blocks:
                # Already has git block, skip
                continue
                
            # Find the first task block
            task_blocks = day_sec.find_all(class_=re.compile(r'\btask-block\b'))
            if not task_blocks:
                print(f"⚠️ Week {w}, Day {day_num}: No tasks found to inject git-block.")
                continue
                
            first_task = task_blocks[0]
            task_body = first_task.find(class_=re.compile(r'\btask-body\b'))
            if not task_body:
                # Fallback to direct child
                task_body = first_task
                
            done_when = task_body.find(class_=re.compile(r'\bdone-when\b'))
            
            # Create git-block element
            new_git = soup.new_tag('div')
            new_git['class'] = 'git-block'
            
            commit_desc = capstones.get(day_num, f"complete day {day_num} tasks and coding exercises")
            new_git.string = f'git add . && git commit -m "day{day_num}: {commit_desc}"'
            
            if done_when:
                # Insert after done-when
                done_when.insert_after(new_git)
            else:
                # Append to task body
                task_body.append(new_git)
                
            print(f"✅ Week {w}, Day {day_num}: Injected git-block.")
            modified = True
            
        if modified:
            # Save the file
            # Format the soup output nicely without breaking formatting
            with open(path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"💾 Saved updates to {fn}")

inject_git_blocks()
