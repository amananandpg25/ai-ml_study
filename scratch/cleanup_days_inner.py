import os
import re
from bs4 import BeautifulSoup

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def clean_inner_content(html_fragment):
    # Wrap in a dummy div to ensure a single root and valid parsing
    soup = BeautifulSoup(f"<div id='dummy-root'>{html_fragment}</div>", 'html.parser')
    root = soup.find(id='dummy-root')
    if not root:
        return html_fragment
        
    # 1. Clean predict-blocks
    predicts = root.find_all(class_='predict-block')
    if len(predicts) > 1:
        keep_p = predicts[0]
        extra_elements = []
        for dup_p in predicts[1:]:
            # Extract nested callouts or other blocks from duplicate predict-blocks
            # We want to extract callouts, misconceptions, or ml-connect blocks
            nested_blocks = dup_p.find_all(class_=['callout', 'misconception', 'ml-connect'])
            for nb in nested_blocks:
                nb_extracted = nb.extract()
                extra_elements.append(nb_extracted)
            dup_p.decompose()
            
        # Append extra elements after the kept predict-block
        current = keep_p
        for elem in extra_elements:
            current.insert_after(elem)
            current = elem

    # 2. Clean analogies (deduplicate identical ones)
    analogies = root.find_all(class_='analogy')
    seen_analogies = set()
    for a in list(analogies):
        text = a.get_text(strip=True).lower()
        if text in seen_analogies:
            a.decompose()
        else:
            seen_analogies.add(text)

    # 3. Clean hinglish takeaways (deduplicate identical ones)
    hinglishes = root.find_all(class_='hinglish')
    seen_hinglish = set()
    for h in list(hinglishes):
        text = h.get_text(strip=True).lower()
        if text in seen_hinglish:
            h.decompose()
        else:
            seen_hinglish.add(text)

    # 4. Clean misconceptions (deduplicate identical ones)
    misconceptions = root.find_all(class_='misconception')
    seen_misconceptions = set()
    for m in list(misconceptions):
        text = m.get_text(strip=True).lower()
        if text in seen_misconceptions:
            m.decompose()
        else:
            seen_misconceptions.add(text)

    # Reconstruct the inner HTML of dummy root
    cleaned_fragment = "".join(str(child) for child in root.contents)
    return cleaned_fragment

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
        
    print(f"Cleaning inner content in week{w}.html...")
    content = open(path, 'r', encoding='utf-8').read()
    
    day_matches = list(re.finditer(r'(<div\s+class="day-section[^"]*"\s+id="day-(\d+)">)', content))
    if not day_matches:
        continue
        
    new_content = ""
    last_idx = 0
    
    for i in range(len(day_matches)):
        start_match = day_matches[i]
        d_num = int(start_match.group(2))
        start_idx = start_match.start()
        body_start = start_match.end()
        
        # Determine day_limit to search for closing tag
        if i + 1 < len(day_matches):
            day_limit = day_matches[i+1].start()
        else:
            # Fallback for the end of the last day section
            day_limit = content.find("<!-- Sidebar -->", body_start)
            if day_limit == -1:
                day_limit = content.find("<!-- Scripts -->", body_start)
            if day_limit == -1:
                day_limit = content.find("<script>", body_start)
            if day_limit == -1:
                day_limit = len(content)
                
        # Find all closing </div> tags in the search range [body_start, day_limit]
        div_closes = [m.start() for m in re.finditer(r'</div>', content[body_start:day_limit])]
        if not div_closes:
            print(f"  Warning: No closing div found for Day {d_num}")
            # Fallback
            body_end = day_limit
        else:
            # The closing tag of the day section is the last </div> before day_limit
            body_end = body_start + div_closes[-1]
            
        # Append text from last_idx up to body_start
        new_content += content[last_idx:body_start]
        
        # Clean the day's inner content
        day_inner_content = content[body_start:body_end]
        cleaned_inner = clean_inner_content(day_inner_content)
        
        new_content += cleaned_inner
        last_idx = body_end
        
    # Append the remainder of the file
    new_content += content[last_idx:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Finished week{w}.html")
