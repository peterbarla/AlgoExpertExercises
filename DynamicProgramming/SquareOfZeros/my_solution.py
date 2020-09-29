# O(n^4) time | O(1) space
def squareOfZeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(1, len(matrix)):
                if isSquare(i, i + k, j, j + k, matrix) and hasBordersZero(i, i + k, j, j + k, matrix):
                    return True
    return False

def isSquare(r1, r2, c1, c2, matrix):
    return r1 < len(matrix) and r2 < len(matrix) and c1 < len(matrix) and c2 < len(matrix)

def hasBordersZero(r1, r2, c1, c2, matrix):
    for i in range(r1, r2 + 1):
        if matrix[i][c1] != 0 or matrix[i][c2] != 0:
            return False
    for i in range(c1, c2 + 1):
        if matrix[r1][i] != 0 or matrix[r2][i] != 0:
            return False
    return True

matrix = [[0, 0],
          [0, 0]]

print(squareOfZeroes(matrix))