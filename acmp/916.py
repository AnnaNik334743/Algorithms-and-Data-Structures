n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))[::-1]
s, i = 0, 0
while i < n:
    s += a[i] * (1 + i // k)
    i += 1
print(s)
