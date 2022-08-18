a, b = input().split()
f = 1
if len(a) != len(b) or set(a) != set(b):
    f = 0
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            f = 0
print("YES" if f else "NO")
