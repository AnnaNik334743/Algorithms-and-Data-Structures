# в этой задаче проблемы с вводом-выводом, потоковый не работает корректно

def check(line):
    stack = []
    for i in line:
        if i in "([{":
            stack.append(i)
        else:
            if len(stack) > 0 and \
                    (i == ")" and stack[-1] == "(" or i == "]" and stack[-1] == "[" or i == "}" and stack[-1] == "{"):
                stack.pop()
            else:
                return 1
    return 0 if len(stack) == 0 else 1


with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        lines = infile.readlines()
        for line in lines:
            print(check(line.strip()), end='', file=outfile)
