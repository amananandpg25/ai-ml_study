import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

REPLACEMENTS = {
    # 1. Corey Schafer Python
    "https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbG_echLdxWYjHZst": """<a class="res-card type-yt-card" href="https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWgDp1WyUNp6t5yIC69" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Apna College</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Python Full Course in Hinglish</span>
        <div class="res-desc">Complete, easy-to-follow Python playlist covering all programming basics, OOP, and data structures.</div>
        <div class="res-why">&#10026; Best for: Python programming fundamentals in Hinglish.</div>
      </div>
    </a>""",
    
    # 2. Keith Galli Pandas
    "https://www.youtube.com/watch?v=GB9ByFAIAH4": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=bDhvCp3_1jY" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Krish Naik</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Pandas Full Tutorial for Data Science</span>
        <div class="res-desc">Excellent, step-by-step Pandas tutorial covering DataFrame manipulations, filtering, aggregations, and cleaning.</div>
        <div class="res-why">&#10026; Best for: Tabular data loading and preprocessing.</div>
      </div>
    </a>""",
    
    # 3. SQL Beginner to Advanced Playlist
    "https://www.youtube.com/playlist?list=PLUaB-1hjhk8HTMlz-KcqgYD5RqKVY0m-A": """<a class="res-card type-yt-card" href="https://www.youtube.com/playlist?list=PLxCzCOWd7aiGGTA0JUXoMjDxOfqhjaMjB" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Gate Smashers</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--orange); color:var(--orange); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Intermediate</span>
          </div>
        <span class="res-title">SQL Full Playlist for Beginners</span>
        <div class="res-desc">Comprehensive database querying tutorial covering queries, grouping, sorting, joins, and aggregates.</div>
        <div class="res-why">&#10026; Best for: Database querying and SQL logic.</div>
      </div>
    </a>""",
    
    # 4. Git and GitHub Crash Course
    "https://www.youtube.com/watch?v=RGOj5yH7evk": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=Ez8F0nW6S-w" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Apna College</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Git & GitHub One Shot Tutorial</span>
        <div class="res-desc">Quick, high-yield crash course on Git commands, branch management, pull requests, and GitHub integrations.</div>
        <div class="res-why">&#10026; Best for: Git versioning fundamentals.</div>
      </div>
    </a>""",
    
    # 5. Matplotlib Series
    "https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=3Xc3CA655Y4" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; CodeWithHarry</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Matplotlib and Seaborn Complete Tutorial</span>
        <div class="res-desc">Clear, hands-on visual mapping tutorial explaining plots, lines, labels, and customized styling.</div>
        <div class="res-why">&#10026; Best for: Plotting basics and visualizations.</div>
      </div>
    </a>""",
    
    # 6. Seaborn Tutorial
    "https://www.youtube.com/watch?v=6GUZXDef2U0": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=GjcckG59p0k" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Krish Naik</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Seaborn Library for Statistical Plotting</span>
        <div class="res-desc">Hinglish video detailing Seaborn's statistical charts: scatterplots, heatmaps, boxplots, and pairplots.</div>
        <div class="res-why">&#10026; Best for: High-level statistical plots.</div>
      </div>
    </a>""",
    
    # 7. Complete EDA
    "https://www.youtube.com/watch?v=ysF3K0JVWtk": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=cst8A1054QY" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Krish Naik</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--orange); color:var(--orange); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Intermediate</span>
          </div>
        <span class="res-title">Complete EDA & Feature Engineering Walkthrough</span>
        <div class="res-desc">Walkthrough of parsing raw tabular files, imputing values, analyzing correlations, and extracting features.</div>
        <div class="res-why">&#10026; Best for: Hands-on Exploratory Data Analysis.</div>
      </div>
    </a>""",
    
    # 8. sentdex NLTK
    "https://www.youtube.com/watch?v=xvqsFTUsOmc": """<a class="res-card type-yt-card" href="https://www.youtube.com/playlist?list=PLZoTAELRMXVNNrHS9ipO5D_Vkg14t-W2t" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; Krish Naik</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--orange); color:var(--orange); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Intermediate</span>
          </div>
        <span class="res-title">NLP Full Playlist — Tokenization to BERT</span>
        <div class="res-desc">Detailed natural language processing playlist explaining spaCy, NLTK, word representations, and sequence modeling.</div>
        <div class="res-why">&#10026; Best for: Classical and deep NLP structures.</div>
      </div>
    </a>""",
    
    # 9. freeCodeCamp Flask
    "https://www.youtube.com/watch?v=Z1RJmh_OqeA": """<a class="res-card type-yt-card" href="https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xI4h0Z5n65Y" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; CodeWithHarry</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--green); color:var(--green); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Beginner</span>
          </div>
        <span class="res-title">Python Flask Full Course in Hinglish</span>
        <div class="res-desc">Easy-to-understand tutorial on constructing web applications and REST API routing logic in Python.</div>
        <div class="res-why">&#10026; Best for: Web application backends and API endpoints.</div>
      </div>
    </a>""",
    
    # 10. TechWorld with Nana Docker
    "https://www.youtube.com/watch?v=pTFZFxd5hgI": """<a class="res-card type-yt-card" href="https://www.youtube.com/watch?v=Qr4Q1dDekpM" target="_blank">
      <div class="res-icon type-yt">&#9654;</div>
      <div class="res-body">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="color:var(--yt)">YouTube &middot; CodeWithHarry</div>
            <span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid var(--orange); color:var(--orange); padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">Intermediate</span>
          </div>
        <span class="res-title">Docker and Docker Compose Full Tutorial</span>
        <div class="res-desc">Detailed guide on writing Dockerfiles, building container images, exposing ports, and running Compose networks.</div>
        <div class="res-why">&#10026; Best for: Containerized app deployments.</div>
      </div>
    </a>"""
}

def replace_card_by_url(content, target_url, new_card_html):
    pos = 0
    modifications = 0
    while True:
        idx = content.find(target_url, pos)
        if idx == -1:
            break
        # Find start tag
        start = content.rfind('<a', 0, idx)
        # Find end tag
        end = content.find('</a>', idx) + 4
        if start != -1 and end != -1:
            content = content[:start] + new_card_html + content[end:]
            pos = start + len(new_card_html)
            modifications += 1
        else:
            pos = idx + len(target_url)
    return content, modifications

def process_replacements():
    for w in range(1, 18):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        content = open(path, 'r', encoding='utf-8').read()
        total_mods = 0
        
        for url, new_html in REPLACEMENTS.items():
            content, mods = replace_card_by_url(content, url, new_html)
            total_mods += mods
            
        if total_mods > 0:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Replaced {total_mods} YouTube resource cards in {os.path.basename(path)}")

if __name__ == '__main__':
    process_replacements()
    print("\nYouTube video resources replacement complete!")
