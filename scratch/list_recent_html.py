import os
import glob
import time

downloads_dir = "/Users/amananand/Downloads"
html_files = glob.glob(os.path.join(downloads_dir, "*.html"))

# Sort by modification time
html_files.sort(key=os.path.getmtime, reverse=True)

print("Recent HTML files in Downloads:")
for f in html_files[:10]:
    mtime = time.ctime(os.path.getmtime(f))
    size = os.path.getsize(f)
    print(f"  - {f} (size: {size} bytes, modified: {mtime})")
