#!/usr/bin/python3
def uniq_add(my_list=[]):
    brand_new = set(my_list)
    poki = 0
    for f in brand_new:
        poki += f
    return poki
