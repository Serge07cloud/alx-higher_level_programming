#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    def square(value):
        return value ** 2

    s = [[0] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            s[i][j] = square(matrix[i][j])
    return s
