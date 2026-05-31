with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="resources-section"')
# Let's find Day 61 resources
idx = content.find('Day 61 Resources — ResNet & Norm')
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Not found Day 61 resources")
