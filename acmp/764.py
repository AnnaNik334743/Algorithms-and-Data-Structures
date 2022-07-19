d1, d2, d3, d4 = {}, {}, {}, {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    k = y / x if x != 0 else 'inf'
    if y >= 0 and x >= 0:
        try:
            d1[k] += 1
        except KeyError:
            d1[k] = 1
    if y <= 0 and x >= 0:
        try:
            d2[k] += 1
        except KeyError:
            d2[k] = 1
    if y <= 0 and x <= 0:
        try:
            d3[k] += 1
        except KeyError:
            d3[k] = 1
    if y >= 0 and x <= 0:
        try:
            d4[k] += 1
        except KeyError:
            d4[k] = 1
print(max(list(d1.values()) + list(d2.values()) + list(d3.values()) + list(d4.values())))
