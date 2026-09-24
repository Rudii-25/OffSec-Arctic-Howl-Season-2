#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 2 Expanse Surveyor
HAR Traffic Forensic Inspector
Parses HTTP Archive (.har) to isolate C2 telemetry, location pings, and chunk uploads.
"""

import json
import sys

def parse_har_evidence(har_file: str):
    """Analyze HTTP requests in HAR export for exfiltration endpoints."""
    with open(har_file, "r", encoding="utf-8") as f:
        har = json.load(f)
    
    entries = har.get("log", {}).get("entries", [])
    print(f"[*] Total entries in HAR: {len(entries)}")
    
    for idx, entry in enumerate(entries):
        req = entry.get("request", {})
        url = req.get("url", "")
        method = req.get("method", "")
        status = entry.get("response", {}).get("status", 0)
        
        if "ngrok" in url or "backup/chunk" in url or "geotag" in url:
            time_stamp = entry.get("startedDateTime", "")
            print(f"[{time_stamp}] {method} {url} -> Status {status}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_har_evidence(sys.argv[1])
    else:
        print("[*] Usage: python3 extract_har_traffic.py <traffic.har>")
