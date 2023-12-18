#!/usr/bin/python3

def magic_calculation(a, b):

    value = 0
    for kev in range(1, 3):
        try:
            if kev > a:
                raise Exception('Too far')
            value += a ** b / kev
        except Exception:
            value = b + a
            break
    return value
