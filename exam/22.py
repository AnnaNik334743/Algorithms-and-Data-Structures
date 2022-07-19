def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


n = int(input())
coords = []
for _ in range(n):
    coords.append(tuple(map(int, input().split())))
dists = set()
for i in range(n):
    for j in range(i + 1, n):
        dists.add(distance(coords[i], coords[j]))
print(len(dists))
for i in sorted(dists):
    print(i)
