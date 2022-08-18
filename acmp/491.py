s = input()
print("NO SOLUTION" if len(set(s)) == 1 else s[1:] if s == s[::-1] else s)
