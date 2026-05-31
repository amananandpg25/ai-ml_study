import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def fix_file_robustly(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # We find all occurrences of '<div class="day-section"'
    # For each, we check if it is malformed.
    # We find the start index of '<div class="day-section"'
    
    # We can use a regex to find all start tags of day-section, even if they span multiple lines
    # and don't close with '>' immediately.
    # Let's search for '<div class="day-section"'
    starts = [m.start() for m in re.finditer(r'<div\s+class="day-section"', content)]
    if not starts:
        return
        
    modified = False
    new_content = content
    
    # Process from the end of the file to the beginning to avoid index offset issues
    for start_idx in reversed(starts):
        # Find the next '<div class="day-header">' or similar which marks the start of the actual content
        m = re.search(r'<div\s+[^>]*class=["\'](?:day-header|day-tag|day-section)["\']', new_content[start_idx + 1:])
        if m:
            header_idx = start_idx + 1 + m.start()
        else:
            header_idx = len(new_content)
            
        # The substring containing the malformed opening tag and any swallowed elements
        substring = new_content[start_idx:header_idx]
        
        # Check if it has a closing '>' before the first inner tag starts.
        # An inner tag starts with '<' at some position after the opening '<div'
        first_inner_lt = substring.find('<', 1)
        first_gt = substring.find('>')
        
        # If there is no '>' or the first '<' (which represents an inner tag) appears before the first '>',
        # then it is malformed!
        if first_gt == -1 or (first_inner_lt != -1 and first_inner_lt < first_gt):
            # It's malformed!
            print(f"week{w}.html: Found malformed day-section at index {start_idx}.")
            
            # Find the day number from id="day-XXX" inside the substring
            id_match = re.search(r'id="day-(\d+)"', substring)
            if not id_match:
                print(f"  WARNING: Could not find day ID in malformed section at index {start_idx}!")
                continue
                
            day_num = id_match.group(1)
            
            # Construct the replacement by keeping everything after the first inner '<' tag
            replacement = f'<div class="day-section" id="day-{day_num}">\n  ' + substring[first_inner_lt:]
            
            # Replace in new_content
            new_content = new_content[:start_idx] + replacement + new_content[start_idx + len(substring):]
            modified = True
            print(f"  Fixed day-{day_num} successfully.")
            
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"week{w}.html: Saved changes.")

if __name__ == '__main__':
    for w in range(1, 18):
        fix_file_robustly(w)
