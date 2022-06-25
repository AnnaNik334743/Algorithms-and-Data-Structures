import math

w, h, n = map(int, input().split())
l, r = 0, math.ceil((w*h*n)**0.5) * max(h, w)
m = r // 2
while r - l > 1:
    if (m // h) * (m // w) >= n:
        r = m
    else:
        l = m
    m = (r + l) // 2
print(r)
