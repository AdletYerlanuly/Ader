x = int(input())
y = int(input())
z = int(input())
if x == y:
    if y == z:
        print('3')
    else:
        print('2')
elif y == z:
    if z == x:
        print('3')
    else:
        print('2')
elif z == x:
    if z == y:
        print('3')
    else:
        print('2')
else:
    print('0')
