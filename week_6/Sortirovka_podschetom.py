def CS(list):
    sorted_List = [0] * 101
    for i in list:
        sorted_List[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sorted_List[i], end='')
list = [int(i) for i in input().split()]
CS(list)
