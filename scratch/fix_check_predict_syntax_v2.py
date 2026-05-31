import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

TARGET = """  } else {
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer.replace(/\\n/g, ' ') + ' — try again';
  }"""

REPLACEMENT = """  } else {
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer.replace(/\\n/g, ' ') + ' — try again';
  }
}"""

def add_closing_braces():
    for w in range(1, 18):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        content = open(path, 'r', encoding='utf-8').read()
        
        # Check if the TARGET block is present
        if TARGET in content:
            # First, check if the REPLACEMENT is already present to prevent double curly braces
            if REPLACEMENT in content:
                print(f"week{w}.html: Already has the closing brace.")
            else:
                new_content = content.replace(TARGET, REPLACEMENT)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"week{w}.html: Added closing brace to checkPredict.")
        else:
            # Normalized check
            normalized_target = TARGET.replace('\r\n', '\n')
            normalized_replacement = REPLACEMENT.replace('\r\n', '\n')
            normalized_content = content.replace('\r\n', '\n')
            if normalized_target in normalized_content:
                if normalized_replacement in normalized_content:
                    print(f"week{w}.html: Already has the closing brace (normalized).")
                else:
                    new_content = normalized_content.replace(normalized_target, normalized_replacement)
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"week{w}.html: Added closing brace to checkPredict (normalized).")
            else:
                print(f"week{w}.html: TARGET block NOT found!")

if __name__ == '__main__':
    add_closing_braces()
