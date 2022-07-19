n = 30000
input()
ind = map(int, input().split())

a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

line = "".join(map(str, [i for i in a if i != 0]))
for i in ind:
    print(line[i-1], end='')
