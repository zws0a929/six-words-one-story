"""Six-word story writer: emit the story to /output/entry.txt."""

from pathlib import Path

WORDS = ["She", "left;", "the", "lighthouse", "kept", "shining."]
OUTPUT_PATH = Path("/output/entry.txt")


def build_story(words):
    story = " ".join(words)
    if len(words) != 6:
        raise ValueError(f"a six-word story needs 6 words, got {len(words)}")
    return story


def main():
    story = build_story(WORDS)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(story, encoding="utf-8")
    print(f"Wrote {len(WORDS)}-word story to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
