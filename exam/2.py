n, i, j = map(int, input().split())
x = i if i < j else j
y = i if i > j else j
l, r = 0, (n-1) * y
while l != r:
    mid = (l + r) // 2
    j = mid // x + mid // y
    if j < n - 1:
        l = mid + 1
    else:
        r = mid
print(x + r)
