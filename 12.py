def NesYo(sub, init):
    if len(sub) > len(init):
        return "NO"
    else:
        i = 0
        for let_sub in sub:
            if i == len(init):
                return "NO"
            while init[i] != let_sub:
                i += 1
                if i == len(init):
                    return "NO"
            else:
                i += 1
    return "YES"


print(NesYo(input(), input()))
