def func(let1, let2, f):
    if let1 == '0' and let2 == '0':
        return f[0]
    if let1 == '0' and let2 == '1':
        return f[1]
    if let1 == '1' and let2 == '0':
        return f[2]
    return f[3]


n, m = map(int, input().split())
pic1 = [list(input()) for _ in range(m)]
pic2 = [list(input()) for _ in range(m)]
f = input()
for i in range(m):
    for j in range(n):
        print(func(pic1[i][j], pic2[i][j], f), end='')
    print()

