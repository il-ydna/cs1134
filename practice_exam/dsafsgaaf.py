def partition(lst):
    pivot = lst[0]
    lower_count=1
    for i in range(1, len(lst)-1):
        if lst[i] < pivot:
            lst[i],lst[lower_count]=lst[lower_count],lst[i]
            lower_count+=1
        else:
            continue
    lst.insert(lower_count, pivot)

    res_lst = lst
    return res_lst

lst = [4,2,3,1,5]
print(partition(lst))