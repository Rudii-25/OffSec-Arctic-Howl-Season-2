#!/usr/bin/env python3
"""
OffSec Arctic Howl - Season 2: Week 4 Trusted Trouble
Exfiltrated Database Credential Extractor
Simulates unpacking of note3 archive and queries sensitive.db for compromised user credentials.
"""

import sqlite3
import sys

def dump_credentials(db_path: str):
    """Query sensitive.db SQLite database for high-privilege credentials."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        print(f"[*] Tables found: {[t[0] for t in tables]}")
        
        for table in tables:
            tname = table[0]
            print(f"\n[*] Dumping rows from {tname}:")
            cur.execute(f"SELECT * FROM {tname} LIMIT 10;")
            for row in cur.fetchall():
                print(f"  {row}")
        conn.close()
    except Exception as e:
        print(f"[-] Database extraction error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dump_credentials(sys.argv[1])
    else:
        print("[*] Target credential: Robin Schwartz / 5up3r5Tr0NgP@$$w0rd!")
        print("[*] Usage: python3 decrypt_sensitive_db.py <sensitive.db>")
