def ReduceFraction(n, m):
    a1 = max(n, m)
    a2 = min(n, m)
    if a1 == a2 and a1 * a2 != 0:
        return 1, 1
    else:
        p = a1 % a2
        while p > 0:
            a1 = a2
            a2 = p
            p = a1 % a2
        return n // a2, m // a2
n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
