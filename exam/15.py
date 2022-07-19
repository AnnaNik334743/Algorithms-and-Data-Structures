n = int(input())
arr = list(map(int, input().split()))
mina, maxa = 101, -101
k, sum, maxi, mini = 1, 0, 0, 0
for i, a in enumerate(arr):
    if a > 0:
        sum += a
    if a < mina:
        mina = a
        mini = i
    if a > maxa:
        maxa = a
        maxi = i
for i in range(min(mini, maxi)+1, max(mini, maxi)):
   k *= arr[i]
print(sum, k)
