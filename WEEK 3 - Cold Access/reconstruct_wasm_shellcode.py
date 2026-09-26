#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 3 Cold Access
WASM JIT Shellcode Reconstructor
Parses float64 constants (f64.const, opcode 0x44) from wasmBuffer to extract x64 shellcode.
"""

import struct
import sys

def reconstruct_shellcode_from_wasm(wasm_bytes: bytes) -> bytes:
    """Extract 8-byte immediate floats from WASM f64.const instructions."""
    shellcode = bytearray()
    i = 0
    opcode_f64 = 0x44  # f64.const opcode in WebAssembly
    while i < len(wasm_bytes) - 8:
        if wasm_bytes[i] == opcode_f64:
            chunk = wasm_bytes[i + 1:i + 9]
            shellcode.extend(chunk)
            i += 9
        else:
            i += 1
    return bytes(shellcode)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[1], "rb") as f:
            raw_wasm = f.read()
        sc = reconstruct_shellcode_from_wasm(raw_wasm)
        with open(sys.argv[2], "wb") as f_out:
            f_out.write(sc)
        print(f"[+] Extracted {len(sc)} bytes of x64 shellcode to {sys.argv[2]}")
    else:
        print("[*] Usage: python3 reconstruct_wasm_shellcode.py <module.wasm> <shellcode.bin>")
