a = input()
first_word = a[:a.find(' ')]
second_word = a[a.find(' ') + 1:]
print(second_word + ' ' + first_word)
