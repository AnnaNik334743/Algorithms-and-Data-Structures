# на Python TLE, на PyPy всё супер

n = int(input())
dp = []
for i in range(n):
    row = [0] * (i+1) + list(map(int, input().split()))
    dp.append(row)
for row in range(2, n+1):
    i, j = 0, row
    while i < n + 1 - row:
        mn = dp[i][j]
        for x in range(i + 1, j):
            if dp[i][x] + dp[x][j] < mn:
                mn = dp[i][x] + dp[x][j]
        dp[i][j] = mn
        i += 1
        j += 1
print(dp[0][n])
