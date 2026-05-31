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

# 2. New resources sections
new_resources = {
    87: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://spacy.io/usage/spacy-101" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Docs &middot; spaCy</div>
          <span class="res-title">spaCy 101: Everything you need to know</span>
          <div class="res-desc">Excellent primer explaining tokenization, POS tagging, dependency parsing, and pipeline architectures in spaCy.</div>
          <div class="res-why">&#10026; Best for: understanding spaCy fundamentals.</div>
        </div>
      </a>
    </div>
  </div>""",
    88: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Docs &middot; Scikit-Learn</div>
          <span class="res-title">TfidfVectorizer Documentation</span>
          <div class="res-desc">Official documentation for the TF-IDF representation layer in Scikit-Learn, including analyzer and ngram configurations.</div>
          <div class="res-why">&#10026; Reference</div>
        </div>
      </a>
    </div>
  </div>""",
    89: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://jalammar.github.io/illustrated-word2vec/" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Visual &middot; Jay Alammar</div>
          <span class="res-title">The Illustrated Word2Vec</span>
          <div class="res-desc">The ultimate illustrated conceptual guide explaining CBOW, Skip-Gram, negative sampling, and word vector dimensions.</div>
          <div class="res-why">&#10026; Recommended</div>
        </div>
      </a>
    </div>
  </div>""",
    90: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://course.spacy.io/en/" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Interactive &middot; spaCy</div>
          <span class="res-title">spaCy 101 Interactive Course</span>
          <div class="res-desc">The official interactive course covering advanced NLP pipelines, rule-based matching, and entity recognition.</div>
          <div class="res-why">&#10026; Best for: hands-on spaCy mastery.</div>
        </div>
      </a>
    </div>
  </div>""",
    91: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://huggingface.co/learn/nlp-course/chapter1/1" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Course &middot; HuggingFace</div>
          <span class="res-title">Hugging Face NLP Course: Chapter 1</span>
          <div class="res-desc">Introduction to NLP, transformers pipeline abstractions, and basic classification benchmarks.</div>
          <div class="res-why">&#10026; Best for: modern NLP concepts.</div>
        </div>
      </a>
    </div>
  </div>""",
    92: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://keras.io/examples/nlp/text_classification_from_scratch/" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Practice &middot; Keras</div>
          <span class="res-title">Keras Text Classification from Scratch</span>
          <div class="res-desc">Complete code implementation for training recurrent models for classification on the IMDB sentiment dataset.</div>
          <div class="res-why">&#10026; Best for: recurrent model practice.</div>
        </div>
      </a>
    </div>
  </div>""",
    93: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="res-card type-web-card" href="https://spacy.io/usage/processing-pipelines" target="_blank">
        <div class="res-icon type-web">&#128214;</div>
        <div class="res-body">
          <div class="res-type" style="color:var(--web)">Docs &middot; spaCy</div>
          <span class="res-title">Language Processing Pipelines</span>
          <div class="res-desc">Official guide to customizing pipelines, writing custom components, and optimizing batch operations.</div>
          <div class="res-why">&#10026; Reference</div>
        </div>
      </a>
    </div>
  </div>"""
}

# Apply diagram replacements first
for day_num in [88, 90, 91, 92, 93]:
    day_id = f"day-{day_num}"
    start_tag = f'id="{day_id}"'
    start_idx = content.find(start_tag)
    
    if day_num < 93:
        next_day_tag = f'id="day-{day_num+1}"'
        end_idx = content.find(next_day_tag)
    else:
        end_idx = content.find('</main>')
        if end_idx == -1:
            end_idx = content.find('<script>')
            
    if start_idx != -1 and end_idx != -1:
        day_block = content[start_idx:end_idx]
        m_start = day_block.find('<div class="mermaid">')
        if m_start != -1:
            m_end = day_block.find('</div>', m_start)
            if m_end != -1:
                old_m = day_block[m_start:m_end+6]
                new_day_block = day_block.replace(old_m, new_diagrams[day_num], 1)
                content = content.replace(day_block, new_day_block)
                print(f"Diagram replaced in Day {day_num}!")

# Now, inject resources section before the closing </div><!-- /day-N --> for each day
for day_num in range(87, 94):
    closing_tag = f"</div><!-- /day-{day_num} -->"
    closing_idx = content.find(closing_tag)
    if closing_idx != -1:
        # We insert the new resources block right before the closing tag, with nice spacing
        new_block = "\\n\\n" + new_resources[day_num] + "\\n\\n"
        content = content[:closing_idx] + new_block + content[closing_idx:]
        print(f"Resources injected for Day {day_num}!")
    else:
        print(f"Warning: closing tag {closing_tag} not found!")

with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved week13.html")
