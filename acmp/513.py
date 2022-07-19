from math import factorial


def colloc(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m))


n = int(input())
s = 0
for m in range(2, n+1):
    s += colloc(n, m)
print(int(s))
