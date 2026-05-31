with open('/Users/amananand/Downloads/SDE/ai:ml/_backup/week13.html', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# Let's write the backup content back to week13.html to restore it
with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'w', encoding='utf-8') as f:
    f.write(backup_content)
print("Restored week13.html from backup!")
