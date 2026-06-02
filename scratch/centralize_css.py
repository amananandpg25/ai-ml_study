import os
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# Explicit RGB values
RGB_MAP = {
    "green": "79, 209, 165",
    "blue": "108, 140, 255",
    "orange": "247, 169, 75",
    "pink": "229, 107, 140",
    "purple": "180, 124, 252",
    "yellow": "245, 215, 110",
    "teal": "56, 189, 248"
}

# Mapping of week to its accent and secondary colors
WEEK_THEMES = {
    1: ("green", "blue"),
    2: ("blue", "purple"),
    3: ("blue", "purple"),
    4: ("blue", "purple"),
    5: ("blue", "teal"),
    6: ("blue", "teal"),
    7: ("purple", "blue"),
    8: ("teal", "blue"),
    9: ("orange", "yellow"),
    10: ("orange", "yellow"),
    11: ("purple", "pink"),
    12: ("purple", "pink"),
    13: ("purple", "pink"),
    14: ("pink", "purple"),
    15: ("teal", "purple"),
    16: ("purple", "pink"),
    17: ("green", "teal"),
    18: ("green", "teal")
}

def centralize_week(week_num):
    filename = f"week{week_num}.html"
    path = os.path.join(workspace_dir, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return False
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if there is a <style> tag
    style_matches = list(re.finditer(r'<style>(.*?)</style>', content, re.DOTALL))
    if not style_matches:
        print(f"No <style> block found in {filename}!")
        return False
        
    if len(style_matches) > 1:
        print(f"Warning: Multiple <style> blocks found in {filename} ({len(style_matches)})!")
        
    # We will replace the first style block
    target_match = style_matches[0]
    start, end = target_match.span()
    
    # Generate new style block
    accent_name, sec_name = WEEK_THEMES[week_num]
    accent_val = RGB_MAP[accent_name]
    sec_val = RGB_MAP[sec_name]
    
    new_style_block = f"""<style>
:root {{
  --accent-rgb: {accent_val};
  --accent-sec-rgb: {sec_val};
}}
</style>
<link rel="stylesheet" href="course.css">"""
    
    new_content = content[:start] + new_style_block + content[end:]
    
    # Save the updated file
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully centralized CSS in {filename} (Accent: {accent_name}, Secondary: {sec_name})")
    return True

if __name__ == "__main__":
    success_count = 0
    for w in range(1, 19):
        if centralize_week(w):
            success_count += 1
    print(f"\nCompleted! Centralized CSS in {success_count}/18 week files.")
