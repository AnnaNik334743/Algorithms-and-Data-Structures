def conv(n, rad):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r = ""
    while n > 0:
        k = n % rad
        r = digits[k] + r
        n = n // rad
    return r


d, m, y = map(int, input().split('/'))
o = d + 1
print('/'.join([conv(d, o), conv(m, o), conv(y, o)]))
