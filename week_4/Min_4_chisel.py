a = int(input())
b = int(input())
c = int(input())
d = int(input())


def Min4(a, b, c, d):
    return min(min(min(a, b), c), d)


print(Min4(a, b, c, d))
