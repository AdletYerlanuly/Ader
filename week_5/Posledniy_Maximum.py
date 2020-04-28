spisok = list(map(int, input().split()))
x = spisok[0]
y = 0
for n, m in enumerate(spisok):
    if m >= x:
        y = n
        x = m
print(x, y)
