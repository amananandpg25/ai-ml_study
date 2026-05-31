import os
import glob
import time

now = time.time()
two_hours = 2 * 60 * 60

search_paths = [
    "/Users/amananand/Downloads/**/*.html",
    "/Users/amananand/Desktop/**/*.html",
    "/Users/amananand/Documents/**/*.html",
    "/Users/amananand/Downloads/*.html",
    "/Users/amananand/Desktop/*.html",
    "/Users/amananand/Documents/*.html",
]

print("Searching for HTML files modified in the last 2 hours:")
found = False
for path in search_paths:
    for f in glob.glob(path, recursive=True):
        try:
            mtime = os.path.getmtime(f)
            if now - mtime < two_hours:
                print(f"  - {f} (size: {os.path.getsize(f)} bytes, modified: {time.ctime(mtime)})")
                found = True
        except Exception as e:
            pass

if not found:
    print("No HTML files found in last 2 hours.")
