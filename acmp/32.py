import re


def transform_both(a: str, b: str):
    if a[0] == '-' and b[0] == '-':
        return int(transform(a, 'min')) - int(transform(b, 'max'))
    elif a[0] == '-' and b[0] != '-':
        return int(transform(a, 'min')) - int(transform(b, 'min'))
    elif a[0] != '-' and b[0] == '-':
        return int(transform(a, 'max')) - int(transform(b, 'max'))
    else:
        return int(transform(a, 'max')) - int(transform(b, 'min'))


def transform(n: str, t='min'):
    if n[0] == '-':
        n = n[1:]
        n_new = '-'
    else:
        n_new = ''
    zeros = len(re.findall('0', n)) * '0'
    n = re.sub('0', '', n)
    if t == 'min':
        n = ''.join(sorted(n))
        if len(n) == 0:
            n_new += zeros
        elif len(n) == 1:
            n_new += n[0] + zeros
        else:
            n_new += n[0] + zeros + n[1:]
    else:
        n = ''.join(sorted(n, reverse=True))
        n_new += n + zeros
    return n_new


print(transform_both(input(), input()))
