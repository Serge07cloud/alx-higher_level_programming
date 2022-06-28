#!/usr/bin/python3
# This function prints an integer value
# Returns True if the value to print is an interger else print False
def safe_print_integer(value):

    try:

        print("{:d}".format(value))

        return True

    except (ValueError, TypeError):

        return False
