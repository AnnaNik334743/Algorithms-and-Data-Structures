m = [[0 for _ in range(10)] for _ in range(10)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    m[a][b] = 1
k = 0
for i in range(10):
    for j in range(10):
        if m[i][j] == 1:
            if m[i-1][j] == 0:
                k += 1
            if m[i+1][j] == 0:
                k += 1
            if m[i][j-1] == 0:
                k += 1
            if m[i][j+1] == 0:
                k += 1
print(k)
