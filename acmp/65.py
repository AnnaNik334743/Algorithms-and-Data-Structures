def dist(s1, s2):
    k = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            k += 1
    return k


s = input()
mn = float('inf')
dists = []
for i in range(int(input())):
    dists.append(dist(s, input()))
    if dists[-1] < mn:
        mn = dists[-1]
answer = []
for i, elem in enumerate(dists):
    if elem == mn:
        answer.append(i+1)
print(len(answer))
print(*answer)
