import json

transcript_path = "/Users/amananand/.gemini/antigravity/brain/5616e22c-5d10-479d-909f-5bb666154d2d/.system_generated/logs/transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step is not None and step < 2500:
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    name = tc.get("name")
                    args = tc.get("args")
                    if isinstance(args, str):
                        args = json.loads(args)
                    if name == "run_command":
                        cmd = args.get("CommandLine") or ""
                        if "scratch/" in cmd or "python" in cmd:
                            print(f"Step: {step}, Run: {cmd}")
        except Exception as e:
            pass
