n = bin(int(input()))
l = len(n) - 2
n = n[2:] + n[2:-1]
mx = '0' * l
for i in range(len(n) - l + 1):
    if n[i:i+l] > mx:
        mx = n[i:i+l]
print(int(mx, 2))
