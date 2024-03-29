#!/usr/bin/python3
""" sends a request displays the body of the response"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    req = requests.get(URL)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
