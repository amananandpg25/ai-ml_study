with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find index of id="day-79"
day79_start = content.find('id="day-79"')
if day79_start != -1:
    # Find the next mermaid block after day-79 start
    m_idx = content.find('<div class="mermaid">', day79_start)
    if m_idx != -1:
        m_end = content.find('</div>', m_idx)
        if m_end != -1:
            old_m = content[m_idx:m_end+6]
            new_m = """    <div class="mermaid">
      graph TD
      Real[Real Images] --> Inception[Inception-V3 Network] --> FeatReal[Feature Vector Distribution: m_r, C_r]
      Fake[Fake Images] --> Inception --> FeatFake[Feature Vector Distribution: m_f, C_f]
      FeatReal --> FID["FID = |m_r - m_f|^2 + Tr(C_r + C_f - 2*sqrt(C_r * C_f))"]
      FeatFake --> FID
    </div>"""
            content = content.replace(old_m, new_m, 1)
            print("Successfully replaced Day 79 diagram in week11.html!")
        else:
            print("Could not find closing </div> for mermaid in Day 79")
    else:
        print("Could not find mermaid block after Day 79 start")
else:
    print("Could not find day-79")

with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved week11.html")
