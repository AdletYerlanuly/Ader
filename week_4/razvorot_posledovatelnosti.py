def Recurse():
    m = int(input())
    if m != 0:
        Recurse()
    print(m)
Recurse()
