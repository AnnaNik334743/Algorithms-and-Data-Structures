n = int(input())
a, b = int(input()), int(input())
while a != b:
    if a > b:
        a //= 2
    else:
        b //= 2
print(a)
