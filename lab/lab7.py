def sort_lst(lst):
    for i in range(len(lst)):
        print(lst)
        temp1 = lst[i]
        temp2 = lst[lst[i]]
        lst[lst[i]] = temp1
        lst[i] = temp2
    return lst


lst1 = [0, 3, 1, 2]
sort_lst(lst1)
print(lst1)


def intersection_of_lst(lst1, lst2):
    ind1 = 0
    ind2 = 0
    res = []
    shortest = len(lst1)
    if len(lst2) < len(lst1):
        shortest = len(lst2)
    for i in range(shortest):
        if lst1[ind1] == lst2[ind2]:
            res.append(lst1[ind1])
            ind1+=1
            ind2+=1
        elif lst1[ind1] > lst2[ind2]:
            ind2+=1
        else:
            ind1+=1
    return res


lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8,9,10]
print(intersection_of_lst(lst1, lst2))


def is_pow_of_two(n):
    if n == 1:
        return True
    else:
        bool1 = is_pow_of_two(n//2)
        bool2 = False
        if n%2 == 0:
            bool2 = True
        return bool1 and bool2


print(is_pow_of_two(128))


def split_parity(lst,low,high):
    if low == high:
        return
    if lst[low]%2 == 1 and lst[high]%2 == 0:
        lst[low], lst[high] = lst[high], lst[low]
        split_parity(lst, low+1, high-1)
    elif lst[low]%2 == 0:
        split_parity(lst, low+1, high)
    elif lst[low]%2 == 1:
        split_parity(lst, low, high-1)
    else:
        split_parity(lst, low+1, high-1)

lst1 = [1,2,3,4,5,6,7,8]
split_parity(lst1, 0, len(lst1)-1)
print(lst1)


def nested_sum(lst):
    if isinstance(lst,int):
        return lst
    elif len(lst) == 1:
        return nested_sum(lst[0])
    else:
        return nested_sum(lst[0]) + nested_sum(lst[1:])


lst = [ [1, 2], 3, [4, [5, 6, [7], 8 ] ] ]
print(nested_sum(lst))