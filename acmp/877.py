lines = open('input.txt').readlines()
n = len(lines)
name = ''
for i, line in enumerate(lines):
    if i != 0 and i != n-1:
        meaningful = line[10:].strip()
        if meaningful[-1] != '!' and meaningful[-1] != '?' and meaningful[-1] != '.':
            print(f'"{meaningful}," --- skazal {"Fedya" if i % 2 != 0 else name}.')
        elif meaningful[-1] == '.':
            print(f'"{meaningful[:-1]}," --- skazal {"Fedya" if i % 2 != 0 else name}.')
        else:
            print(f'"{meaningful}" --- skazal {"Fedya" if i % 2 != 0 else name}.')
    else:
        name = line.split()[1]

