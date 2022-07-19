n, m = map(int, input().split())
na = set(map(int, input().split()))
ma = list(map(int, input().split()))
for i in ma:
    print("YES" if i in na else "NO", end=' ')
