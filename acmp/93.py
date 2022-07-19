def check(s1, s2):
    if len(s1) != len(s2):
        return False
    k = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            k += 1
            if k > 1:
                return False
    if k == 1:
        return True
    return False


correct = []
incorrect = []
for _ in range(int(input())):
    correct.append(input())
for _ in range(int(input())):
    incorrect.append(input())
for word in correct:
    k = 0
    for word2 in incorrect:
        if check(word, word2):
            k += 1
    print(k, end=' ')
