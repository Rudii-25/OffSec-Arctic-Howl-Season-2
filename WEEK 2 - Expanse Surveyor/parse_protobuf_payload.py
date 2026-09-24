#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 2 Expanse Surveyor
Protobuf Payload Response Parser & InMemory DEX Extractor
"""

import sys

def extract_dex_from_protobuf(binary_data: bytes) -> bytes:
    """Scan raw protobuf buffer for embedded DEX header ('dex\n035\0')."""
    dex_magic = b"dex\n"
    idx = binary_data.find(dex_magic)
    if idx != -1:
        print(f"[+] Found DEX binary starting at offset 0x{idx:04x}")
        return binary_data[idx:]
    print("[-] No DEX magic header detected.")
    return b""

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[1], "rb") as f:
            raw = f.read()
        dex = extract_dex_from_protobuf(raw)
        if dex:
            with open(sys.argv[2], "wb") as out:
                out.write(dex)
            print(f"[+] Written extracted DEX payload to {sys.argv[2]}")
    else:
        print("[*] Usage: python3 parse_protobuf_payload.py <input.bin> <output.dex>")
