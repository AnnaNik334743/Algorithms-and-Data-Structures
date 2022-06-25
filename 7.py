n = int(input())
init = []
for _ in range(n):
    line = list(map(int, list(input())))
    init.append(line)

for x in range(1, n):
    init[0][x] += init[0][x-1]
    init[x][0] += init[x-1][0]
for i in range(1, n):
    for j in range(1, n):
        init[i][j] += min(init[i-1][j], init[i][j-1])

i, j = n-1, n-1
while i != 0 and j != 0:
    init[i][j] = '#'
    if init[i][j-1] < init[i-1][j]:
        j -= 1
    else:
        i -= 1

if i > 0:
    for x in range(i, -1, -1):
        init[x][0] = '#'
elif j > 0:
    for x in range(j, -1, -1):
        init[0][x] = '#'

for row in init:
    for item in row:
        print('#' if item == '#' else '.', end='')
    print()
