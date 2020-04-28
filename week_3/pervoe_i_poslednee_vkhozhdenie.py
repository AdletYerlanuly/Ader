a = input()
count = len(a) - len(a.replace('f', ''))
if count == 0:
    pass
elif count == 1:
    print(a.index('f'))
else:
    print(a.index('f'), a.rindex('f'))
