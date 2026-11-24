"""Sum up 23 November 2026 world news in one image.

Deterministic, no network: copies the bundled entry.png
(a 1024x1024 PNG, 595,779 bytes) to /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)

if __name__ == "__main__":
    main()
