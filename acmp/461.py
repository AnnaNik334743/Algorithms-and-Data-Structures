def div2(n):
    if n % 2 == 0:
        return n // 2 + 1
    return (n + 1) // 2


n = int(input())
arr = sorted(list(map(int, input().split())))[:div2(n)]
s = 0
for i in arr:
    s += div2(i)
print(s)
