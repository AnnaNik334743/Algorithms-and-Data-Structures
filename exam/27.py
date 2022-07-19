def floyd(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix


def answer():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        for i in range(n):
            if row[i] == 100000:
                row[i] = float('inf')
        matrix.append(row)
    matrix = floyd(matrix)
    for i in range(n):
        if matrix[i][i] < 0:
            return "YES"
    return "NO"


print(answer())
