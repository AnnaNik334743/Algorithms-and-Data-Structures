d1, d2, d3, d4 = {}, {}, {}, {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y == 0:
        continue
    k = y / x if x != 0 else 'inf'
    if y >= 0 and x >= 0:
        try:
            d1[k] += 1
        except KeyError:
            d1[k] = 1
    elif y <= 0 <= x:
        try:
            d2[k] += 1
        except KeyError:
            d2[k] = 1
    elif y <= 0 and x <= 0:
        try:
            d3[k] += 1
        except KeyError:
            d3[k] = 1
    elif y >= 0 >= x:
        try:
            d4[k] += 1
        except KeyError:
            d4[k] = 1

print(len(d1) + len(d2) + len(d3) + len(d4))
