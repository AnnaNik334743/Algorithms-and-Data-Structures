k, n = map(int, input().split())
ladder = [0 for _ in range(n + 1)]
ladder[0] = 1
for i in range(n):
    for j in range(1, k + 1):
        if i + j <= n:
            ladder[i + j] += ladder[i]
        else:
            break
print(ladder[-1])
