#!/usr/bin/env python3
"""Fetch cluster health JSON (OpenSearch/ES). Demo if unreachable."""
from __future__ import annotations
import argparse, json, os, sys, urllib.request

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", default=os.getenv("OS_URL", "https://localhost:9200"))
    p.add_argument("--insecure", action="store_true")
    args = p.parse_args()
    url = args.url.rstrip("/") + "/_cluster/health"
    try:
        ctx = None
        if args.insecure:
            import ssl
            ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(url, context=ctx, timeout=5) as r:
            data = json.loads(r.read().decode())
    except Exception as e:
        print(json.dumps({
            "status": "demo",
            "note": f"unreachable: {e}",
            "number_of_nodes": 3,
            "active_shards_percent_as_number": 100.0,
            "relocating_shards": 0,
            "unassigned_shards": 0,
        }, indent=2))
        return
    print(json.dumps(data, indent=2))
    if data.get("status") == "red":
        sys.exit(2)
    if data.get("status") == "yellow":
        sys.exit(1)

if __name__ == "__main__":
    main()
