#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 3 Cold Access
Shellcode Disassembler & Command Extractor
Disassembles extracted x64 shellcode using Capstone and identifies the WinExec payload string.
"""

import sys

def analyze_shellcode(shellcode_bytes: bytes):
    """Scan shellcode for printable ASCII strings and disassemble if Capstone is present."""
    # Look for embedded command strings like 'ping db'
    print(f"[*] Analyzing {len(shellcode_bytes)} bytes of shellcode...")
    
    # Simple ASCII string hunt
    current = []
    found_strings = []
    for b in shellcode_bytes:
        if 32 <= b <= 126:
            current.append(chr(b))
        else:
            if len(current) >= 4:
                found_strings.append("".join(current))
            current = []
    if current and len(current) >= 4:
        found_strings.append("".join(current))
    
    print(f"[+] Found ASCII strings in shellcode: {found_strings}")

    try:
        from capstone import Cs, CS_ARCH_X86, CS_MODE_64
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        print("[*] Disassembly snippet (first 30 instructions):")
        count = 0
        for i in md.disasm(shellcode_bytes, 0x1000):
            print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
            count += 1
            if count >= 30:
                break
    except ImportError:
        print("[!] Capstone engine not installed. Install with 'pip install capstone' for full disassembly.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "rb") as f:
            data = f.read()
        analyze_shellcode(data)
    else:
        # Sample test with embedded "ping db"
        dummy = b"\x48\x31\xc0\x48\x8d\x0d\x08\x00\x00\x00\xff\xd0\x70\x69\x6e\x67\x20\x64\x62\x00"
        analyze_shellcode(dummy)
