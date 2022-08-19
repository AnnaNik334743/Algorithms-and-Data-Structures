from copy import deepcopy


n, m, k = map(int, input().split())
field_prev = [list(input()) for _ in range(n)]
field_next = deepcopy(field_prev)
for epoch in range(k):
    for i in range(n):
        for j in range(m):
            neis = [(i-1, j-1), (i, j-1), (i-1, j), (i-1, (j+1) % m), (i, (j+1) % m),
                    ((i+1) % n, j-1), ((i+1) % n, j), ((i+1) % n, (j+1) % m)]
            alive = 0
            for coord in neis:
                if field_prev[coord[0]][coord[1]] == '*':
                    alive += 1
            field_next[i][j] = '*' if (field_prev[i][j] == '.' and alive == 3) \
                                      or (field_prev[i][j] == '*' and 2 <= alive <= 3) else '.'
    field_prev = field_next
    field_next = deepcopy(field_prev)
for row in field_next:
    print(''.join(row))
