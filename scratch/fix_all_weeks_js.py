import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

target_bad = """  function hide() {
    modalElement.style.opacity = '0';
    modalElement.querySelector('div').style.transform = 'scale(0.9)';
    setTimeout(() => {
      modalElement.style.display = 'none';
    }, 250);
  }

  show();
});
  }
}"""

target_good = """  function hide() {
    modalElement.style.opacity = '0';
    modalElement.querySelector('div').style.transform = 'scale(0.9)';
    setTimeout(() => {
      modalElement.style.display = 'none';
    }, 250);
  }

  show();
}"""

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    
    content = open(path, "r", encoding="utf-8").read()
    
    if target_bad in content:
        new_content = content.replace(target_bad, target_good)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ week{w}.html: Repaired showCompilerModal syntax.")
    else:
        # Let's search with dynamic whitespaces just in case
        normalized_content = content.replace("\r\n", "\n")
        # Let's replace using regex or string replace if line endings are different
        # Let's try direct replace with normalized content
        target_bad_norm = target_bad.replace("\r\n", "\n")
        target_good_norm = target_good.replace("\r\n", "\n")
        if target_bad_norm in normalized_content:
            new_content = normalized_content.replace(target_bad_norm, target_good_norm)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ week{w}.html: Repaired showCompilerModal syntax (normalized).")
        else:
            print(f"❌ week{w}.html: Target string not found!")

print("Repair complete.")
