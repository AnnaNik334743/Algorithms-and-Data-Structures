def get_seq(n):
    string = ''
    for i in range(1, n+1):
        string += str(i)
    return string


n = int(input())
i = 1
string = ''
while len(string) < n:
    string += get_seq(i)
    i += 1
print(string[n-1])
