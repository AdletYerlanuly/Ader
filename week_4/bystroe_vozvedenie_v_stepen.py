def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 != 0:
        return a * power(a, b - 1)
    elif b % 2 == 0:
        return power(a * a, b / 2)
a = float(input())
b = float(input())
print(power(a, b))
