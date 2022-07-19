a, b, c, d, s = map(int, input().split())
p = print
if s <= c:
    p(s * a / c)
elif c <= d:
    p('NO')
else:
    x = c - d
    e = (c - s) // x * -1
    s -= e * x
    p(e * (a + b) + s * a / c)
