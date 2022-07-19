n = input()
string = ''
for i in range(1, int(n)+1):
    string += str(i)
print(string.find(n) + 1)
