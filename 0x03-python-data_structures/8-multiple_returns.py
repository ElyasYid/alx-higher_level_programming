#!/usr/bin/python3
def multiple_returns(sentence):
    mine_tuple = ()
    if len(sentence) == 0:
        mine_tuple = 0, "None"
    else:
        mine_tuple = len(sentence), sentence[0]
    return mine_tuple
