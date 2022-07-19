k = 0
x, y, z, w = map(int, input().split())
for nx in range(w // x + 1):
    leftw = w - nx * x
    for ny in range(leftw // y + 1):
        leftleftw = leftw - ny * y
        if leftleftw % z == 0:
            k += 1
print(k)
