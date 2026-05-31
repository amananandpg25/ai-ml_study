with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Day 61 BatchNorm link replacement
print("Updating Day 61 BatchNorm link...")
old_bn_card = """  <a class="resource-card" href="https://colah.github.io/posts/2014-03-RNNs-and-BatchNorm/" target="_blank">
    <div class="rc-type">📝 ARTICLE</div>
    <div class="rc-title">BatchNorm Explained — Chris Olah</div>
    <div class="rc-sub">Visual walkthrough of normalization in CNNs</div>
  </a>"""

new_bn_card = """  <a class="resource-card" href="https://arxiv.org/abs/1502.03167" target="_blank">
    <div class="rc-type">📖 OFFICIAL</div>
    <div class="rc-title">Original BatchNorm Paper (arXiv)</div>
    <div class="rc-sub">The 2015 Ioffe & Szegedy paper introducing Batch Normalization</div>
  </a>"""

content = content.replace(old_bn_card, new_bn_card)

# 2. Replacing the Mermaid diagrams
# We can find the occurrences of the CNN diagram.
# We know the generic CNN diagram has:
# <div class="mermaid">\n      graph LR\n      Img[Input Image] --> Conv["Convolution + Activation"]\n      Conv --> Pool["Max Pooling / Downsampling"]\n      Pool --> FC[Fully Connected Layers]\n      FC --> Out[Output Class]\n    </div>
# Since there are 6 of these, and we want to replace blocks 1, 2, 3, 4, 5. Let's do this day-by-day by bounding the search within each day's ID.

import re

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

# The target generic diagram to replace:
old_mermaid = """    <div class="mermaid">
      graph LR
      Img[Input Image] --> Conv["Convolution + Activation"]
      Conv --> Pool["Max Pooling / Downsampling"]
      Pool --> FC[Fully Connected Layers]
      FC --> Out[Output Class]
    </div>"""

for day_num in [60, 61, 62, 63, 64]:
    day_id = f"day-{day_num}"
    print(f"Replacing diagram in Day {day_num}...")
    start_tag = f'<div class="day-section" id="{day_id}">'
    next_day_tag = f'<div class="day-section" id="day-{day_num+1}">'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(next_day_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        if old_mermaid in block:
            new_block = block.replace(old_mermaid, new_diagrams[day_num], 1)
            content = content.replace(block, new_block)
            print(f"  Successfully replaced diagram in Day {day_num}!")
        else:
            # try normalising whitespace
            print(f"  Warning: exact old_mermaid match not found in Day {day_num} block!")
    else:
        print(f"  Day {day_num} block start/end index not found!")

# 3. Day 63, 64, 65 resources replacement
print("Updating Day 63, 64, 65 resources...")

# Day 63: we want to append fast.ai to the resource cards
day63_res_start = content.find('Day 63 Resources — Transfer Learning')
if day63_res_start != -1:
    # Let's find the closing </div> of the resources-grid
    grid_end = content.find('</div>\n</div>', day63_res_start)
    if grid_end != -1:
        fast_ai_card = """  <a class="resource-card" href="https://course.fast.ai/" target="_blank">
    <div class="rc-type">🌐 COURSE</div>
    <div class="rc-title">Practical Deep Learning for Coders — fast.ai</div>
    <div class="rc-sub">The premier practical course for deep learning. Highly recommended for transfer learning.</div>
  </a>\n"""
        # Insert before the closing </div>
        content = content[:grid_end] + fast_ai_card + content[grid_end:]
        print("  Added fast.ai to Day 63 resources!")

# Day 64: replace duplicate resources
day64_res_start = content.find('Day 64 Resources — Data Augmentation')
if day64_res_start != -1:
    grid_start = content.find('<div class="resources-grid">', day64_res_start)
    grid_end = content.find('</div>\n</div>', grid_start)
    if grid_start != -1 and grid_end != -1:
        old_grid = content[grid_start:grid_end+6]
        new_grid_day64 = """<div class="resources-grid">
    <a class="resource-card" href="https://course.fast.ai/Lessons/lesson2.html" target="_blank">
      <div class="rc-type">🌐 COURSE</div>
      <div class="rc-title">fast.ai Lesson 2: Production & Deployment</div>
      <div class="rc-sub">Covers practical image augmentation, data cleaning, and deployment.</div>
    </a>
    <a class="resource-card" href="https://albumentations.ai/docs/" target="_blank">
      <div class="rc-type">📖 OFFICIAL</div>
      <div class="rc-title">Albumentations Documentation</div>
      <div class="rc-sub">The industry gold-standard library for fast and flexible image augmentation.</div>
    </a>
    <a class="resource-card" href="https://www.tensorflow.org/tutorials/images/data_augmentation" target="_blank">
      <div class="rc-type">💻 PRACTICE</div>
      <div class="rc-title">TF/Keras Data Augmentation Guide</div>
      <div class="rc-sub">Official guide to using Keras preprocessing layers for augmentation.</div>
    </a>
  </div>"""
        content = content.replace(old_grid, new_grid_day64)
        print("  Successfully replaced Day 64 resources!")

# Day 65: replace duplicate resources
day65_res_start = content.find('Day 65 Resources — Vision Capstone')
if day65_res_start != -1:
    grid_start = content.find('<div class="resources-grid">', day65_res_start)
    grid_end = content.find('</div>\n</div>', grid_start)
    if grid_start != -1 and grid_end != -1:
        old_grid = content[grid_start:grid_end+6]
        new_grid_day65 = """<div class="resources-grid">
    <a class="resource-card" href="https://course.fast.ai/Lessons/lesson1.html" target="_blank">
      <div class="rc-type">🌐 COURSE</div>
      <div class="rc-title">fast.ai Lesson 1: Getting Started with Vision</div>
      <div class="rc-sub">Hands-on guide to training your first high-accuracy image classifier.</div>
    </a>
    <a class="resource-card" href="https://www.kaggle.com/code" target="_blank">
      <div class="rc-type">💻 PRACTICE</div>
      <div class="rc-title">Kaggle Image Classification Notebooks</div>
      <div class="rc-sub">Explore top community solutions and pipeline architectures.</div>
    </a>
    <a class="resource-card" href="https://docs.wandb.ai/guides/integrations/keras" target="_blank">
      <div class="rc-type">📖 GUIDES</div>
      <div class="rc-title">Weights & Biases Keras Integration</div>
      <div class="rc-sub">Track experiments, loss curves, and validation metrics in real-time.</div>
    </a>
  </div>"""
        content = content.replace(old_grid, new_grid_day65)
        print("  Successfully replaced Day 65 resources!")

with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week9.html")
