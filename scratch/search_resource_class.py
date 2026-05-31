with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'resource-', content)]
print(f"Found {len(matches)} occurrences of 'resource-':")
for idx in matches[:10]:
    print("  - Context:", repr(content[idx-40:idx+120]))
    
matches2 = [m.start() for m in re.finditer(r'resources-', content)]
print(f"Found {len(matches2)} occurrences of 'resources-':")
for idx in matches2[:10]:
    print("  - Context:", repr(content[idx-40:idx+120]))
