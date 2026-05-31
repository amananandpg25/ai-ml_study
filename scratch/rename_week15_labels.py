from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "week15.html"


def main() -> None:
    text = FILE.read_text(encoding="utf-8")
    text = text.replace("LLM Engineering", "LLMs + Generative AI + OpenAI APIs")
    text = text.replace("LLM ENGINEERING", "LLMs + Generative AI + OpenAI APIs")
    FILE.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()