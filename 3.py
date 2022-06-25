n = int(input())
a = sorted(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[1] = a[1] - a[0]
if n == 2:
    print(dp[1])
if n > 2:
    dp[2] = a[2] - a[0]
    for i in range(3, n):
        dp[i] = min(dp[i-1], dp[i-2]) + a[i] - a[i-1]
    print(dp[n-1])
