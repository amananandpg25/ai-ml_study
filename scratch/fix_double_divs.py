import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def fix_file(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Pattern 1: <div <div style="display:flex; ...">
    # Wait, some files might have '<div <div style=' or '<div  <div style=' or even '<div <div' on different lines
    p1 = r'<div\s+<div\s+style="display:flex;\s*justify-content:space-between;\s*align-items:center;\s*width:100%;\s*margin-bottom:5px;">'
    r1 = r'<div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">'
    
    # We do a direct string replace if it matches exactly, or a regex if there are slight spacing differences
    content_new, count1 = re.subn(p1, r1, content)
    
    # Pattern 2: <div class="res-type" style="...">TYPE</div>">TYPE</div>
    # Let's match:
    # <div class="res-type" style="[style]">[TYPE]</div>">[TYPE]</div>
    # or:
    # <div class="res-type" style="">[TYPE]</div>">[TYPE]</div>
    # or:
    # <div class="res-type">[TYPE]</div>">[TYPE]</div>
    p2 = r'<div\s+class="res-type"([^>]*)>([^<]*)</div>">\2</div>'
    r2 = r'<div class="res-type"\1>\2</div>'
    
    content_new, count2 = re.subn(p2, r2, content_new)
    
    # Also support single quotes or different tags just in case
    # Let's check for any other variations of '<div <div' or '<div  <div'
    # E.g., <div <div style=...
    p3 = r'<div\s+<div\b'
    r3 = r'<div'
    content_new, count3 = re.subn(p3, r3, content_new)
    
    # And check if there are remaining '">TYPE</div>' that were not caught
    # We can search for '</div>">[A-Za-z0-9 &;\.\-]+</div>'
    p4 = r'</div>">([A-Za-z0-9 &;\.\-\u00b7]+)</div>'
    # Let's see: we want to replace '</div>">TYPE</div>' with '</div>'
    content_new, count4 = re.subn(p4, r'</div>', content_new)
    
    if count1 or count2 or count3 or count4:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"week{w}.html: Fixed {count1} headers, {count2} res-types, {count3} double divs, {count4} trailing res-types.")
    else:
        print(f"week{w}.html: No double-div issues found.")

if __name__ == '__main__':
    for w in range(1, 18):
        fix_file(w)
