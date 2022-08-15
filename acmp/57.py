# class Pig:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, i, x, y):
#
#

def get():
    return map(int, input().split())


def d(tup1, tup2):
    return ((tup1[0] - tup2[0])**2 + (tup1[1] - tup2[1])**2)**0.5


n, c, p = get()
pigs = []
for i in range(n):
    x, y = get()
    pigs.append((x, y))
nx, ny = get()
mn = float('inf')
for pig in pigs:
    dist = d(pig, (nx, ny))
    for pig2 in pigs:
        dist += d(pig, pig2)
    if dist < mn:
        mn = dist
print("YES" if c*mn <= p else "NO")
