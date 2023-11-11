def shift(lst, key):
    length = len(lst)
    for i in range(0, key):
        temp = lst[i]
        lst[i] = lst[length - key + i]
        lst[length - key + i] = temp

    print(lst)


shift([1, 2, 3, 4, 5, 6], 4)