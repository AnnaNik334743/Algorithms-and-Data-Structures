# в sympy есть функция isprime

def value(num):
    return sum(map(int, list(str(num))))


def simple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


a, b = map(int, input().split())
mx = 0
mxnum = -1
for val in range(a + 1, b + 1):
    if simple(val):
        curr = value(val)
        if curr >= mx:
            mx = curr
            mxnum = val
print(mxnum)