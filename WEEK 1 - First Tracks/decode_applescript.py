#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 1 First Tracks
7-Layer Nested Base64 AppleScript Unpacker
"""

import base64
import re
import sys

def unpack_nested_base64(raw_payload: str, max_layers: int = 10) -> str:
    """Recursively unpack nested Base64 payloads."""
    current = raw_payload.strip()
    layer = 0
    while layer < max_layers:
        b64_candidate = re.search(r"[A-Za-z0-9+/=]{16,}", current)
        if not b64_candidate:
            break
        try:
            decoded = base64.b64decode(b64_candidate.group(0)).decode("utf-8", errors="replace")
            layer += 1
            print(f"[+] Unpacked Layer {layer} (length: {len(decoded)})")
            current = decoded
        except Exception:
            break
    return current

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        print(unpack_nested_base64(content))
    else:
        print("[*] Usage: python3 decode_applescript.py <payload_file>")
