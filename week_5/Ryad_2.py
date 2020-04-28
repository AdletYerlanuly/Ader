x = int(input())
y = int(input())
if x < y:
    for n in range(x, y + 1):
        print(n, end=" ")
else:
    for n in range(x, y - 1, -1):
        print(n, end=" ")
