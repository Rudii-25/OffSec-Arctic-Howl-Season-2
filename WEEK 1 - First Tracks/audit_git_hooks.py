#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 1 First Tracks
Git Hook Supply Chain Security Auditor
Scans directory trees for compromised or injected .git/hooks/pre-commit scripts.
"""

import os
import sys

SUSPICIOUS_STRINGS = [
    "bu1knames.io",
    "osascript",
    "base64 -d",
    "curl",
    "jez",
    "cozfi"
]

def scan_repository_hooks(root_dir: str):
    """Walk directories to find .git/hooks files and flag anomalies."""
    flagged = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if ".git" in dirpath and "hooks" in dirpath:
            for file in filenames:
                hook_path = os.path.join(dirpath, file)
                try:
                    with open(hook_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    matches = [s for s in SUSPICIOUS_STRINGS if s in content]
                    if matches:
                        flagged.append((hook_path, matches))
                except (PermissionError, IsADirectoryError):
                    continue
    return flagged

if __name__ == "__main__":
    scan_path = sys.argv[1] if len(sys.argv) > 1 else "."
    results = scan_repository_hooks(scan_path)
    if results:
        print(f"[!] Warning: {len(results)} suspicious Git hook(s) discovered:")
        for path, indicators in results:
            print(f"  [-] {path} -> Matches: {', '.join(indicators)}")
    else:
        print("[+] No compromised Git hooks found in target directory.")
