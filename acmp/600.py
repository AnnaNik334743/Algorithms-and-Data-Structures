for _ in range(int(input())):
    w = input()
    f = 1
    i = 0
    while i < len(w) and w[i] == '0':
        i += 1
    k = i
    while i < len(w) and w[i] == '1':
        i += 1
    if i != 2 * k:
        print("NO")
        f = 0
    else:
        while i < len(w) and w[i] == '2':
            i += 1
        if i != 3 * k or i != len(w):
            print("NO")
            f = 0
    if f:
        print("YES")
