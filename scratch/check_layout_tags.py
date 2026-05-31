import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def check_structure(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # We want to check:
    # 1. Is <div class="layout"> present?
    # 2. Is <div class="main"> or <main> present?
    # 3. Where are they opened and closed?
    
    has_layout = 'class="layout"' in content or "class='layout'" in content
    has_main = 'class="main"' in content or "class='main'" in content or "<main>" in content
    
    layout_open = content.find('class="layout"')
    if layout_open == -1:
        layout_open = content.find("class='layout'")
        
    main_open = content.find('class="main"')
    if main_open == -1:
        main_open = content.find("class='main'")
    if main_open == -1:
        main_open = content.find('<main>')
        
    # Check if there are multiple layout or main divs
    layout_count = content.count('class="layout"') + content.count("class='layout'")
    main_count = content.count('class="main"') + content.count("class='main'") + content.count('<main>')
    
    print(f"week{w}.html | layout_count={layout_count}, main_count={main_count}")
    if layout_count == 0 or main_count == 0:
        print(f"  WARNING: Missing layout/main containers!")

if __name__ == '__main__':
    for w in range(1, 18):
        check_structure(w)
