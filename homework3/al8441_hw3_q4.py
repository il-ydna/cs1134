# worst case is n^2 if every element in the lst is equal to value
def remove_all(lst, val):
    curr = 0
    val_count = 0
    first_val = 0
    for i in lst:
        if i == val:
            val_count += 1

    while len(lst) - first_val != val_count:
        while lst[curr] != val:
            curr += 1
        first_val = curr

        while lst[curr] == val and curr < len(lst)- 1:
            curr += 1
        first_non_val = curr

        lst[first_val], lst[first_non_val] = lst[first_non_val], lst[first_val]

        #print(lst)
        curr = first_val

    while lst[-1] == val:
        lst.pop(-1)
        #print(lst)
    return lst

list1 = [1, 2, 1, 3, 4, 5]
print(remove_all(list1, 1))

# worst case is linear. The function passes through the entire list once.
# it swaps elements in constant time to push all non-val elements to the front
# the swaps are constant time, and done a maximum of n times
# it then pops all elements that equal val off the end of the list
# pop is constant, and is done n times in the worst case
# thus, our worst case is linear
