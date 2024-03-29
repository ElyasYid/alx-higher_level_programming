#!/usr/bin/python3
""" post email """
import requests
import sys


if __name__ == "__main__":
    eml = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=eml)
    print(req.text)
