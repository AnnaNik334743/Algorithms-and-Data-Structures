def explode(diagonal):
    n = len(diagonal)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = diagonal[i]
    return matrix


n = int(input())
arr = explode(list(map(int, input().split())))
for k in range(1, n):
    for i in range(k, n):
            j = i - k
            if (n-k) % 2 != 0:
                arr[i][j] = max(arr[i-1][j], arr[i][j+1])
            else:
                arr[i][j] = min(arr[i-1][j], arr[i][j+1])
print(arr[n-1][0])
