import re
import os

def check_unbalanced_days(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all day sections
    day_matches = list(re.finditer(r'<div class="day-section[^>]*id="day-([^"]+)"[^>]*>', content))
    
    errors = []
    for i, m in enumerate(day_matches):
        day_id = m.group(1)
        start_pos = m.end()  # start right after the opening tag
        
        if i < len(day_matches) - 1:
            end_pos = day_matches[i+1].start()
        else:
            # For the last day, find where the main layout ends (e.g. </main> or </div><!-- /layout -->)
            layout_end = content.find('</div><!-- /layout -->', start_pos)
            if layout_end != -1:
                end_pos = layout_end + len('</div><!-- /layout -->')
            else:
                end_pos = len(content)
                
        subcontent = content[start_pos:end_pos]
        
        # Count divs in this day's content
        # Note: since we started AFTER the opening <div class="day-section">,
        # but we include the closing </div><!-- /day-X --> of this section,
        # we expect the number of closing </div> tags to be exactly 1 more than opening <div tags.
        # i.e., close_count - open_count = 1
        # Let's count:
        open_count = len(re.findall(r'<div\b', subcontent))
        close_count = len(re.findall(r'</div>', subcontent))
        
        diff = close_count - open_count
        if diff != 1:
            # If it's the last day, and we went to the end of the file, it might include the layout closing div
            # which would make diff = 2 (one for day, one for layout). Let's account for that.
            if i == len(day_matches) - 1 and diff == 2:
                continue
            errors.append((day_id, open_count, close_count, diff))
            
    return errors

def main():
    directory = '/Users/amananand/Downloads/SDE/ai:ml'
    files = sorted([f for f in os.listdir(directory) if f.endswith('.html') and f.startswith('week')])
    for filename in files:
        filepath = os.path.join(directory, filename)
        errs = check_unbalanced_days(filepath)
        if errs:
            print(f"Unbalanced days in {filename}:")
            for day_id, op, cl, diff in errs:
                print(f"  Day {day_id}: open={op}, close={cl}, close-open={diff} (expected 1)")
        else:
            print(f"{filename} is perfectly balanced across all days!")

if __name__ == '__main__':
    main()
