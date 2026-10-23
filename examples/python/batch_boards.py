"""Collect two Greenhouse boards in one bounded run."""
import json
from pathlib import Path
from client import collect

if __name__ == "__main__":
    payload = {"boardUrls": ["airbnb", "stripe"], "includeContent": True,
               "maxJobsPerBoard": 5, "maxTotalJobs": 10, "continueOnError": True}
    items, complete = collect(payload)
    Path("greenhouse-batch.json").write_text(json.dumps(items, indent=2), encoding="utf-8")
    print(f"Saved {len(items)} jobs. Check SUMMARY for individual board coverage.")
    raise SystemExit(0 if complete else 2)
