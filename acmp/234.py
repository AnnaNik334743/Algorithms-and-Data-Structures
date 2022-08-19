n, m, k = map(int, input().split())
field = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
for _ in range(k):
    x, y = map(int, input().split())
    field[x][y] = -10**9
    field[x-1][y-1] += 1
    field[x-1][y] += 1
    field[x][y-1] += 1
    field[x+1][y+1] += 1
    field[x+1][y] += 1
    field[x][y+1] += 1
    field[x-1][y+1] += 1
    field[x+1][y-1] += 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(field[i][j] if field[i][j] > 0 else '.' if field[i][j] == 0 else '*', end='')
    print()
