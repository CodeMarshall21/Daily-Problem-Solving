def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    tmat = [[0]*row for _ in range(col)]
    
    for i in range(row):
        for j in range(col):
            tmat[j][i] = matrix[i][j]
    return tmat

matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))
