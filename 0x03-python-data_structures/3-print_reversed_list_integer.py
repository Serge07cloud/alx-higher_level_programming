#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_copy = my_list.copy()
    list_copy.reverse()
    for i in range(len(list_copy)):
        print('{:d}'.format(list_copy[i]))
