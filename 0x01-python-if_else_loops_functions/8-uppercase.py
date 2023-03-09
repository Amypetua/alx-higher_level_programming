#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 65 and  ord(a) <=90:
            print("{}".format(a))
