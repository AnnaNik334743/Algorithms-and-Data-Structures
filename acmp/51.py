n, k = input().split()
n = int(n)
k = len(k)
i = 0
fact = 1
while n - i*k > 0:
    fact *= (n - i*k)
    i += 1
print(fact)
