n = int(input())
arr = list(map(int, input().split()))
d = {i: 0 for i in range(-100, 101)}
for a in arr:
    d[a] += 1
mx, k = max(d.items(), key=lambda x: (x[1], -x[0]))
for a in arr:
    if a != mx:
        print(a, end=' ')
else:
    for _ in range(k):
        print(mx, end=' ')
