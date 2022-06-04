#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    import os

    dirs = os.listdir('.')
    if len(argv) == len(dirs) + 3:
        # All files and directories are listed when *
        # is passed as command line argument
        # If total number of argument egals
        # total numbers of current directory's files and folders
        # We can assume it is a multiplication
        a = int(argv[1])
        op = '*'
        b = int(argv[len(argv) - 1])
        print('{} {} {} = {}'.format(a, op, b, mul(a, b)))
    else:
        if len(argv) == 4 and argv[2] in '+-/':

            a = int(argv[1])
            op = argv[2]
            b = int(argv[3])
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            else:
                result = div(a, b)
            print('{} {} {} = {}'.format(a, op, b, result))

        elif len(argv) != 4:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
            exit(1)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
