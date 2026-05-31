with open('/Users/amananand/Downloads/SDE/ai:ml/week12.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 81 start and end
day81_start = content.find('id="day-81"')
day82_start = content.find('id="day-82"')

if day81_start != -1 and day82_start != -1:
    day81_block = content[day81_start:day82_start]
    
    m_idx = day81_block.find('<div class="mermaid">')
    if m_idx != -1:
        m_end = day81_block.find('</div>', m_idx)
        if m_end != -1:
            old_m = day81_block[m_idx:m_end+6]
            new_m = """    <div class="mermaid">
      graph LR
      Img[Input Image] --> CNN[CNN Encoder: e.g. ResNet] --> Features[Feature Map / Context Vector v]
      Features --> LSTM[LSTM Decoder: Day 81] --> Outputs["Output Word Sequence: [A, cat, sitting, ...]"]
      LSTM -. Feed previous word .-> LSTM
    </div>"""
            new_day81_block = day81_block.replace(old_m, new_m)
            content = content.replace(day81_block, new_day81_block)
            print("Successfully updated Day 81 diagram in week12.html!")
        else:
            print("Could not find closing </div> for mermaid")
    else:
        print("Could not find mermaid block in Day 81")
else:
    print("Day 81 indices not found")

with open('/Users/amananand/Downloads/SDE/ai:ml/week12.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved week12.html")
