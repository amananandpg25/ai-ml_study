import os
import glob

# Search in Downloads and workspace
search_paths = [
    "/Users/amananand/Downloads/*audit*",
    "/Users/amananand/Downloads/*Audit*",
    "/Users/amananand/Downloads/SDE/*audit*",
    "/Users/amananand/Downloads/SDE/*Audit*",
    "/Users/amananand/Downloads/SDE/ai:ml/*audit*",
    "/Users/amananand/Downloads/SDE/ai:ml/*Audit*",
    "/Users/amananand/.gemini/antigravity/**/*audit*",
    "/Users/amananand/.gemini/antigravity/**/*Audit*"
]

for pattern in search_paths:
    files = glob.glob(pattern, recursive=True)
    if files:
        print(f"Pattern '{pattern}' matched:")
        for f in files:
            print(f"  - {f} (size: {os.path.getsize(f)} bytes)")
