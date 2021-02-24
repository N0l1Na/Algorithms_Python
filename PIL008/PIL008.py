"""

PIL - The exercise is taken from the Pilshchikov's Pascal problem book

Task 9.2 page 48
Regular types: matrix

Specify the variable types
A, A[3], A[9][18], A[1][1], B, B[15], B[3], B[10][16]

"""

n = 10
first_matrix = [[0 for i in range(n)] for i in range(n)]
n = 10
matrix1 = [[0 for i in range(n)] for i in range(5)]
for i in range(n):          #task A
    matrix1[i][i] = i
    print(matrix1[i])
