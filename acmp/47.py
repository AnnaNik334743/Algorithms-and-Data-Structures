def sum_d(num):
    s = 0
    while num > 0:
        s += num % 10
        num /= 10
    return s


n = int(input())
best = 1
best_sum = 1
for i in range(2, n+1):
    if n % i == 0:
        d = sum_d(i)
        if d > best_sum or d == best_sum and i < best:
            best = i
            best_sum = d
print(best)
