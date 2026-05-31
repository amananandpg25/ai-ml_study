import os

brain_dir = "/Users/amananand/.gemini/antigravity/brain"
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if 'week13' in f or 'replace_week13' in f:
            print("Found file:", os.path.join(root, f))
        elif f.endswith('.html'):
            print("Found HTML file:", os.path.join(root, f))
