import json

transcript_path = "/Users/amananand/.gemini/antigravity/brain/5477403a-810b-4cb1-9c43-fef8e2255167/.system_generated/logs/transcript.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                if 'Full Content Audit' in content:
                    print("USER_INPUT content length in transcript line:", len(content))
                    print("Last 100 characters of USER_INPUT:")
                    print(repr(content[-100:]))
        except Exception as e:
            pass
