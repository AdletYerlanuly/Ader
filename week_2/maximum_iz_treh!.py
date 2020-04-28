a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    if b <= c:
        print(c)
    elif c <= b:
        print(b)
elif b <= a and b <= c:
    if c <= a:
        print(a)
    elif a <= c:
        print(c)
elif c <= a and c <= b:
    if a <= b:
        print(b)
    elif b <= a:
        print(a)
