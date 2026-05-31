import os

worktrees_dir = "/Users/amananand/.gemini/antigravity/worktrees"
if os.path.exists(worktrees_dir):
    print("Listing files in worktrees:")
    for root, dirs, files in os.walk(worktrees_dir):
        for f in files:
            if f.endswith('.html'):
                print("  -", os.path.join(root, f))
else:
    print("worktrees directory does not exist")
