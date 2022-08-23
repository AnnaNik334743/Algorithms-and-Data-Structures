from itertools import combinations as c


i = input
r = print
i()
m = 0
l = []
for t in c(enumerate(list(map(int, i().split()))), 3):
    a, b, c = t[0][1], t[1][1], t[2][1]
    p = (a + b + c) / 2
    u = p * (p - a) * (p - b) * (p - c)
    s = u ** 0.5 if u > 0 else 0
    if s > m:
        m = s
        l = [t[0][0] + 1, t[1][0] + 1, t[2][0] + 1]
if m > 0:
    r(m)
    r(*l)
else:
    r(-1)

