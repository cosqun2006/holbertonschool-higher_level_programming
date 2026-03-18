#!/usr/bin/python3
"""
Bu modul matrixin bolunmesi funksiaysini temsil edir
"""

def matrix_divided(matrix, div):
    """
        Matrisin bütün elementlərini verilmiş rəqəmə bölür.

        Args:
            matrix (list of lists): İnt və ya float-lardan ibarət matris.
            div (int/float): Bölən rəqəm.

        Returns:
            list of lists: Bölünmüş və yuvarlaqlaşdırılmış yeni matris.
        """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element/div, 2) for element in row] for row in matrix]
