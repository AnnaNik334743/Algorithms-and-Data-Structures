n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
deleted = 0
c = 0
while deleted != n-1:
    for i in range(len(arr)):
        if deleted == n-1:
            break
        if arr[i] != -1:
            c += 1
            if c % k == 0:
                arr[i] = -1
                deleted += 1
for a in arr:
    if a != -1:
        print(a)
        break
