def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            squared = element ** 2
            new_row.append(squared)
        result.append(new_row)
    return result