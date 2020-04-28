S, N = map(int, input().split())
V = sorted([int(input()) for _ in range(N)])
n = sum(V)
while n > S and N:
    n -= V.pop()
    N -= 1
print(N)
