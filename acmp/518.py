n, k = map(int, input().split())

matrix = [['1' for _ in range(n+2)]]
for _ in range(n):
    matrix.append(['1'] + list(input()) + ['1'])
matrix.append(['1' for _ in range(n+2)])

answer = [[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(k+1)]
answer[0][1][1] = 1

for step in range(1, k+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == '0':
                answer[step][i][j] = answer[step-1][i-1][j] + answer[step-1][i][j-1] + answer[step-1][i+1][j] + answer[step-1][i][j+1]

print(answer[k][n][n])
