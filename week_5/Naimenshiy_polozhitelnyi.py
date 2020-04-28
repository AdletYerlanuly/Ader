m = list(input().split())
minimal = 1000
for n in range(len(m)):
    s = int(m[n])
    if (s < minimal)and(s > 0):
        minimal = s
print(minimal)
