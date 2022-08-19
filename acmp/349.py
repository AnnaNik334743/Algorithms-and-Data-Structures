s, n = map(int, input().split())
a = [i for i in range(n+1)]
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
a = set(a)
a.remove(0)
f = 1
for i in sorted(a):
    if s <= i <= n:
        print(i)
        f = 0
if f:
    print("Absent")
