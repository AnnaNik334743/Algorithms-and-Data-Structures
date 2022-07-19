arr = [0 for _ in range(300_000)]
curr = 0
for n in range(1, int(input())):
    arr[curr] = 1
    curr += 3 if arr[n] == 1 else 2
print(curr + 1)
