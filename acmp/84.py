n, m = map(int, input().split())
l = u = 10**9
r = d = 0
a = [list(input()) for _ in ' '*n]
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            if j < l:
                l = j
            if j > r:
                r = j
            if i < u:
                u = i
            if i > d:
                d = i
for i in range(n):
    for j in range(m):
        a[i][j] = '*' if u <= i <= d and l <= j <= r else '.'
for o in a:
    print(*o, sep='')
