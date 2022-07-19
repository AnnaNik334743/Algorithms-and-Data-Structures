string = input()
n = len(string)
a, b = 1, 1
while b <= n:
    print(string[b - 1], end='')
    a, b = b, a + b
