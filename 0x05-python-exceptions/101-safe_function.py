#!/usr/bin/python3

from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        bactrica = fct(*args)
    except Exception as z:
        print("Exception: {}".format(z), file=sys.stderr)
        return None
    else:
        return bactrica
