n = int(input())
a = [2, 3, 4, 7, 13, 15]
b = [1, 5, 6, 8, 9, 10, 11, 12, 14]
i_a = 6
for i in range(n - 5):
    a.append(b[i_a - 1] + b[i_a - 3])
    i_a += 1
    item = a[-2] + 1
    while item < a[-1]:
        b.append(item)
        item += 1
print(a[n-1], b[n-1], sep='\n')
