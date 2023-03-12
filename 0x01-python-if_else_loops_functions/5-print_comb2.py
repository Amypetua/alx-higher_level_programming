#!/usr/bin/python3
for i in range(0, 100):
    print("{}{}".format((i // 10), (i % 10)), end="" if i == 99 else ", ")
