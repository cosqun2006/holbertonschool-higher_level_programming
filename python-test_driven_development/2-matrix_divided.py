#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matris yoxlanışı
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # div yoxlanışı
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Sətir və element yoxlanışı
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            # Buradakı yoxlama həm int, həm float (inf/nan daxil) qəbul edir
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Hesablama hissəsi
    # float('inf') gələndə element / div avtomatik 0.0 qaytaracaq
    return [[round(element / div, 2) for element in row] for row in matrix]
