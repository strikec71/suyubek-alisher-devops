#!/usr/bin/env python3
"""Wait for readiness and verify the running container's identity."""
import json
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen
from app.main import student_info

base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"
for attempt in range(30):
    try:
        with urlopen(base + "/health", timeout=2) as response:
            if response.status != 200 or response.read().strip() != b"OK":
                raise ValueError("Invalid health response")
        break
    except (URLError, TimeoutError, ConnectionError):
        if attempt == 29:
            raise SystemExit("Application was not ready within the retry limit")
        time.sleep(1)
with urlopen(base + "/student", timeout=3) as response:
    actual = json.load(response)
expected = student_info()
if actual != expected:
    raise SystemExit(f"Student mismatch: expected {expected}, received {actual}")
print("HTTP health and all four student fields verified:", actual)
