#!/usr/bin/python3
"""
sends a request to the URL and displays the value
of the X-Request-Id var
"""
import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]

    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as f:
        print(dict(f.headers).get("X-Request-Id"))
