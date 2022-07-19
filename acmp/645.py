k = int(input())
cost = float('inf')
answer = 0
for h in range(1, int(k**0.5) + 1):
    w = k // h
    if abs(h - w) + k - h * w < cost:
        cost = abs(h - w) + k - h * w
        answer = (h, w)
print(*answer)
