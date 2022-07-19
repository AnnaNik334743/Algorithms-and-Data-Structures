def convert_base(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def complexity(num):
    n = str(num) if isinstance(num, int) else num
    return len(n) + len(set(n))


n = int(input())
for _ in range(n):
    curr_num = int(input())
    best_comp = float('inf')
    best_osn = -1
    best_per = -1
    for osnovanie in range(2, 37):
        perevod = convert_base(curr_num, osnovanie)
        curr_comp = complexity(perevod)
        if curr_comp < best_comp:
            best_comp = curr_comp
            best_osn = osnovanie
            best_per = perevod
    print(best_osn, best_per)
