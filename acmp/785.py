a, b = map(int, input().split())
for i in range(a, b + 1):
    if i**2 % (10 ** len(str(i))) == i:
        print(i, end=' ')
