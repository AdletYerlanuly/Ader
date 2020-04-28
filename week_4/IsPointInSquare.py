def IsPointInSquare(x, y):
    b = -1 <= x <= 1 and -1 <= y <= 1
    return b
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
