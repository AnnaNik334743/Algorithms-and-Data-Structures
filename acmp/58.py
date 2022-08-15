

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(input().split()) for _ in range(n)]
    for i in range(0, n-1):
        for j in range(0, m-1):
            if len(set([arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1]])) == 1:
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')



