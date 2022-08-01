from math import pi, sin, cos


n, a = map(int, input().split())
R = a / (2 * sin(pi / n))
r = R * cos(pi / n)
print('YES' if abs(R - r) < 1 else 'NO')
