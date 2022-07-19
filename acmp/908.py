n = int(input())
arr = [float('inf') for _ in range(n+1)]
arr[1] = 0
for i in range(1, n+1):
    curr = i + 1
    if curr <= n:
        arr[curr] = min(arr[curr], arr[i] + 1)
    curr = i * 2
    if curr <= n:
        arr[curr] = min(arr[curr], arr[i] + 1)
    curr = i * 3
    if curr <= n:
        arr[curr] = min(arr[curr], arr[i] + 1)
print(arr[n])
