def simple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    n = list(input())
    if '0' in n:
        return 'No'
    return 'Yes' if simple(int(''.join(sorted(n)))) and simple(int(''.join(sorted(n, reverse=True)))) else 'No'


print(main())
