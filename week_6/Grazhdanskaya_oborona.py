n = int(input())
r = map(int, input().split())
m = int(input())
s = list(map(int, input().split()))
for i in range(len(s)):
    s[i] = [i + 1, s[i]]
s.sort(key=lambda x: x[1])


def find_V(x):
    if(x < s[0][1]):
        return s[0][0]
    if(x > s[-1][1]):
        return s[-1][0]
    l = 0
    d = len(s) - 1
    while(d - l > 1):
        m = (d + l) >> 1
        if(s[m][1] < x):
            l = m
        else:
            d = m
    if(x - s[l][1] < s[d][1] - x):
        return s[l][0]
    else:
        return s[d][0]
print(*[find_V(v) for v in r])
