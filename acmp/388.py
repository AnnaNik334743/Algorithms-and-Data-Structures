n, m = map(int, input().split())
mins = [float('inf') for _ in range(n)]
maxes = [float('-inf') for _ in range(m)]
for i in range(n):
    row = list(map(int, input().split()))
    for j, elem in enumerate(row):
        if elem < mins[i]:
            mins[i] = elem
        if elem > maxes[j]:
            maxes[j] = elem
k = 0
for mn in mins:
    for mx in maxes:
        if mn == mx:
            k += 1
print(k)
