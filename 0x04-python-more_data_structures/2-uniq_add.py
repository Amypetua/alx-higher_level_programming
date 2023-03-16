#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    for num in my_list:
        if isinstance(num, int) and num not in unique_integers:
            unique_integers.add(num)
    sum_unique_integers = sum(unique_integers)

    return sum_unique_integers
