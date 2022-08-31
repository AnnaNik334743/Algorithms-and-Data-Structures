class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def s(a, b, c):
    return abs(0.5*((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)))


lim = 0.0001
k = 0
for _ in range(int(input())):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    i, a, b, c, d = Point(x, y), Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)
    overall_s = s(a, b, c) + s(b, c, d)
    from_p = s(a, b, i) + s(b, c, i) + s(c, d, i) + s(d, a, i)
    if from_p - overall_s <= lim:
        k +=1
print(k)
