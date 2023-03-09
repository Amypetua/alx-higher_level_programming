#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, subtract(a, b)))
    print("{} * {} = {}".format(a, b, multiply(a, b)))
    print("{} / {} = {}".format(a, b, divide(a, b)))
