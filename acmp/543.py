n, w, d, p = map(int, input().split())
ans = int((n * (n-1) / 2 * w - p) // d)
print(n if ans == 0 else ans)
