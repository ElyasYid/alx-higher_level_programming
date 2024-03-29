#!/usr/bin/python3
"""fetches an URL with requests package"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    p = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(p), p))
