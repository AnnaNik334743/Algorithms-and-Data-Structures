input()
back = []
for i, item in enumerate(sorted(list(map(int, input().split())))):
    if i % 2 == 0:
        print(item, end=' ')
    else:
        back.append(item)
print(*back[::-1])
