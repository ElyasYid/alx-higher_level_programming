#!/usr/bin/python3
"""
sends POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    ltr = "" if len(sys.argv) == 1 else sys.argv[1]
    pd = {"q": ltr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pd)
    try:
        say = req.json()
        if say == {}:
            print("No result")
        else:
            print("[{}] {}".format(say.get("id"), say.get("name")))
    except ValueError:
        print("Not a valid JSON")
