def dist(coords1, coords2):
    return ((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)**0.5

init = list(map(int, input().split()))
x = []
y = []
for i, item in enumerate(init):
    if i % 2 == 0:
        x.append(item)
    else:
        y.append(item)
points = list(zip(x, y))
zero_one = dist(points[0], points[1])
one_two = dist(points[1], points[2])
zero_two = dist(points[0], points[2])
mx = max(zero_one, one_two, zero_two)
if mx == zero_one:
    vect = (points[0][0] - points[2][0], points[0][1] - points[2][1])
    print(vect[0] + points[1][0], vect[1] + points[1][1])
elif mx == one_two:
    vect = (points[1][0] - points[0][0], points[1][1] - points[0][1])
    print(vect[0] + points[2][0], vect[1] + points[2][1])
else:
    vect = (points[0][0] - points[1][0], points[0][1] - points[1][1])
    print(vect[0] + points[2][0], vect[1] + points[2][1])
