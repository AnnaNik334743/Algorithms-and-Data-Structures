n = int(input())
cap = sorted(list(map(int, input().split())))
init = int(input())
i = 0
while i < n and ((cap[i] + init) / 2 >= init or cap[i] <= init):
    if cap[i] > init:
        init = (cap[i] + init) / 2
    i += 1
print('%.6f' % init)
