def split_parity(lst):
    left_curr = 0
    right_curr = len(lst)-1
    while left_curr < right_curr:
        if lst[left_curr] % 2 == 1:
            left_curr += 1
        elif lst[right_curr] % 2 == 0:
            right_curr -= 1
        else:
            temp = lst[left_curr]
            lst[left_curr] = lst[right_curr]
            lst[right_curr] = temp

    return lst


#sprint(split_parity([1, 2, 3, 4, 5, 6]))

