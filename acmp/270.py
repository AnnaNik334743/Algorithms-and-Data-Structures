from re import fullmatch as f, sub as b

s = input()
n = ""
if f(r"[a-z]+(_[a-z]+)*", s):
  n = b(r"_([a-z])", lambda m: m.group(1).upper(), s)
elif f(r"[a-z]+([A-Z][a-z]*)+", s):
  n = b(r"([A-Z])", lambda m: '_' + m.group(1).lower(), s)
print(n if len(n) else "Error!")
