import re
import os

files = [f"week{i}.html" for i in range(1, 18)]
base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for f in files:
    path = os.path.join(base_dir, f)
    if not os.path.exists(path):
        print(f"{f}: Missing file")
        continue
    
    content = open(path, 'r', encoding='utf-8').read()
    
    # Check for features
    has_favicon = "rel=\"icon\"" in content
    has_theme_btn = "class=\"theme-btn\"" in content or "toggleTheme()" in content
    has_level_badge = "class=\"level-badge\"" in content or "getLevel(" in content
    has_week_nav = "class=\"week-nav-links\"" in content
    has_focus_visible = ":focus-visible" in content
    has_print_style = "@media print" in content
    has_quiz_icons = "✓" in content and "correct" in content and ("quiz" in content or "checkAnswer" in content)
    has_render_mermaid = "renderMermaid" in content
    
    features = []
    if has_favicon: features.append("favicon")
    if has_theme_btn: features.append("theme")
    if has_level_badge: features.append("level")
    if has_week_nav: features.append("week-nav")
    if has_focus_visible: features.append("focus-visible")
    if has_print_style: features.append("print")
    if has_quiz_icons: features.append("quiz-icons")
    if has_render_mermaid: features.append("render-mermaid")
    
    print(f"{f}: {len(features)}/8 features ({', '.join(features)})")
