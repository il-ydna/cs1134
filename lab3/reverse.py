def reverse_list(lst):
    length = len(lst)

    for i in range(length//2):
        temp = lst[i]
        lst[i] = lst[length-i-1]
        lst[length-i-1] = temp

    print(lst)


def reverse_list_precise(lst, low = None, high = None):
    length = high - low + 1

    for i in range(low, (high + 1)//2):
        temp = lst[i]
        lst[i] = lst[high - (i - low)]
        lst[high - (i - low)] = temp

    print(lst)


lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4, 5, 6]
reverse_list(lst1)
reverse_list_precise(lst2, 1, 3)
