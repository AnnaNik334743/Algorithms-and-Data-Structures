set1 = set()
for i in range(int(input())):
    set1.add(input())
set2 = set()
for i in range(int(input())):
    set2.add(input())
print('Friends:', ', '.join(sorted(set1)))
print('Mutual Friends:', ', '.join(sorted(set1.intersection(set2))))
print('Also Friend of:', ', '.join(sorted(set2 - set1)))
