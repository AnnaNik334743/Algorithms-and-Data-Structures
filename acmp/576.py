from math import gcd

n = int(input())
k = 0
for m in range(1, n):
    if gcd(m, n) == 1:
        k += 1
print(k)
