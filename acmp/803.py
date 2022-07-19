a, b, k=map(int, input().split())
for _ in range(k+1):
    c, a=divmod(a, b)
    a *= 10
print(c)
