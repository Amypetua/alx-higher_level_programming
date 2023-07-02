#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    """ Method to find the peak or highest number in an array """
    if bool(list_of_integers) is False:
        return (None)

    list_of_integers.sort()
    return (list_of_integers[-1])
