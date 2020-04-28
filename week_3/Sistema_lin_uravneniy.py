a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
R = c * e
S = f * a
T = b * c
V = a * d
y = (R - S) / (T - V)
x = (e - b * y) / a
print(int(x), int(y))
