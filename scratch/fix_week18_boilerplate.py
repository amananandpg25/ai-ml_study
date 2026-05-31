from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "week18.html"


def main() -> None:
    text = FILE.read_text(encoding="utf-8")

    analogy_pattern = re.compile(
        r'<div class="analogy">Jaise kitchen mein alag-alag recipes ke liye ingredients ka preparation zaroori hota hai, vaise hi ([^<]+) ke liye data preprocessing aur parameter check sabse basic step hai\.</div>'
    )
    text = analogy_pattern.sub(
        lambda match: (
            f'<div class="analogy">Before you scale {match.group(1)}, verify the inputs, dependencies, and deployment steps first.</div>'
        ),
        text,
    )

    misconception_pattern = re.compile(
        r'<strong>⚠️ Common Misconception:</strong> ([^<]+) hamesha baseline parameters ke sath bina tuning ke perfectly kaam karega\.'
    )
    text = misconception_pattern.sub(
        lambda match: (
            f'<strong>⚠️ Common Misconception:</strong> {match.group(1)} needs validation, iteration, and rollback plans.'
        ),
        text,
    )

    FILE.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()