n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
mn = 10**9
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            if matrix[i][j] + matrix[j][k] + matrix[k][i] < mn:
                mn = matrix[i][j] + matrix[j][k] + matrix[k][i]
print(mn)
