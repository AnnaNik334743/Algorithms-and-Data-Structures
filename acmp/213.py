n = int(input())
points = list(map(int, input().split()))
extra = int(input())
mx = -1
for i in range(1, int(input()) + 1):
    s = -2 * (i-1)
    k = 0
    for j, item in enumerate(input().split()):
        if item == '1':
            k += 1
            s += points[j]
    if k == n:
        s += extra
    mx = max(mx, s)
    print(mx)
