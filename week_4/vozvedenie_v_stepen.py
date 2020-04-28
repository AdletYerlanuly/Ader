def power(x, y):
    if y == 0:
        return 1
    res = power(x * x, y // 2)
    if y % 2:
        res *= x
    return res
x = float(input())
y = float(input())
print(power(x, y))
