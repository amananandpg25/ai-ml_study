import json
import os

transcript_path = "/Users/amananand/.gemini/antigravity/brain/5477403a-810b-4cb1-9c43-fef8e2255167/.system_generated/logs/transcript.jsonl"

if not os.path.exists(transcript_path):
    print("Transcript not found at", transcript_path)
    # Check parent dirs
    parent = os.path.dirname(transcript_path)
    if os.path.exists(parent):
        print("Files in parent:", os.listdir(parent))
else:
    print("Transcript size:", os.path.getsize(transcript_path))
    # Read last few lines to find USER_INPUT
    user_inputs = []
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'USER_INPUT':
                    user_inputs.append(data)
            except Exception as e:
                pass
    
    if user_inputs:
        last_input = user_inputs[-1]
        content = last_input.get('content', '')
        print("Found user input of length:", len(content))
        with open("/Users/amananand/Downloads/SDE/ai:ml/full_audit_report.html", "w", encoding="utf-8") as out:
            out.write(content)
        print("Written to /Users/amananand/Downloads/SDE/ai:ml/full_audit_report.html")
    else:
        print("No USER_INPUT found in transcript.")
