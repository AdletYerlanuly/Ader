a = - 1
n = 0
m = 0
while a != 0:
    a = int(input())
    if a > n and a != 0:
        m = n
        n = a
    elif a > m and a != 0:
        m = a
print(m)
