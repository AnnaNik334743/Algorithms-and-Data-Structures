LET, NUM = 'abcdefgh', '12345678'

iz, v = input().split()
x1, y1 = LET.find(iz[0]), NUM.find(iz[1])
x2, y2 = LET.find(v[0]), NUM.find(v[1])
if (x1 + y1) % 2 != (x2 + y2) % 2 or y2 <= y1:
    print("NO")
else:
    print("YES" if abs(x2-x1) <= abs(y2-y1) else "NO")
