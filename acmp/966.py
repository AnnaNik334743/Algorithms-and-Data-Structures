init_list = [0 for _ in range(1001)]
for _ in range(int(input())):
  l, r, v = map(int, input().split())
  for i in range(l, r):
    init_list[i] += v
p = 0
for i in range(min(1001, int(input()))):
  p = max(0, p + init_list[i])
print(p)
