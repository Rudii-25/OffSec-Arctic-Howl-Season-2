#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 4 Trusted Trouble
SMTP Traffic Forensics & Insider Correlation
Parses SMTP conversations to extract hiring candidates and correlates external IP artifacts.
"""

import re
import sys

HIRED_CANDIDATES = [
    "fernanda.ribeiro",
    "samuel.adu",
    "min-jun.park"
]

INSIDER_DROP_IP = "203.98.112.47"

def analyze_smtp_stream(log_or_stream_file: str):
    """Scan text or stream dump for Megacorp One application submissions."""
    applicants = set()
    with open(log_or_stream_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Find emails submitted to apply@megacorpone.com
    matches = re.findall(r"from:\s*<([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>", content, re.IGNORECASE)
    for m in matches:
        applicants.add(m.lower())

    print(f"[*] Total unique applicants identified: {len(applicants)}")
    for app in sorted(applicants):
        print(f"  [-] Applicant: {app}")

    if INSIDER_DROP_IP in content:
        print(f"[!] Target Exfil IP identified in stream: {INSIDER_DROP_IP}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_smtp_stream(sys.argv[1])
    else:
        print("[*] Usage: python3 analyze_smtp_traffic.py <mail_stream.txt>")
