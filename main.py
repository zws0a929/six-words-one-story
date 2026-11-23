"""Write the six-word story to /output/entry.txt."""
from pathlib import Path

STORY = "She left; the lighthouse kept shining."


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
