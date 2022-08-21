a, b = map(lambda x: list(x)[::-1], input().split())
m = max(len(a), len(b)) + 1
ans = [0]*m
left = 0
for i in range(m-1):
    curr = left
    try:
        curr += int(a[i])
    except:
        pass
    try:
        curr += int(b[i])
    except:
        pass
    left, ans[i] = divmod(curr, 3)
if left != 0:
    ans[-1] = left
else:
    ans = ans[:-1]
ans = ''.join(map(str, ans[::-1]))
print(int(ans, 3))

# коротко то же самое:
# print(sum(map(lambda x: int(x, 3), input().split())))
