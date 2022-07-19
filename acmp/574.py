def get_dict(string):
    dictionary = {}
    for letter in string:
        try:
            dictionary[letter] += 1
        except KeyError:
            dictionary[letter] = 1
    return dictionary


s1 = get_dict(input())
s2 = get_dict(input())
print("YES" if s1 == s2 else "NO")
