n = int(input())
if n == 1:
    print(n, 'korova')
elif 2 <= n <= 4:
    print(n, 'korovy')
elif n % 10 == 1:
    if n // 10 == 1:
        print(n, 'korov')
    else:
        print(n, 'korova')
elif 2 <= (n % 10) <= 4:
    if n // 10 == 1:
        print(n, 'korov')
    else:
        print(n, 'korovy')
else:
    print(n, 'korov')
