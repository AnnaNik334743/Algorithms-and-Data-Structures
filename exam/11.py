n = int(input())
money = list(map(int, input().split()))[::-1]
mx = money[0]
s = 0
for i in range(n):
    if money[i] > mx:
        mx = money[i]
    s += mx
print(s)
