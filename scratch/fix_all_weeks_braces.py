import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# We want to replace the double closing braces at the end of checkPredict
# and right before openRepl()

bad_snippet = """    result.textContent = '❌ Expected: ' + answer.replace(/\\n/g, ' ') + ' — try again';
  }
}
}

function openRepl()"""

good_snippet = """    result.textContent = '❌ Expected: ' + answer.replace(/\\n/g, ' ') + ' — try again';
  }
}

function openRepl()"""

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    
    content = open(path, "r", encoding="utf-8").read()
    
    # Let's normalize newlines to make match reliable
    content_norm = content.replace("\r\n", "\n")
    bad_norm = bad_snippet.replace("\r\n", "\n")
    good_norm = good_snippet.replace("\r\n", "\n")
    
    if bad_norm in content_norm:
        new_content = content_norm.replace(bad_norm, good_norm)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ week{w}.html: Removed extra closing brace before openRepl().")
    else:
        # Let's try matching with single quotes or different whitespace
        # Let's see if we can search for the end of checkPredict
        # We can find checkPredict and replace the double curly braces
        print(f"❌ week{w}.html: Snippet not found, trying fallback matching.")
        # Fallback: search for "function checkPredict" then the closing of it before openRepl
        # Let's look at what is between the end of checkPredict and openRepl
        # Since it is a small file edit, let's write a regex that matches } } \s* function openRepl
        pattern = r'\}\s*\}\s*\}\s*function\s+openRepl\s*\('
        # Wait, if we have 3 closing braces: 1 for else block, 1 for checkPredict function, 1 extra.
        # So we match } } } and replace with } }
        content_replaced, count = os.path.subn if hasattr(os, 'subn') else (None, 0)
        import re
        content_replaced, count = re.subn(r'\}\s*\}\s*\}\s*function\s+openRepl\s*\(', r'}\n}\n\nfunction openRepl(', content_norm)
        if count > 0:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content_replaced)
            print(f"✅ week{w}.html: Removed extra brace using regex fallback (matched {count} times).")
        else:
            print(f"❌ week{w}.html: Fallback matching failed too!")

print("Brace clean complete.")
