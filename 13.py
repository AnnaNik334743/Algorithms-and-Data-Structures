summa, kolvo = map(int, input().split())
dmx = {}
for i in range(9, 0, -1):
    dmx[str(i)] = summa // i
    summa %= i
mx = ""
for para in dmx.items():
    mx += para[0] * para[1]
if kolvo - len(mx) > 0:
    k = kolvo - len(mx)
    mx += "0" * k
mn = mx[::-1]
if mn[0] == "0":
    mn = "1" + mn[1:k] + str(int(mn[k]) - 1) + mn[k+1:]
print(mx, mn)
