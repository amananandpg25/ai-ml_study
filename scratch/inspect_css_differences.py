import os
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
weeks = [f"week{i}.html" for i in range(1, 19)]

print("Scanning CSS definitions in week HTML files...")

for w in weeks:
    path = os.path.join(workspace_dir, w)
    if not os.path.exists(path):
        print(f"File not found: {w}")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        print(f"{w}: No <style> tag found!")
        continue
        
    style_text = style_match.group(1)
    
    # Check for variables definition
    root_match = re.search(r':root\s*{(.*?)}', style_text, re.DOTALL)
    
    # Check for .brand definition
    brand_match = re.search(r'\.brand\s*{(.*?)}', style_text)
    
    # Check for .prog-inner definition
    prog_inner_match = re.search(r'\.prog-inner\s*{(.*?)}', style_text)
    
    # Check for week-specific custom definitions that don't match the general boilerplate
    # Let's count some selectors
    selectors = re.findall(r'([^{]+)\s*\{', style_text)
    selectors_clean = [s.strip() for s in selectors if not s.strip().startswith('@')]
    
    print(f"\n=== {w} ===")
    if root_match:
        print(f"  Root variables: {root_match.group(1).strip()}")
    if brand_match:
        print(f"  .brand: {brand_match.group(1).strip()}")
    if prog_inner_match:
        print(f"  .prog-inner: {prog_inner_match.group(1).strip()}")
    
    # Check if there are any selectors that are unique or not present in week2.html style
    # E.g. search for .concept-map-flow or anything inline in files.
    # Note: we are just looking for CSS selectors defined in the style block.
