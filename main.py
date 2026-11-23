"""Write the six-word story to /output/entry.txt.

The story is exactly six words: She / left; / the / lighthouse / kept / shining.
"""
from pathlib import Path

STORY = "She left; the lighthouse kept shining."


def main():
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(STORY, encoding="utf-8")
    print(f"Wrote {len(words)}-word story to {output}")


if __name__ == "__main__":
    main()
