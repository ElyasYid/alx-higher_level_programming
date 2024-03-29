#!/usr/bin/python3
"""
sends request to URL displays the body response in utf8
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as f:
            print(f.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
