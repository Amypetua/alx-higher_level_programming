#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]
    for i in range(2):
        if len(a) <= i:
            a += (0,)
        if len(b) <= i:
            b += (0,)
    result = (a[0] + b[0], a[1] + b[1])
    return (result)
