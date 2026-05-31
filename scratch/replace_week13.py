with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. New diagrams definitions
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

# Replace diagrams day by day
for day_num in [88, 90, 91, 92, 93]:
    day_id = f"day-{day_num}"
    print(f"Replacing diagram in Day {day_num}...")
    start_tag = f'<div class="day-section" id="{day_id}">' if day_num > 87 else f'<div class="day-section active" id="{day_id}">'
    next_day_tag = f'<div class="day-section" id="day-{day_num+1}">' if day_num < 93 else '<!-- ── FOOTER ── -->'
    
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

# 2. Replacing the resources
# Let's define the new resources grid for each day
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

# In week13.html, the resources section is outside the day-section block (immediately follows it).
# Let's find each Day's resources block and replace it.
# We can search for the day title, e.g., "Day 87 Resources", find the resources-grid following it, and replace it.
for day_num in [87, 88, 89, 90, 91, 92, 93]:
    day_title = f"Day {day_num} Resources"
    idx = content.find(day_title)
    if idx != -1:
        grid_start = content.find('<div class="resources-grid">', idx)
        if grid_start != -1:
            grid_end = content.find('</div>', grid_start)
            if grid_end != -1:
                # We need to include the nested anchor tags
                # A robust way is to find the next day section start or toolkit/footer and extract the exact resources-grid block
                # Let's find the closing </div> of the resources-grid. In the file, it has some indentation.
                # Let's find the closing </div> of resources-grid. It's followed by </div>\n</div> or similar.
                # Let's find the next <div class="day-section" or <!-- or </main>
                next_marker = content.find('<div class="day-section"', grid_start)
                if next_marker == -1:
                    next_marker = content.find('<div class="day-section active"', grid_start)
                if next_marker == -1:
                    next_marker = content.find('</main>', grid_start)
                
                # Within this range, find the resources-grid block and replace it
                sub_content = content[grid_start:next_marker]
                # Find the closing </div> for resources-grid. It's the one before the closing </div> of resources-section
                # Actually, let's just find the last </div> in the sub_content that matches resources-grid end
                # In this file, all resources-grid blocks have two resource cards except Day 93 which might have one.
                # Let's search for the closing </div> of resources-grid
                # Since we know they all look like: <div class="resources-grid"> ... </a>\n  </div>
                grid_match = re.search(r'<div class="resources-grid">.*?</a>\s*</div>', sub_content, re.DOTALL)
                if grid_match:
                    old_grid = grid_match.group(0)
                    content = content.replace(old_grid, new_resources[day_num], 1)
                    print(f"  Successfully replaced Day {day_num} resources!")
                else:
                    print(f"  Could not match resources-grid format in Day {day_num}!")
        else:
            print(f"  Could not find grid end for Day {day_num}!")
    else:
        print(f"  Day {day_num} title not found for resources!")

with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week13.html")
