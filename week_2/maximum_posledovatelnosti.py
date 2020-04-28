m = int(input())
maxM = m
while m != 0:
    m = int(input())
    if m == 0:
        break
    if m > maxM:
        maxM = m
print(maxM)
