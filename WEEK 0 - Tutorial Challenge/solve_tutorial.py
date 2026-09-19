#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 0 Tutorial Challenge
Web Server Log Analysis and Base64 Decoder
"""

import base64
import re
import sys

def decode_tutorial_flag(encoded_text: str) -> str:
    """Decode base64 string and extract flag."""
    decoded = base64.b64decode(encoded_text).decode("utf-8", errors="replace")
    match = re.search(r"'(TryHarder)'", decoded)
    return match.group(1) if match else "Flag not found"

def analyze_access_log(log_path: str):
    """
    Search access log for path traversal attempts and extract attacker IP,
    target resource, status code, and bytes transferred.
    """
    pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<uri>[^\s]+)\s+HTTP/[0-9.]+"\s+(?P<status>\d+)\s+(?P<bytes>\d+)'
    )
    traversal_hits = []
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if ".." in line or "id_rsa" in line:
                    match = pattern.search(line)
                    if match:
                        traversal_hits.append(match.groupdict())
    except FileNotFoundError:
        print(f"[-] File not found: {log_path}")
        return []
    return traversal_hits

if __name__ == "__main__":
    sample_b64 = "VGhlIGFuc3dlciB0byB0aGlzIGV4ZXJjaXNlIGlzICdUcnlIYXJkZXInIC0gbm90IGV4YWN0bHkgb3JpZ2luYWwsIGJ1dCBjbGVhcmx5IGVmZmVjdGl2ZS4="
    flag = decode_tutorial_flag(sample_b64)
    print(f"[+] Tutorial Flag: {flag}")
