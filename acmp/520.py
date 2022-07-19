p144, p12, p1 = 114000, 10250, 1050
n = int(input())
k144 = k12 = k1 = 0
k144, ost = divmod(n, 144)
if k144 <= ost // 12 * p12 + ost % 12 * p1:
    k144 += 1
else:
    k12, ost = divmod(ost, 12)
    if k12 <= ost * p1:
        k12 += 1
    else:
        k1 = ost
print(k144, k12, k1)

