input()
s, order, tour = 0, 1, 0
throws = list(map(int, input().split()))
for i in range(len(throws)):
    if order == 1:
        tour += 1
    if tour < 10:
        if throws[i] == 10 and order == 1:
            s += 10 + sum(throws[i+1:i+3])
            order = 1
        elif i != 0 and throws[i-1] + throws[i] == 10 and order == 2:
            s += throws[i] + sum(throws[i+1:i+2])
            order = 1
        else:
            s += throws[i]
            order = 2 if order == 1 else 1
    else:
        if throws[i] == 10 and order == 1:
            s += 10 + sum(throws[i+1:])
            break
        elif throws[i-1] + throws[i] == 10 and order == 2:
            s += throws[i] + sum(throws[i+1:])
            break
        else:
            s += throws[i]
        order += 1
print(s)
