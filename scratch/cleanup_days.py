import os
import re
from bs4 import BeautifulSoup, Comment

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def clean_day_section(day_id, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Clean predict-blocks
    predicts = soup.find_all(class_='predict-block')
    if len(predicts) > 1:
        keep_p = predicts[0]
        # Collect callouts and other non-standard children from duplicate predict blocks
        extra_elements = []
        for dup_p in predicts[1:]:
            # Find any callout nested in the duplicate predict-block
            callouts = dup_p.find_all(class_='callout')
            for c in callouts:
                # Extract and keep
                c_extract = c.extract()
                extra_elements.append(c_extract)
            # Remove the duplicate predict-block itself
            dup_p.decompose()
        
        # Insert extra elements after the kept predict-block
        current = keep_p
        for elem in extra_elements:
            current.insert_after(elem)
            current = elem

    # 2. Clean analogies
    analogies = soup.find_all(class_='analogy')
    seen_analogies = set()
    for a in list(analogies):
        text = a.get_text(strip=True).lower()
        if text in seen_analogies:
            a.decompose()
        else:
            seen_analogies.add(text)

    # 3. Clean hinglish takeaways
    # Only clean if they are identical in content
    hinglish_elements = soup.find_all(class_='hinglish')
    seen_hinglish = set()
    for h in list(hinglish_elements):
        text = h.get_text(strip=True).lower()
        if text in seen_hinglish:
            h.decompose()
        else:
            seen_hinglish.add(text)

    # 4. Clean misconceptions
    misconceptions = soup.find_all(class_='misconception')
    seen_misconceptions = set()
    for m in list(misconceptions):
        text = m.get_text(strip=True).lower()
        if text in seen_misconceptions:
            m.decompose()
        else:
            seen_misconceptions.add(text)

    # Return the cleaned HTML as string (decode without adding extra outer wrapper)
    return soup.decode()

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
        
    print(f"Processing week{w}.html...")
    content = open(path, 'r', encoding='utf-8').read()
    
    # We want to find each day section, extract it, clean it, and replace it.
    # To preserve formatting outside day sections, we find days by splitting or regex.
    day_matches = list(re.finditer(r'(<div\s+class="day-section[^"]*"\s+id="day-(\d+)">)', content))
    if not day_matches:
        continue
        
    # We will reconstruct the content by replacing each day section body.
    new_content = ""
    last_idx = 0
    
    for i in range(len(day_matches)):
        start_match = day_matches[i]
        d_num = int(start_match.group(2))
        start_idx = start_match.start()
        
        # Find the end of this day section.
        # It ends either at the next day section, or at the day section close marker, or at the end of the layout.
        if i + 1 < len(day_matches):
            end_idx = day_matches[i+1].start()
        else:
            # Last day section in the file.
            # Usually ends at the container close before sidebar/footer or script.
            # We can find the end of the day section by searching for the closing tag or script.
            # Let's search for "<!-- /day-" or "</div>\n\n<!-- ==" or similar.
            end_idx = content.find("</div><!-- /day-", start_idx)
            if end_idx == -1:
                end_idx = content.find("</div>\n<!-- ═════", start_idx)
            if end_idx == -1:
                # Fallback: search for layout container end or script
                end_idx = content.find("<!-- Sidebar -->", start_idx)
            if end_idx == -1:
                end_idx = content.find("<!-- Scripts -->", start_idx)
            if end_idx == -1:
                end_idx = content.find("<script>", start_idx)
            if end_idx == -1:
                end_idx = len(content)
        
        # Append content before this day section
        new_content += content[last_idx:start_idx]
        
        day_block = content[start_idx:end_idx]
        # Clean the day section HTML using BeautifulSoup
        cleaned_day_block = clean_day_section(d_num, day_block)
        
        new_content += cleaned_day_block
        last_idx = end_idx
        
    # Append the remainder
    new_content += content[last_idx:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Finished week{w}.html")
