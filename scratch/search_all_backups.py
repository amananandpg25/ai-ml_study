import os

brain_dir = "/Users/amananand/.gemini/antigravity/brain"
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if 'week13' in f:
            print("Found week13 file in brain:", os.path.join(root, f))
