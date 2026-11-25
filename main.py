"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a To: line naming
who the message was meant for, and the unsent message itself on the next line,
exactly as it was typed, with nothing after it.
"""

from pathlib import Path

TO_LINE = "To: the nurse on night shift, ward 6"
MESSAGE = (
    "I told Dad you were the one who held his hand that last night because "
    "I sat in the car park till it was over, too scared to come back up, "
    "and I never thanked you for lying for me."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TO_LINE + "\n" + MESSAGE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
