def needed(s):
    lst = list(map(int, str(s)))
    if sum(lst) % len(lst) == 0:
        return True
    return False


n = int(input())
counter = 0
i = 1
while counter != n:
    counter += 1 if needed(i) else 0
    i += 1
print(i - 1)
