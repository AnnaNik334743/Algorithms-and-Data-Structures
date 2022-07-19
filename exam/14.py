n = int(input())
m = list(map(int, input().split()))
a = [0]*201
for i in range(n):
    a[m[i] + 100] += 1
for i in range(201):
    print((str(i-100)+' ')*a[i], end='')
