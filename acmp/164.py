def flatten(string):
    if len(string) <= 1:
        if len(string) == 0:
            return None
        return int(string)
    return flatten(str(sum(list(map(int, string)))))


def main():
    init_str = input()
    for razdel in range(len(init_str)):
        if flatten(init_str[:razdel+1]) == flatten(init_str[razdel+1:]):
            return "YES"
    return "NO"


print(main())
