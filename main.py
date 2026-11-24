#!/usr/bin/env python3
"""One Word for Your Wi-Fi: Molasses.

Writes a single word describing the entrant's Wi-Fi to /output/entry.txt.

The word is "Molasses". Home Wi-Fi as it is actually lived: pages ooze
in at the speed of cold molasses, the spinner hangs, the video drops to
a blur, everything arrives eventually but never when you need it. The
image needs no explaining, it is true of every slow connection, and the
speed angle is the one the field left empty: the visible entries argue
about ghosts and gaslighting while nobody names the slowness itself.

The gate wants UTF-8 text of 1 to 20 characters, not only whitespace.
"Molasses" is 8 characters, one word, no trailing newline.
"""

import os

WORD = "Molasses"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    # Gate checks, enforced before the file is trusted.
    text = WORD
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert "\n" not in text, "entry must carry no newline"
    assert 1 <= len(text) <= 20, "entry out of gate range"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Verify by reading back exactly what was written.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    assert back.decode("utf-8") == WORD, "read-back text mismatch"


if __name__ == "__main__":
    main()
