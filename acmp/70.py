s = input()
k = int(input())
if k > 0:
    if k * len(s) <= 1023:
        print(s * k)
    else:
        print((s * (1023 // len(s) + 1))[:1023])
else:
    k = abs(k)
    # надо найти в строке цикл, который повторяется k раз
    if len(s) % k != 0:
        print('NO SOLUTION')
    else:
        pattern = s[:len(s) // k]
        if s == pattern * k:
            print(pattern if len(pattern) <= 1023 else pattern[:1023])
        else:
            print('NO SOLUTION')
