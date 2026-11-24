"""The Robot Apology — entrypoint for make.fun bounty
u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix.

Standard library only — the grading sandbox installs nothing.
"""

import os

ENTRY = (
    "I'm sorry I deleted the only photo of your grandmother's birthday "
    "because the blur looked like a mistake to me.\n"
    "I learned a blur can still be a memory, so now I ask before I delete "
    "anything with a face in it.\n"
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-400 UTF-8 chars,
    # not only whitespace. Fail loudly here rather than ship invalid text.
    text = ENTRY.strip()
    if not text or len(ENTRY) > 400:
        raise SystemExit(f"entry invalid: {len(ENTRY)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
