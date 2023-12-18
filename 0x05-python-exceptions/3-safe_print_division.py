#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        slash = a / b
    except (TypeError, ZeroDivisionError):
        slash = None
    finally:
        print("Inside result: {}".format(slash))
    return (slash)
