numbers = [int(s) for s in input().split()]
before = set()
for num in numbers:
    if num in before:
        print('YES')
    else:
        print('NO')
        before.add(num)
