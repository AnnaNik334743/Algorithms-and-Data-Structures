from math import prod

l, r = map(int, input().split())
k = 0
for i in range(l, r+1):
    try:
        if i % prod(map(int, str(i))) == 0:
            k += 1
    except ArithmeticError:
        continue
print(k)
