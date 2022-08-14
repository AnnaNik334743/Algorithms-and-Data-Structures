screen = [list(input()) for _ in range(int(input().split()[0]))]
input()
screen2 = [list(input()) for _ in range(len(screen))]
ans_up, ans_low = [], []
for i, row in enumerate(screen):
    for j in range(len(row)):
        if screen[i][j] != screen2[i][j] and screen[i][j] != '.':
            if screen[i][j].isupper():
                ans_up.append(screen[i][j])
            else:
                ans_low.append(screen[i][j])
print(len(ans_up) + len(ans_low))
print(''.join(sorted(ans_low) + sorted(ans_up)))
