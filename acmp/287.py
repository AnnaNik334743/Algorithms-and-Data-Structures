n, m = map(int, input().split())
string = input()
s = set()
for i in range(n - m + 1):
    s.add(string[i:i+m])
print(len(s))
