def find_pivot(lst):
    mid = len(lst)//2
    low = 0
    high = len(lst) - 1
    last_val = lst[len(lst) - 1]
    while low < high:
        if lst[mid] < lst[mid-1]:
            return mid
        if lst[low] < lst[mid]:
            low = mid
        if lst[low] > lst[mid]:
            high = mid
        mid = (low + high)//2
    return mid

def shift_binary_search(lst, target):
    pivot = find_pivot(lst)
    print(pivot)
    if lst[0] <= target <= lst[pivot-1]:
        low = 0
        high = pivot-1
    else:
        low = pivot
        high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        print(low, mid, high)
        if target == lst[mid]:
            return mid
        if target < lst[mid]:
            high = mid - 1
        if target > lst[mid]:
            low = mid + 1



lst = [3, 4, 1, 2]
print(find_pivot(lst))
print(shift_binary_search(lst, 4))


