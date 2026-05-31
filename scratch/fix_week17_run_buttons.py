from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "week17.html"


def main() -> None:
    text = FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        r'(<button class="copy-btn" onclick="copyCode\(this\)">copy</button>)'
        r'(?:<button class="run-btn" onclick="runCode\(this\)" style="margin-left: 4px;">Run</button>){3}'
    )
    replacement = r'\1<button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button>'
    updated = pattern.sub(replacement, text)
    FILE.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()