#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:2d}".format(row[i]), end=" ")
            print()
