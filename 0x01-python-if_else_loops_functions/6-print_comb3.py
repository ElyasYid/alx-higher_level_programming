#!/usr/bin/python3
for u1 in range(0, 10):
    for u2 in range(u1 + 1, 10):
        if u1 == 8 and u2 == 9:
            print("{}{}".format(u1, u2))
        else:
            print("{}{}".format(u1, u2), end=", ")
