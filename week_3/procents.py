Z = float(input())
Y = float(input())
X = float(input())
Shekel1 = 100 * Y + X
Shekel2 = int(Shekel1 * (100 + Z) / 100)
print(Shekel2 // 100, Shekel2 % 100)
