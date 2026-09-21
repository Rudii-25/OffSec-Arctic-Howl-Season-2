#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 1 First Tracks
Triple Hex Dropper Deobfuscator
"""

import sys

def decode_triple_hex(encoded_str: str) -> str:
    """Decode string obfuscated with 3 successive rounds of hex encoding."""
    current = encoded_str.strip().replace(" ", "").replace("\n", "")
    for round_idx in range(1, 4):
        try:
            byte_data = bytes.fromhex(current)
            current = byte_data.decode("utf-8", errors="replace")
            print(f"[+] Round {round_idx} decoded ({len(current)} chars)")
        except ValueError as e:
            print(f"[-] Hex decoding failed at round {round_idx}: {e}")
            break
    return current

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
        print(decode_triple_hex(data))
    else:
        print("[*] Usage: python3 decode_dropper.py <dropper_file>")
