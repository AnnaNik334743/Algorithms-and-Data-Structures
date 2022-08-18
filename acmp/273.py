from itertools import combinations

print(len(list(filter(lambda t: len(str(int(''.join(t)))) == 3, set(combinations(input(), 3))))))
