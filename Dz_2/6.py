def countSquares(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
    count = 0
    for i in matrix:
        count += sum(i)
    return count

