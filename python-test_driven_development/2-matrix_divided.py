#!/usr/bin/python3
"""
Bu modul matrisin bütün elementlərini bölən
matrix_divided funksiyasını təqdim edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.

    Args:
        matrix: Tam ədədlərdən və ya float-lardan ibarət listlər listi.
        div: Bölən ədəd (int və ya float).

    Returns:
        Hər elementi 2 onluq rəqəmə qədər yuvarlaqlaşdırılmış yeni matris.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matrisin list of lists olduğunu yoxla
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    # Hər sıranın daxilindəkilərin int/float olduğunu yoxla
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError(msg)

    # Sıraların ölçüsünün eyni olduğunu yoxla
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div-in rəqəm olduğunu yoxla
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Sıfıra bölünməni yoxla
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Yeni matris yarat və yuvarlaqlaşdırılmış nəticələri əlavə et
    return [[round(item / div, 2) for item in row] for row in matrix]
