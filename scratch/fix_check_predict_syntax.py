import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# The target dangling string to remove.
# We will match it and replace it with an empty string.
TARGET_DANGLING = """} else {
    result.style.background = 'rgba(229,107,140,.08)';
    result.style.border = '1px solid rgba(229,107,140,.3)';
    result.style.color = 'var(--pink)';
    result.style.borderRadius = '6px';
    result.style.padding = '.5rem .8rem';
    result.textContent = '❌ Expected: ' + answer + ' — try again';
  }
}"""

def fix_dangling_blocks():
    for w in range(1, 18):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        content = open(path, 'r', encoding='utf-8').read()
        
        # We also check if it contains the target block
        if TARGET_DANGLING in content:
            new_content = content.replace(TARGET_DANGLING, "")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"week{w}.html: Successfully removed dangling else block.")
        else:
            # Let's check with standard normalizing or a slightly different spacing if any
            normalized_dangling = TARGET_DANGLING.replace('\r\n', '\n')
            normalized_content = content.replace('\r\n', '\n')
            if normalized_dangling in normalized_content:
                new_content = normalized_content.replace(normalized_dangling, "")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"week{w}.html: Successfully removed dangling else block (normalized path).")
            else:
                print(f"week{w}.html: Target dangling block NOT found!")

if __name__ == '__main__':
    fix_dangling_blocks()
