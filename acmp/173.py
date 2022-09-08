def palindrom(s):
    if type(s) is not str:
        s = str(s)
    l = len(s) // 2
    return True if s[:l] == (s[-l:])[::-1] or len(s) == 1 else False


def conv(n, rad):
    if type(n) is not int:
        n = int(n)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r = ""
    while n > 0:
        k = n % rad
        r = digits[k] + r
        n = n // rad
    return r


n = int(input())
ans = []
for i in range(2, 37):
    if palindrom(conv(n, i)):
        ans.append(i)
if len(ans) == 0:
    print('none')
elif len(ans) == 1:
    print('unique')
    print(ans[0])
else:
    print('multiple')
    print(*ans)
