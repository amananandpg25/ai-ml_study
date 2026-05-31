from pathlib import Path


path = Path('/Users/amananand/Downloads/SDE/ai:ml/week11.html')
text = path.read_text(encoding='utf-8')

replacements = [
    ('<div aria-selected="true" class="day-pill active" data-xp="200" id="pill-73" onclick="goDay(73)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(73)" role="tab" tabindex="0">73</div>',
     '<div aria-selected="true" class="day-pill active" data-xp="200" id="pill-73" onclick="goDay(73)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(73)" role="tab" tabindex="0">73</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="200" id="pill-74" onclick="goDay(74)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(74)" role="tab" tabindex="0">74</div>',
     '<div aria-selected="false" class="day-pill" data-xp="200" id="pill-74" onclick="goDay(74)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(74)" role="tab" tabindex="0">74</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="200" id="pill-75" onclick="goDay(75)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(75)" role="tab" tabindex="0">75</div>',
     '<div aria-selected="false" class="day-pill" data-xp="200" id="pill-75" onclick="goDay(75)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(75)" role="tab" tabindex="0">75</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="200" id="pill-76" onclick="goDay(76)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(76)" role="tab" tabindex="0">76</div>',
     '<div aria-selected="false" class="day-pill" data-xp="200" id="pill-76" onclick="goDay(76)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(76)" role="tab" tabindex="0">76</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="200" id="pill-77" onclick="goDay(77)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(77)" role="tab" tabindex="0">77</div>',
     '<div aria-selected="false" class="day-pill" data-xp="200" id="pill-77" onclick="goDay(77)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(77)" role="tab" tabindex="0">77</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="200" id="pill-78" onclick="goDay(78)" data-xp="200" data-xp="200" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(78)" role="tab" tabindex="0">78</div>',
     '<div aria-selected="false" class="day-pill" data-xp="200" id="pill-78" onclick="goDay(78)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(78)" role="tab" tabindex="0">78</div>'),
    ('<div aria-selected="false" class="day-pill" data-xp="500" id="pill-79" onclick="goDay(79)" data-xp="500" data-xp="500" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(79)" role="tab" tabindex="0">79</div>',
     '<div aria-selected="false" class="day-pill" data-xp="500" id="pill-79" onclick="goDay(79)" onkeydown="if(event.key===\'Enter\'||event.key===\' \')goDay(79)" role="tab" tabindex="0">79</div>'),
    ('<div class="day-section active" data-xp="200" id="day-73" data-xp="200" data-xp="200">',
     '<div class="day-section active" data-xp="200" id="day-73">'),
    ('<div class="day-section" data-xp="200" id="day-74" data-xp="200" data-xp="200">',
     '<div class="day-section" data-xp="200" id="day-74">'),
    ('<div class="day-section" data-xp="200" id="day-75" data-xp="200" data-xp="200">',
     '<div class="day-section" data-xp="200" id="day-75">'),
    ('<div class="day-section" data-xp="200" id="day-76" data-xp="200" data-xp="200">',
     '<div class="day-section" data-xp="200" id="day-76">'),
    ('<div class="day-section" data-xp="200" id="day-77" data-xp="200" data-xp="200">',
     '<div class="day-section" data-xp="200" id="day-77">'),
    ('<div class="day-section" data-xp="200" id="day-78" data-xp="200" data-xp="200">',
     '<div class="day-section" data-xp="200" id="day-78">'),
    ('<div <div="" class="misconception">', '<div class="misconception">'),
    ('<span class="X0 XP&lt;/span&gt; &lt;span class=" meta-badge="" pk"="">🎨 Phase 1 Design</span>',
     '<span class="meta-badge pk">🎨 Phase 1 Design</span>'),
    ('<span class="X0 XP&lt;/span&gt; &lt;span class=" meta-badge="" pk"="">🎨 Phase 2 Loops</span>',
     '<span class="meta-badge pk">🎨 Phase 2 Loops</span>'),
    ('<span class="X0 XP&lt;/span&gt; &lt;span class=" meta-badge="" pk"="">🎨 Phase 3 Model Save</span>',
     '<span class="meta-badge pk">🎨 Phase 3 Model Save</span>'),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f'Missing expected pattern: {old}')
    text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print('Updated week11.html structure fixes.')