#!/usr/bin/env python3
"""Atlas Ledger — hand the finished 26 November front page to the grader.

The picture is drawn beforehand by render.py (see BUILD.md for the 40
verified stories and the newspaper design). This program has one job:
carry entry.png, which sits next to it, into the directory the grader
names, byte for byte, after proving the file really is the PNG it claims
to be. Standard library only, no network, no randomness, no environment
reads for code — so two runs always produce the same bytes.
"""

import os
import sys
from hashlib import sha256
from pathlib import Path

PNG_SIGNATURE = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))
PNG_TRAILER = bytes((0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44,
                     0xAE, 0x42, 0x60, 0x82))  # IEND chunk: length 0 + "IEND" + CRC
MAX_BYTES = 1048576  # the gate refuses anything over 1 MiB
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"
READ_BLOCK = 1 << 16


def digest(path):
    """SHA-256 of a file, read in blocks so big files stay cheap."""
    total = sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(READ_BLOCK)
            if not block:
                break
            total.update(block)
    return total.hexdigest()


def deliver():
    """Copy SOURCE_IMAGE to the grader's output directory and verify it."""
    if not SOURCE_IMAGE.is_file():
        print(f"source image missing: {SOURCE_IMAGE}")
        return 1
    raw = SOURCE_IMAGE.read_bytes()
    if raw[:len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        print(f"source image is not a PNG: {SOURCE_IMAGE}")
        return 1
    if raw[-len(PNG_TRAILER):] != PNG_TRAILER:
        print(f"source image is truncated (no IEND): {SOURCE_IMAGE}")
        return 1
    if len(raw) > MAX_BYTES:
        print(f"source image over the 1 MiB limit: {len(raw)} bytes")
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(raw)
    if digest(target) != digest(SOURCE_IMAGE):
        print(f"copy does not match source: {target}")
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"sha256 {digest(target)})")
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
