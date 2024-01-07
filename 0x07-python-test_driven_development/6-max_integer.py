#!/usr/bin/python3
"""Module to find max int in list"""


def max_integer(list=[]):
    """ func to find max int in list
        if none returns none"""

    if len(list) == 0:
        return None
    xmas = list[0]
    j = 1
    while j < len(list):
        if list[j] > xmas:
            xmas = list[j]
        j += 1
    return xmas
