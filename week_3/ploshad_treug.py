a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
S = ((p - a) * (p - b) * (p - c) * p) ** (1/2)
print(S)
