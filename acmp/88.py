def main():
    n = int(input())
    ideal = [i for i in range(1, n**2 + 1)]
    sudoku = [list(map(int, input().split())) for _ in range(n**2)]
    sudokut = [[sudoku[j][i] for j in range(n**2)] for i in range(n**2)]
    for i in range(n**2):
        if sorted(sudoku[i][:]) != ideal or sorted(sudokut[i][:]) != ideal:
            return 'Inc'
    for i in range(0, n**2, n):
        for j in range(0, n**2, n):
            inner = []
            for x in range(i, i+n):
                inner.extend(sudoku[x][j:j+n])
            if sorted(inner) != ideal:
                return 'Inc'
    return 'C'


print(main() + 'orrect')
