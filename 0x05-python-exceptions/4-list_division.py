#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    res = [0 for i in range(list_length)]
    low = min(len(my_list_1), len(my_list_2))

    for i in range(low):

        if type(my_list_1[i]) is int or type(my_list_1[i]) is float:
            if type(my_list_1[i]) is int or type(my_list_1[i]) is float:
                try:
                    quotient = my_list_1[i] / my_list_2[i]
                    res.insert(i, quotient)
                except ZeroDivisionError:
                    print("division by 0")
                    pass
                finally:
                    pass
            else:
                print("wrong type")
        else:
            print("wrong type")
    if list_length > low:
        print('out of range')

    return res
