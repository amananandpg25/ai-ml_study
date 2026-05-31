import os

path = "/Users/amananand/Downloads/SDE/ai:ml/roadmap.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Replace the career salary table rows
old_rows = """      <tr><td><strong>AI Engineer</strong></td><td>LLMs, RAG, LangChain, APIs, deployment</td><td>8–20 LPA</td><td>Build 3 LLM projects, learn LangChain deeply</td></tr>
      <tr><td><strong>ML Engineer</strong></td><td>scikit-learn, XGBoost, MLOps, Docker, Feature engineering</td><td>10–25 LPA</td><td>Build end-to-end pipelines, master deployment</td></tr>
      <tr><td><strong>Data Scientist</strong></td><td>Statistics, SQL, EDA, storytelling, Pandas, ML</td><td>8–18 LPA</td><td>Build EDA portfolio, master visualization & stats</td></tr>
      <tr><td><strong>GenAI Engineer</strong></td><td>LLMs, Agents, RAG, Prompt engineering, Fine-tuning</td><td>12–30 LPA</td><td>Build agentic workflows, fine-tune open LLMs</td></tr>"""

new_rows = """      <tr><td><strong>AI Engineer</strong></td><td>LLMs, RAG, LangChain, APIs, deployment</td><td>15–35 LPA</td><td>Build 3 LLM projects, learn LLM framework concepts (Chroma, LangChain, LangGraph, direct SDK usage)</td></tr>
      <tr><td><strong>ML Engineer</strong></td><td>scikit-learn, XGBoost, MLOps, Docker, Feature engineering</td><td>12–30 LPA</td><td>Build end-to-end pipelines, master deployment</td></tr>
      <tr><td><strong>Data Scientist</strong></td><td>Statistics, SQL, EDA, storytelling, Pandas, ML</td><td>10–25 LPA</td><td>Build EDA portfolio, master visualization & stats</td></tr>
      <tr><td><strong>GenAI Engineer</strong></td><td>LLMs, Agents, RAG, Prompt engineering, Fine-tuning</td><td>18–45 LPA</td><td>Build agentic workflows, fine-tune open LLMs</td></tr>"""

html = html.replace(old_rows, new_rows)

# Add disclaimer right after the closing </table> in the career section
old_table_end = """      <tr><td><strong>GenAI Engineer</strong></td><td>LLMs, Agents, RAG, Prompt engineering, Fine-tuning</td><td>18–45 LPA</td><td>Build agentic workflows, fine-tune open LLMs</td></tr>
    </table>"""

new_table_end = """      <tr><td><strong>GenAI Engineer</strong></td><td>LLMs, Agents, RAG, Prompt engineering, Fine-tuning</td><td>18–45 LPA</td><td>Build agentic workflows, fine-tune open LLMs</td></tr>
    </table>
    <p style="font-size:11.5px; color:var(--muted); margin-top:0.5rem; font-style:italic;">
      * Note: Salary ranges are indicative for mid-level roles in India (May 2026) and vary widely by company scale, funding, and location. Check Levels.fyi (India), AmbitionBox, and Glassdoor for current data.
    </p>"""

html = html.replace(old_table_end, new_table_end)

# 2. Inject virtual environment and README template in resources section
old_resources_end = """    </table>
  </div>

  <!-- CAREER ROADMAP -->"""

new_resources_end = """    </table>

    <h3 style="margin-top: 2rem;">🔧 Pinned Environment Setup</h3>
    <p>Set up your Python virtual environment using Python 3.11+ (recommended for best scikit-learn and library compatibility). Create a file named <code>requirements.txt</code> with the following pinned packages:</p>
    <div class="cb" style="margin:.5rem 0">
      <div class="cb-head"><span class="cb-lang">requirements.txt</span></div>
      <pre>python-dotenv==1.0.1
numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
seaborn==0.13.2
scikit-learn==1.4.2
category-encoders==2.6.3
scipy==1.13.0
statsmodels==0.14.2
ipykernel==6.29.4
notebook==7.1.3
# LLM / RAG / GenAI stack (study versions carefully as API changes frequently)
langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.6
chromadb==0.5.0
faiss-cpu==1.8.0
transformers==4.40.1
torch==2.3.0
sentence-transformers==2.7.0</pre>
    </div>
    <p>Install these inside a virtual environment using:</p>
    <div class="cb" style="margin:.5rem 0">
      <div class="cb-head"><span class="cb-lang">bash</span></div>
      <pre>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</pre>
    </div>

    <h3 style="margin-top: 2rem;">📦 Portfolio Project README Template</h3>
    <p>Recruiters at top companies look for clear project framing and self-assessment. Use this template for your project\'s <code>README.md</code> file:</p>
    <div class="cb" style="margin:.5rem 0">
      <div class="cb-head"><span class="cb-lang">markdown — README.md</span></div>
      <pre># Project Title: [Name of Project]

## 1. Problem Statement
[Explain the business problem you are solving, the metric you want to optimize, and who benefits.]

## 2. Dataset
- **Source:** [Kaggle link, company data, web scraped]
- **Size:** [Number of rows, columns, memory usage]
- **Features:** [Brief explanation of target and key predictor features]

## 3. Approach & Methodology
- **Cleaning:** [Handling missing values, duplicate removal, outliers]
- **Encoding/Scaling:** [Pipelines, ColumnTransformers, scalers used]
- **Modeling:** [Models tried, validation strategy used e.g., 5-fold CV]

## 4. Key Results & Performance
- **Baseline Model Score:** [e.g. Logistic Regression: F1=0.74]
- **Final Model Score:** [e.g. XGBoost: F1=0.86]
- **Core Findings:** [e.g., Feature X has the strongest correlation to churn]

## 5. How to Run
```bash
# Clone the repository
git clone [repository-url]
# Install dependencies
pip install -r requirements.txt
# Run the analysis/notebook
jupyter notebook
```

## 6. What I\'d Improve (Critical Self-Assessment)
- **Alternative Approaches:** [e.g., I would try target encoding instead of One-Hot to reduce dimensions]
- **Limitations:** [e.g., The dataset is highly imbalanced; gathering more positive samples would improve precision]
- **Scale considerations:** [e.g., If the data grows to 10M+ rows, I would use Dask or Polars instead of Pandas]</pre>
    </div>
  </div>

  <!-- CAREER ROADMAP -->"""

html = html.replace(old_resources_end, new_resources_end)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched roadmap.html!")
