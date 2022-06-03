#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    var = dir(hidden_4)
    for i in range(len(var)):
        if var[i][:2] != '__':
            print('{}'.format(var[i]))
