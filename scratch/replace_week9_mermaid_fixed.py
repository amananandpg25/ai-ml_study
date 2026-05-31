with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_diagrams = {
    60: """    <div class="mermaid">
      graph TD
      Input["4x4 Input Matrix"] --> MaxP["Max Pooling (2x2 kernel, stride 2) <br/> Takes the maximum value from each quadrant"]
      Input --> AvgP["Average Pooling (2x2 kernel, stride 2) <br/> Takes the average value from each quadrant"]
      MaxP --> MaxOut["2x2 Output (Reduces parameters, extracts dominant features)"]
      AvgP --> AvgOut["2x2 Output (Reduces parameters, smooths features)"]
    </div>""",
    61: """    <div class="mermaid">
      graph TD
      Feat["Feature Map: (H x W x C)"] --> Flat["Flattening: <br/> Concatenates all elements into a vector (H*W*C) <br/> Leads to parameter explosion in Dense layer"]
      Feat --> GAP["Global Average Pooling (GAP): <br/> Computes average of each (H x W) channel <br/> Output shape: (1 x 1 x C) <br/> Reduces parameters & prevents overfitting"]
      Flat --> Dense1["Dense Layer (Huge weights)"]
      GAP --> Dense2["Dense Layer (Minimal weights)"]
    </div>""",
    62: """    <div class="mermaid">
      graph LR
      X["Input X"] --> Conv1["Weight Layer (Conv)"] --> ReLU["ReLU"] --> Conv2["Weight Layer (Conv)"]
      X --> Shortcut["Shortcut / Identity Connection (Passes X directly)"]
      Conv2 --> Add["(+) Addition Node (F(X) + X)"]
      Shortcut --> Add
      Add --> OutReLU["ReLU (Output)"]
    </div>""",
    63: """    <div class="mermaid">
      graph TD
      Img["Input Image"] --> Grid["Divide into S x S Grid"]
      Grid --> Detect["Each Grid Cell predicts B bounding boxes <br/> and C class conditional probabilities"]
      Detect --> NMS["Non-Maximum Suppression (NMS) <br/> Filters low-confidence & overlapping boxes using IoU"]
      NMS --> Output["Final Detections"]
    </div>""",
    64: """    <div class="mermaid">
      graph LR
      subgraph Encoder [Contracting Path]
      E1["Input Image -> Conv Block"] --> E2["Max Pool -> Conv Block"] --> E3["Max Pool -> Bottleneck"]
      end
      subgraph Decoder [Expanding Path]
      D1["Bottleneck"] --> D2["Up-Conv + Skip -> Conv Block"] --> D3["Up-Conv + Skip -> Output Segmentation Map"]
      end
      E1 -->|"Skip Connection (High-res spatial features)"| D3
      E2 -->|"Skip Connection"| D2
    </div>"""
}

for day_num in [60, 61, 62, 63, 64]:
    day_id = f"day-{day_num}"
    print(f"Replacing diagram in Day {day_num}...")
    start_tag = f'<div class="day-section" id="{day_id}">'
    next_day_tag = f'<div class="day-section" id="day-{day_num+1}">'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(next_day_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        
        # Find <div class="mermaid"> in the block
        m_start = block.find('<div class="mermaid">')
        if m_start != -1:
            m_end = block.find('</div>', m_start)
            if m_end != -1:
                old_m_block = block[m_start:m_end+6]
                new_block = block.replace(old_m_block, new_diagrams[day_num], 1)
                content = content.replace(block, new_block)
                print(f"  Successfully replaced diagram in Day {day_num}!")
            else:
                print(f"  Could not find closing </div> for mermaid in Day {day_num}!")
        else:
            print(f"  Could not find mermaid block in Day {day_num} block!")
    else:
        print(f"  Day {day_num} block indices not found!")

with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week9.html")
