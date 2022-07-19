n = int(input())
initial = list(map(int, input().split()))
index = [-1 for i in range(len(initial))]
path = [10**9 + 1 for i in range(n+1)]
path[0] = -10**9 - 1
counter = 0
for i in range(n):
    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if path[mid] >= initial[i]:
            right = mid
        else:
            left = mid
    if path[right] == 10**9 + 1:
        counter += 1
    path[right] = initial[i]
    index[i] = right - 1
print(counter)
