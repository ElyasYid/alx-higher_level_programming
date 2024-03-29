#!/usr/bin/python3
"""
sends a POST reques, takes email as a parameter
& displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    eml = {"email": sys.argv[2]}
    val = urllib.parse.urlencode(eml).encode("ascii")

    rq = urllib.request.Request(URL, val)
    with urllib.request.urlopen(rq) as f:
        print(f.read().decode("utf-8"))
