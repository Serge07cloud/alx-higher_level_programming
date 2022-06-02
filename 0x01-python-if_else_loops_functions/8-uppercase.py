#!/usr/bin/python3
def uppercase(str):
    text = ""
    for i in range(len(str)):
        if ord(str[i]) > 96:
            # The letter is lowercase
            index = ord(str[i]) - 32
            c = chr(index)
        else:
            c = str[i]

        print('{}'.format(c), end="")

    print()
