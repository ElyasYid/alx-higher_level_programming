#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list provided"""

    if list_of_integers is None or list_of_integers == []:
        return None
    btm = 0
    top = len(list_of_integers)
    cnt = ((top - btm) // 2) + btm
    cnt = int(cnt)
    if top == 1:
        return list_of_integers[0]
    if top == 2:
        return max(list_of_integers)
    if list_of_integers[cnt] >= list_of_integers[cnt - 1] and\
            list_of_integers[cnt] >= list_of_integers[cnt + 1]:
        return list_of_integers[cnt]
    if cnt > 0 and list_of_integers[cnt] < list_of_integers[cnt + 1]:
        return find_peak(list_of_integers[cnt:])
    if cnt > 0 and list_of_integers[cnt] < list_of_integers[cnt - 1]:
        return find_peak(list_of_integers[:cnt])
