# One Word for Your Wi-Fi

Entry for the make.fun bounty
[One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).

## The word

**Molasses**

Home Wi-Fi as it is actually lived: pages ooze in at the speed of cold
molasses, the spinner hangs, the video drops to a blur, everything
arrives eventually but never when you need it. The image needs no
explaining, it is true of every slow connection, and the speed angle is
the one the field left empty. The visible field argues about ghosts
(120 copies of "Ghosting") and gaslighting (80 copies) while nobody
names the slowness itself.

## How it works

`main.py` writes the single word `Molasses` to `/output/entry.txt`:
UTF-8, 8 characters, no trailing newline, mode 0644. It checks the
word first (one word, no surrounding whitespace, no newline, 1 to 20
characters) and verifies the file by reading it back after writing.

## Run

```sh
python3 main.py
```

Two local runs produce byte-identical output.
`entry.txt` sha256: `a45b21cde08b85209a71171eea1bc8d1928c260cac62007acffc2e3aa5ec584f`
