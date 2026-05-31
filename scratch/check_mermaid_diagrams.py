import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def check_mermaid():
    for w in range(1, 18):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        content = open(path, 'r', encoding='utf-8').read()
        
        # Find all divs or elements with class="mermaid"
        mermaid_blocks = re.findall(r'<div class=\"mermaid\">(.*?)</div>', content, re.DOTALL)
        mermaid_blocks_alt = re.findall(r'<pre class=\"mermaid\">(.*?)</pre>', content, re.DOTALL)
        
        blocks = mermaid_blocks + mermaid_blocks_alt
        if blocks:
            print(f"\nweek{w}.html: Found {len(blocks)} Mermaid blocks")
            for idx, block in enumerate(blocks):
                # Clean up block
                block_clean = block.strip()
                # Check for unescaped characters or typical syntax issues
                has_unescaped_amp = '&amp;' in block_clean
                has_unescaped_lt = '&lt;' in block_clean
                has_unescaped_gt = '&gt;' in block_clean
                
                # Check for brackets or parentheses inside node names that could break parsing
                # e.g., id[Text (with parens)] instead of id["Text (with parens)"]
                broken_brackets = re.findall(r'\b\w+\[[^\]]*\([^)]*\)[^\]]*\]', block_clean)
                broken_parens = re.findall(r'\b\w+\([^)]*\[[^\]]*\][^)]*\)', block_clean)
                
                print(f"  Block {idx+1}: length={len(block_clean)}, has_amp={has_amp(block_clean)}, has_lt={has_lt(block_clean)}, has_gt={has_gt(block_clean)}")
                if broken_brackets:
                    print(f"    WARNING: Suspected broken brackets in block {idx+1}: {broken_brackets}")
                if broken_parens:
                    print(f"    WARNING: Suspected broken parentheses in block {idx+1}: {broken_parens}")
                
                # Verify parentheses are balanced in the block
                open_p = block_clean.count('(')
                close_p = block_clean.count(')')
                open_b = block_clean.count('[')
                close_b = block_clean.count(']')
                open_c = block_clean.count('{')
                close_c = block_clean.count('}')
                
                if open_p != close_p or open_b != close_b or open_c != close_c:
                    print(f"    WARNING: Unbalanced parentheses/brackets/braces in block {idx+1}!")
                    print(f"      ( ) counts: {open_p} vs {close_p}")
                    print(f"      [ ] counts: {open_b} vs {close_b}")
                    print(f"      {{ }} counts: {open_c} vs {close_c}")

def has_amp(text):
    return '&' in text and '&amp;' not in text

def has_lt(text):
    return '<' in text and '&lt;' not in text

def has_gt(text):
    return '>' in text and '&gt;' not in text

if __name__ == '__main__':
    check_mermaid()
