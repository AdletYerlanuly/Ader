n = dict()
with open('input.txt', 'r') as file:
    for line in file:
        for word in line.strip().split():
            n[word] = n.get(word, -1) + 1
            print(n[word], end=' ')
