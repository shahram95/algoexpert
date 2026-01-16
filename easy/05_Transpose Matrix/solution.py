def transposeMatrix(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    matrixT = [[None for _ in range(numRows)] for _ in range(numCols)]

    for i in range(numRows):
        for j in range(numCols):
            matrixT[j][i] = matrix[i][j]
    return matrixT