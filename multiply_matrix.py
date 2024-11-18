def multiply_matrix(matrix1, matrix2) -> list[list[int]]:
    row1 = len(matrix1)
    col1 = len(matrix1[0]) 
    row2 = len(matrix2)
    col2 = len(matrix2[0]) 

    result = [[0 for _ in range(col2)] for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2, 3],
            [4, 5, 6]]

matrix2 = [[7, 8],
            [9, 10],
            [11, 12]]

result = multiply_matrix(matrix1, matrix2)

print("Result:")
for row in result:
    print(row)
