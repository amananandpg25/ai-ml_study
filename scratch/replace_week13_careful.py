with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_diagrams = {
    88: """    <div class="mermaid">
      graph TD
      Docs["Documents List"] --> TF["Term Frequency (TF) <br/> How often word appears in document"]
      Docs --> IDF["Inverse Document Frequency (IDF) <br/> How rare word is across all documents"]
      TF --> Vector["TF-IDF Vector: TF * IDF <br/> High weight for important, discriminative words"]
      IDF --> Vector
    </div>""",
    90: """    <div class="mermaid">
      graph LR
      Input["Sentence: Apple bought Beats in 2014"] --> POS["POS Tagger: <br/> Apple (PROPN), bought (VERB), Beats (PROPN), in (ADP), 2014 (NUM)"]
      Input --> NER["NER Tagger: <br/> Apple (ORG), Beats (ORG), 2014 (DATE)"]
    </div>""",
    91: """    <div class="mermaid">
      graph LR
      Text["Input Text Article"] --> Preproc["Tokenizer & Embedding Layer"] --> Classifier["Machine Learning Classifier (Naïve Bayes / SVM)"] --> Output["Label: Real or Fake News"]
    </div>""",
    92: """    <div class="mermaid">
      graph LR
      Tokens["Tokens: x_1, x_2, ..., x_t"] --> LSTM["LSTM Hidden Layer (States h_t)"] --> Dense["Dense Layer"] --> Output["Label (e.g. Sentiment probability)"]
    </div>""",
    93: """    <div class="mermaid">
      graph TD
      Raw["Raw Customer Reviews"] --> Pipeline["Modular spacy NLP Preprocessing Pipeline"] --> Vectorizer["TF-IDF / Word2Vec Embeddings"] --> Model["Trained Classifier Model"] --> Eval["Validation Metrics: Accuracy, Precision, Recall, F1"]
    </div>"""
}

new_resources = {
    87: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://spacy.io/usage/spacy-101" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Docs &middot; spaCy</div>
        <span class="res-title">spaCy 101: Everything you need to know</span>
        <div class="res-desc">Excellent primer explaining tokenization, POS tagging, dependency parsing, and pipeline architectures in spaCy.</div>
        <div class="res-why">&#10026; Best for: understanding spaCy fundamentals.</div>
      </div>
    </a>
  </div>""",
    88: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Docs &middot; Scikit-Learn</div>
        <span class="res-title">TfidfVectorizer Documentation</span>
        <div class="res-desc">Official documentation for the TF-IDF representation layer in Scikit-Learn, including analyzer and ngram configurations.</div>
        <div class="res-why">&#10026; Reference</div>
      </div>
    </a>
  </div>""",
    89: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://jalammar.github.io/illustrated-word2vec/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Visual &middot; Jay Alammar</div>
        <span class="res-title">The Illustrated Word2Vec</span>
        <div class="res-desc">The ultimate illustrated conceptual guide explaining CBOW, Skip-Gram, negative sampling, and word vector dimensions.</div>
        <div class="res-why">&#10026; Recommended</div>
      </div>
    </a>
  </div>""",
    90: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://course.spacy.io/en/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Interactive &middot; spaCy</div>
        <span class="res-title">spaCy 101 Interactive Course</span>
        <div class="res-desc">The official interactive course covering advanced NLP pipelines, rule-based matching, and entity recognition.</div>
        <div class="res-why">&#10026; Best for: hands-on spaCy mastery.</div>
      </div>
    </a>
  </div>""",
    91: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://huggingface.co/learn/nlp-course/chapter1/1" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Course &middot; HuggingFace</div>
        <span class="res-title">Hugging Face NLP Course: Chapter 1</span>
        <div class="res-desc">Introduction to NLP, transformers pipeline abstractions, and basic classification benchmarks.</div>
        <div class="res-why">&#10026; Best for: modern NLP concepts.</div>
      </div>
    </a>
  </div>""",
    92: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://keras.io/examples/nlp/text_classification_from_scratch/" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Practice &middot; Keras</div>
        <span class="res-title">Keras Text Classification from Scratch</span>
        <div class="res-desc">Complete code implementation for training recurrent models for classification on the IMDB sentiment dataset.</div>
        <div class="res-why">&#10026; Best for: recurrent model practice.</div>
      </div>
    </a>
  </div>""",
    93: """<div class="resources-grid">
    <a class="res-card type-web-card" href="https://spacy.io/usage/processing-pipelines" target="_blank">
      <div class="res-icon type-web">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Docs &middot; spaCy</div>
        <span class="res-title">Language Processing Pipelines</span>
        <div class="res-desc">Official guide to customizing pipelines, writing custom components, and optimizing batch operations.</div>
        <div class="res-why">&#10026; Reference</div>
      </div>
    </a>
  </div>"""
}

# Iterate through Day 87 to Day 93
for day_num in range(87, 94):
    day_id = f"day-{day_num}"
    start_tag = f'id="{day_id}"'
    
    start_idx = content.find(start_tag)
    if start_idx == -1:
        print(f"Start tag not found for {day_id}!")
        continue
        
    if day_num < 93:
        next_day_tag = f'id="day-{day_num+1}"'
        end_idx = content.find(next_day_tag)
    else:
        end_idx = content.find('</main>')
        if end_idx == -1:
            end_idx = content.find('<script>')
            
    if end_idx == -1:
        print(f"End index not found for {day_id}!")
        continue
        
    day_block = content[start_idx:end_idx]
    new_day_block = day_block
    
    # 1. Replace diagram
    if day_num in new_diagrams:
        m_start = day_block.find('<div class="mermaid">')
        if m_start != -1:
            m_end = day_block.find('</div>', m_start)
            if m_end != -1:
                old_m = day_block[m_start:m_end+6]
                new_day_block = new_day_block.replace(old_m, new_diagrams[day_num], 1)
                print(f"  Diagram replaced for Day {day_num}")
                
    # 2. Replace resources-grid carefully
    import re
    # Match <div class="resources-grid"> ... </div> (and check that it contains illustrated-transformer)
    # We want to match only the grid itself. The grid has class="resources-grid".
    # Let's search for '<div class="resources-grid">' inside day_block.
    grid_idx = day_block.find('class="resources-grid"')
    if grid_idx != -1:
        # Find the opening <div ...> that contains it
        div_start = day_block.rfind('<div', 0, grid_idx)
        # Find the matching closing </div> of this grid
        # Since it contains 2 resource cards, let's find the closing </div> that terminates the grid.
        # Let's trace open/close divs inside day_block from div_start
        depth = 0
        div_pattern = re.compile(r'</?div\b[^>]*>')
        pos = div_start
        grid_end_idx = -1
        for match in div_pattern.finditer(day_block, div_start):
            tag = match.group(0)
            if tag.startswith('</'):
                depth -= 1
            else:
                depth += 1
            if depth == 0:
                grid_end_idx = match.end()
                break
                
        if grid_end_idx != -1:
            old_grid = day_block[div_start:grid_end_idx]
            new_day_block = new_day_block.replace(old_grid, new_resources[day_num], 1)
            print(f"  Resources replaced for Day {day_num}")
        else:
            print(f"  Could not find matching closing div for resources-grid in Day {day_num}")
    else:
        print(f"  resources-grid not found in Day {day_num} block")
        
    if new_day_block != day_block:
        content = content.replace(day_block, new_day_block)

with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week13.html")
