#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square_row = []
        for element in row:
            square_row.append(element**2)

        new_matrix.append(square_row)
    return new_matrix
