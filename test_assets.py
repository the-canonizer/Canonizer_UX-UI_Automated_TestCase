"""On-demand image fixtures for the upload tests.

The upload scenarios used to reference absolute paths on one developer's
machine, so they could never pass anywhere else. These helpers build real PNG
files under .test_assets/ the first time they are needed, and reuse them after
that. The directory is git-ignored.
"""

import os
import struct
import zlib
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parent / ".test_assets"

# The application rejects uploads larger than this.
MAX_UPLOAD_BYTES = 5 * 1024 * 1024


def _png_chunk(tag, data):
    """Build one length-prefixed, CRC-suffixed PNG chunk."""
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def _write_png(path, width, height):
    """Write a valid 8-bit RGB PNG filled with random pixels.

    Random bytes do not compress and the zlib stream is stored rather than
    deflated, so the resulting size is predictable at roughly
    height * (1 + width * 3) bytes.
    """
    raw = bytearray()
    for _ in range(height):
        raw.append(0)  # filter type 0 (None) for this scanline
        raw.extend(os.urandom(width * 3))

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    idat = zlib.compress(bytes(raw), 0)

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(b"\x89PNG\r\n\x1a\n")
        handle.write(_png_chunk(b"IHDR", ihdr))
        handle.write(_png_chunk(b"IDAT", idat))
        handle.write(_png_chunk(b"IEND", b""))


def _ensure(name, width, height, is_right_size):
    path = ASSET_DIR / name
    if not path.exists() or not is_right_size(path.stat().st_size):
        _write_png(path, width, height)
        size = path.stat().st_size
        if not is_right_size(size):
            raise AssertionError(
                "Generated %s is %d bytes, which is not the size this test needs."
                % (name, size)
            )
    return str(path)


def image_over_5mb():
    """Absolute path to a valid PNG larger than the upload limit."""
    return _ensure("oversize.png", 1500, 1500, lambda size: size > MAX_UPLOAD_BYTES)


def image_under_5mb():
    """Absolute path to a valid PNG comfortably under the upload limit."""
    return _ensure("sample.png", 200, 200, lambda size: 0 < size < MAX_UPLOAD_BYTES)
