def square_matrix_simple(matrix=[]):
    squares = []
    newmatrix = []
    for i in range(len(matrix)):
        actual = matrix[i]
        for j in range(len(actual)):
            squares.append(actual[j - 1] * actual[j - 1])
        squares.sort()
        newmatrix.append(squares)
        squares = []
    return(newmatrix)
