bag1 = []
bag2 = []
n, m = map(int, input().split())
for _ in range(n):
    bag1 += list(input())
for _ in range(m):
    bag2 += list(input())
for letter in bag2:
    bag1.remove(letter)
print("".join(sorted(bag1)))
