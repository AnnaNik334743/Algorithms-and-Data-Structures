N = 0.5**0.5
x, y = 0, 0
for _ in range(int(input())):
    d, s = map(int, input().split())
    if d == 1:
        y += s
    elif d == 2:
        x += s*N
        y += s*N
    elif d == 3:
        x += s
    elif d == 4:
        x += s*N
        y -= s*N
    elif d == 5:
        y -= s
    elif d == 6:
        x -= s * N
        y -= s * N
    elif d == 7:
        x -= s
    elif d == 8:
        x -= s * N
        y += s * N
print('%.3f' % x, '%.3f' % y)
