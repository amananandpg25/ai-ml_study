import json

transcript_path = "/Users/amananand/.gemini/antigravity/brain/5477403a-810b-4cb1-9c43-fef8e2255167/.system_generated/logs/transcript.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            if 'Full Content Audit' in str(data):
                print(f"Line {i}: Type {data.get('type')}, Status {data.get('status')}")
                content = data.get('content', '')
                if isinstance(content, str):
                    print("  Length of content:", len(content))
                elif isinstance(content, dict):
                    print("  Content keys:", content.keys())
        except Exception as e:
            pass
