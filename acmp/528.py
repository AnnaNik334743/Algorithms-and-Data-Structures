n, k = map(int, input().split())
s = 1
for i in range(k):
    s += n * (i + 1) - 2 * i - 1
print(s)
