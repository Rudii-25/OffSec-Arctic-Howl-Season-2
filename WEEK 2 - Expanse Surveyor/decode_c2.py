#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 2 Expanse Surveyor
Android C2 Resolution: 15-Round Base64 Decode + XOR "blastoise"
"""

import base64
import sys

def resolve_c2_address(raw_gist_content: str) -> str:
    """Perform 15 rounds of Base64 decoding followed by XOR decryption with key 'blastoise'."""
    data = raw_gist_content.strip().encode("utf-8")
    for i in range(15):
        data = base64.b64decode(data)
    
    xor_key = b"blastoise"
    result = bytearray(len(data))
    for j in range(len(data)):
        result[j] = data[j] ^ xor_key[j % len(xor_key)]
    
    return result.decode("utf-8", errors="replace")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()
        print(f"[+] Resolved C2: {resolve_c2_address(content)}")
    else:
        print("[*] Usage: python3 decode_c2.py <gist_content.txt>")
