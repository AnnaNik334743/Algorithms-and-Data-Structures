n, m = map(int, input().split())
steps = [list(map(int, input().split())) for row in range(n)]
steps[n-1][m-1] = 1
answer = [[0 for _ in range(m)] for _ in range(n)]
answer[0][0] = 1

for i in range(n):
    for j in range(m):
        step = steps[i][j]
        if step != 0:
            if i + step < n:
                answer[i + step][j] += answer[i][j]
            if j + step < m:
                answer[i][j + step] += answer[i][j]

print(answer[n-1][m-1])
