#!/usr/bin/python3

def multiple_returns(sentence):
    if lenlen(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
