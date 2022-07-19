n = int(input())
timing = []
for _ in range(n):
    timing.append(tuple(map(int, input().split())))
dp = [0 for _ in range(n)]
dp[0] = timing[0][0]
if n > 1:
    dp[1] = min(timing[0][1], timing[0][0] + timing[1][0])
    if n > 2:
        dp[2] = min(timing[0][2], timing[0][1] + timing[2][0], timing[0][0] + timing[1][1],
                    timing[0][0] + timing[1][0] + timing[2][0])
        for i in range(3, n):
            dp[i] = min(dp[i-3] + timing[i-2][2], dp[i-2] + timing[i-1][1], dp[i-1] + timing[i][0])
print(dp[n-1])
