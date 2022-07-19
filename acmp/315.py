def main():
    string = input()
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k0 = 0
    place = -1
    for i, letter in enumerate(string):
        if letter == '0':
            k0 += 1
        curr = alphabet.find(letter)
        if curr == -1:
            return -1
        else:
            if curr > place:
                place = curr
    return 2 if k0 == len(string) else place + 1


print(main())
