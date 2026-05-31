import os, re

base = "/Users/amananand/Downloads/SDE/ai:ml"

# IDs that repeat per-day and need to be made unique by prefixing with day-N-
# We detect these by looking at per-day sections and any IDs that appear within them

def fix_duplicate_ids_in_week(fn):
    path = os.path.join(base, fn)
    c = open(path).read()
    
    # Find duplicate IDs
    ids = re.findall(r'id="([^"]+)"', c)
    from collections import Counter
    id_counts = Counter(ids)
    dupes = {id_: count for id_, count in id_counts.items() if count > 1}
    
    if not dupes:
        print(f"  ✅ {fn}: No duplicate IDs")
        return
    
    print(f"  🔧 {fn}: Fixing duplicates: {list(dupes.keys())}")
    
    # For each day section, we need to prefix the IDs within that day
    # Strategy: process each day section separately, making IDs unique
    # Day sections are bounded by <div id="day-N" ...> ... (next day or end)
    
    w = int(fn.replace("week","").replace(".html",""))
    
    # Get all day IDs
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', c)))
    
    # For each duplicate ID, we'll add a day prefix within each day's context
    # Approach: split content by day sections, fix IDs within each, rejoin
    
    new_c = c
    
    # For each duplicate, replace occurrences in a context-aware way
    for dup_id in dupes:
        # Skip day-N IDs themselves (they're not duplicated within a file)
        if dup_id.startswith('day-'):
            continue
        
        # Find all positions of this ID
        positions = [(m.start(), m.end()) for m in re.finditer(rf'id="{re.escape(dup_id)}"', new_c)]
        
        # Also find all href/for/aria-labelledby references to this ID
        ref_positions = []
        for ref_pattern in [rf'href="#{re.escape(dup_id)}"', rf'for="{re.escape(dup_id)}"',
                           rf'aria-labelledby="{re.escape(dup_id)}"', rf'aria-controls="{re.escape(dup_id)}"']:
            for m in re.finditer(ref_pattern, new_c):
                ref_positions.append((m.start(), m.end(), m.group(0)))
        
        if len(positions) <= 1:
            continue
        
        # Determine which day section each occurrence falls in
        # We'll build a lookup of day start positions
        day_starts = {}
        for d in day_ids:
            match = re.search(rf'id="day-{d}"', new_c)
            if match:
                day_starts[d] = match.start()
        
        sorted_days = sorted(day_starts.items(), key=lambda x: x[1])
        
        def get_day_for_pos(pos):
            """Find which day section a position falls in"""
            result = None
            for d, start in sorted_days:
                if pos >= start:
                    result = d
                else:
                    break
            return result
        
        # Replace from the end to avoid position shifts
        replacements = []  # (start, end, new_text)
        
        for i, (start, end) in enumerate(positions):
            day = get_day_for_pos(start)
            if day is not None and i > 0:  # Keep first occurrence as-is only if it's different day
                new_id = f"day-{day}-{dup_id}"
                replacements.append((start, end, f'id="{new_id}"'))
            elif day is not None and i == 0:
                # First occurrence in its day
                new_id = f"day-{day}-{dup_id}"
                replacements.append((start, end, f'id="{new_id}"'))
        
        # Apply replacements from end to start
        replacements.sort(key=lambda x: x[0], reverse=True)
        for start, end, new_text in replacements:
            new_c = new_c[:start] + new_text + new_c[end:]
    
    # Also update JavaScript getElementById calls for the fixed IDs
    # The JS typically uses 'theory', 'quiz-section' etc. without day prefix
    # These are usually generic containers, so we need to be careful
    # For now, skip JS updates as these IDs are not used in JS (they're section containers)
    
    open(path, "w").write(new_c)
    
    # Verify
    new_ids = re.findall(r'id="([^"]+)"', new_c)
    from collections import Counter
    new_counts = Counter(new_ids)
    remaining_dupes = {id_: count for id_, count in new_counts.items() if count > 1}
    if remaining_dupes:
        print(f"    ⚠️  Remaining dupes after fix: {list(remaining_dupes.keys())}")
    else:
        print(f"    ✅ All duplicates resolved")

for w in range(1, 19):
    fix_duplicate_ids_in_week(f"week{w}.html")

print("\nDone!")
