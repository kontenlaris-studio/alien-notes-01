#!/usr/bin/env python3
"""Write the alien field note about Earth to /output/entry.txt."""

import os

LINE = "4/5. The locals pay a stranger to shout their name wrong on a paper cup, then drink it happily. I have never felt more at home. Would return."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
