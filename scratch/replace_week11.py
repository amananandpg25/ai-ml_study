with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's define the new diagrams
new_diagrams = {
    73: """    <div class="mermaid">
      graph LR
      Noise[Noise Vector z] --> Gen[Generator G] --> Fake[Fake Images G_z]
      Real[Real Images x] --> Disc[Discriminator D]
      Fake --> Disc
      Disc --> Loss[Loss & Gradients]
      Loss -. Update weights .-> Gen
      Loss -. Update weights .-> Disc
    </div>""",
    74: """    <div class="mermaid">
      graph LR
      Noise["Noise Vector (1x1x100)"] --> Project["Project & Reshape (4x4x1024)"]
      Project --> Up1["Transposed Conv 1 (8x8x512)"]
      Up1 --> Up2["Transposed Conv 2 (16x16x256)"]
      Up2 --> Up3["Transposed Conv 3 (32x32x128)"]
      Up3 --> Up4["Transposed Conv 4 (64x64x3)"]
    </div>""",
    75: """    <div class="mermaid">
      graph TD
      Real[Real Data] --> Critic[Critic D]
      Fake[Fake Data] --> Critic
      Interp[Interpolated Data] --> Critic
      Critic --> L_wgan[WGAN Loss: E[D(x)] - E[D(G(z))]]
      Critic --> GP[Gradient Penalty: (|grad D(x_interp)| - 1)^2]
      GP --> Loss[Total Critic Loss]
      L_wgan --> Loss
    </div>""",
    76: """    <div class="mermaid">
      graph LR
      X[Domain X] --> G[Generator G] --> Y_hat[Translated Domain Y] --> F[Generator F] --> X_cycle[Recycled Domain X]
      Y_hat --> DiscY[Discriminator Dy]
      X_cycle -. Cycle Consistency Loss .-> Loss
      Y_hat -. Adversarial Loss .-> Loss
    </div>""",
    77: """    <div class="mermaid">
      graph TD
      TrainD["Step 1: Train Discriminator <br/> Real Images -> D (Target: 1) <br/> Noise -> G -> Fake Images -> D (Target: 0) <br/> Calculate Loss & Update D"]
      TrainD --> TrainG["Step 2: Train Generator <br/> Noise -> G -> Fake Images -> D (Target: 1) <br/> Calculate Loss & Update G"]
    </div>""",
    79: """    <div class="mermaid">
      graph TD
      Real[Real Images] --> Inception[Inception-V3 Network] --> FeatReal[Feature Vector Distribution: m_r, C_r]
      Fake[Fake Images] --> Inception --> FeatFake[Feature Vector Distribution: m_f, C_f]
      FeatReal --> FID["FID = |m_r - m_f|^2 + Tr(C_r + C_f - 2*sqrt(C_r * C_f))"]
      FeatFake --> FID
    </div>"""
}

# Replace the diagrams
for day_num in [73, 74, 75, 76, 77, 79]:
    day_id = f"day-{day_num}"
    print(f"Replacing diagram in Day {day_num}...")
    start_tag = f'<div class="day-section" id="{day_id}">' if day_num > 73 else f'<div class="day-section active" id="{day_id}">'
    next_day_tag = f'<div class="day-section" id="day-{day_num+1}">' if day_num < 79 else '<!-- ── FOOTER ── -->'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(next_day_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        
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

# Replace LangChain and Pinecone links in Day 77 resources
print("Replacing LangChain and Pinecone links in Day 77...")
old_langchain_card = """        <a class="res-card type-web-card" href="https://python.langchain.com/v0.2/docs/introduction/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Docs &middot; LangChain</div>
        <span class="res-title">LangChain Documentation</span>
        <div class="res-desc">Official documentation for LangChain and LCEL: chain expression language, prompt templates, vector store integration, and agents.</div>
        <div class="res-why">&#10026; Best for: building LLM applications.</div>
      </div>
    </a>"""

new_ganlab_card = """        <a class="res-card type-web-card" href="https://poloclub.github.io/ganlab/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Interactive &middot; GAN Lab</div>
        <span class="res-title">GAN Lab Interactive Visualization</span>
        <div class="res-desc">An interactive tool that runs directly in your browser to visualize and explain how GAN training dynamically converges.</div>
        <div class="res-why">&#10026; Best for: visual and intuitive understanding of GAN dynamics.</div>
      </div>
    </a>"""

old_pinecone_card = """    <a class="res-card type-web-card" href="https://www.pinecone.io/learn/vector-database/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Reference &middot; Pinecone</div>
        <span class="res-title">Vector Database & Semantic Search Guide</span>
        <div class="res-desc">Complete conceptual guide explaining what vector databases are, semantic search, cosine similarity, index algorithms, and RAG.</div>
        <div class="res-why">&#10026; Best for: understanding vector retrieval.</div>
      </div>
    </a>"""

new_wandb_card = """    <a class="res-card type-web-card" href="https://docs.wandb.ai/guides/integrations/keras" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Guides &middot; W&B</div>
        <span class="res-title">Weights & Biases Keras Integration</span>
        <div class="res-desc">Learn how to log loss curves, monitor training convergence, and track generated image grids over multiple epochs.</div>
        <div class="res-why">&#10026; Best for: practical GAN experiment tracking.</div>
      </div>
    </a>"""

# Replace these in the file content
content = content.replace(old_langchain_card, new_ganlab_card)
content = content.replace(old_pinecone_card, new_wandb_card)

# Add PyTorch DCGAN official tutorial to Day 74 resources and GAN Zoo to Day 76 resources
# Let's inspect if they have resources-grid or cards in Day 74 and Day 76.
# Actually, let's look at Day 74 resources-grid using a script or find.
print("Injecting new resources to Day 74 and Day 76...")
day74_res_idx = content.find('Day 74 Resources')
if day74_res_idx != -1:
    grid_end = content.find('</div>\n      </div>', day74_res_idx)
    if grid_end == -1:
        grid_end = content.find('</div>\n</div>', day74_res_idx)
    # Let's append PyTorch DCGAN card
    pytorch_dcgan_card = """  <a class="resource-card" href="https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html" target="_blank">
    <div class="rc-type">📖 OFFICIAL</div>
    <div class="rc-title">PyTorch DCGAN Faces Tutorial</div>
    <div class="rc-sub">The classic PyTorch implementation guide for training a DCGAN on face images.</div>
  </a>\n"""
    # Insert before the closing grid div
    content = content[:grid_end] + pytorch_dcgan_card + content[grid_end:]

day76_res_idx = content.find('Day 76 Resources')
if day76_res_idx != -1:
    grid_end = content.find('</div>\n      </div>', day76_res_idx)
    if grid_end == -1:
        grid_end = content.find('</div>\n</div>', day76_res_idx)
    # Let's append GAN Zoo card
    gan_zoo_card = """  <a class="resource-card" href="https://github.com/hindupuravinash/the-gan-zoo" target="_blank">
    <div class="rc-type">🐙 GITHUB</div>
    <div class="rc-title">The GAN Zoo Repository</div>
    <div class="rc-sub">A comprehensive curated list of named Generative Adversarial Networks (GANs).</div>
  </a>\n"""
    # Insert before the closing grid div
    content = content[:grid_end] + gan_zoo_card + content[grid_end:]

# Double check if any python.langchain.com/v0.2 links are left and replace them with python.langchain.com/docs/
content = content.replace("python.langchain.com/v0.2/docs/introduction/", "python.langchain.com/docs/introduction/")

with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week11.html")
