#!/usr/bin/python3
# This function prints x elements of a list
# x: number of elements to print
# Returns the real number of elements printed
def safe_print_list(my_list=[], x=0):
    i = -1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        i -= 1
        pass

    print()
    return i+1
