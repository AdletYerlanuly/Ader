n = int(input())
m = 2
s = 1
while m != n + 1:
    s += 1/(m ** 2)
    m += 1
print(s)
