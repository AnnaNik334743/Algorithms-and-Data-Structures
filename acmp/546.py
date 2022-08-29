from math import ceil

n = int(input())
n_pages = ceil(n / 4)
first_row = []
second_row = []
for i in range(1, n_pages+1):
    first_row.extend([i, i])
    second_row.extend([1, 2])
progression = [i if i <= n else 0 for i in range(1, n_pages * 4 + 1)]
third_row = progression[:len(progression) // 2]
fourth_row = progression[len(progression) // 2:][::-1]
for i in range(len(third_row)):
    if i % 2 == 0:
        third_row[i], fourth_row[i] = fourth_row[i], third_row[i]
for i in range(len(first_row)):
    print(first_row[i], second_row[i], third_row[i], fourth_row[i])

