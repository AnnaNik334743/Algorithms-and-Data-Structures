n = int(input())
arr = list(input().split())
rules = int(input())
rules_dict = {}
for _ in range(rules):
    was, will = input().split()
    rules_dict[was] = will
for i in range(n):
    try:
        arr[i] = rules_dict[arr[i]]
    except Exception:
        pass
print(*arr)
