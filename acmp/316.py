from math import ceil

s = int(input())
b = 100 * (s // 107)
s %= 107
b += max(s - 7, 0)
print(b, 7 * ceil(b/100))
