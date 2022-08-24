k, m, n, d = map(int, input().split())
for i in range(10000):
    if i % k == 0 and i % m == 0 and i % n == 0:
        if i / k + i / m + i / n + d == i:
            print(i)
            break
else:
    print(-1)
