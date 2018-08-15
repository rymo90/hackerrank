matrix = []
for _ in range(6):
    matrix.append([int(i) for i in input().split()])

maxSum = -63
for i in range(len(matrix)-2):
    for j in range(len(matrix[i])-2):
        col1 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
        col2 = matrix[i+1][j+1]
        col3 = matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
        total = col1+col2+col3

        if maxSum < total:
            maxSum = total
print(maxSum)
