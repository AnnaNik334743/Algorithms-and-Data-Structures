n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for row in range(n)]
for i in range(1, n):
    matrix[i][0] += matrix[i-1][0]
for j in range(1, m):
    matrix[0][j] += matrix[0][j-1]

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

print(matrix[n-1][m-1])
