x = [int(n) for n in input().split()]
for n in range(1, len(x)):
    if x[n] > x[n - 1]:
        print(x[n], end=' ')
