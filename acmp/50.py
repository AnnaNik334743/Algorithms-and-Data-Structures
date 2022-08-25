from re import finditer

a = input()
b = input()
k = 0
cycles = set()
for i in range(len(b) + 1):
    cycles.add(b[i:] + b[:i])
for c in cycles:
    k += len([match.group(1) for match in finditer(f'(?=({c}))', a)])
print(k)
