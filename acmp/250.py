def g(x):
    return len(set(str(x))) < 3


n = int(input())
p = print
i = 0
while 1:
    if g(n-i) and n > i:
        p(n-i)
        break
    if g(n+i):
        p(n+i)
        break
    i += 1
