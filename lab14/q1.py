from ChainingHashTableMap import ChainingHashTableMap
from UnsortedArrayMap import UnsortedArrayMap

def most_frequent(lst):
    int_table = ChainingHashTableMap()

    for i in range(0, len(lst)):
        if lst[i] not in int_table:
            int_table[lst[i]] = 0
        int_table[lst[i]] += 1
    max = 0
    for i in int_table:
        curr = int_table[i]
        if curr > max:
            max = curr
    return max

def first_unique(lst):
    int_table = ChainingHashTableMap()

    for i in range(0, len(lst)):
        if lst[i] not in int_table:
            int_table[lst[i]] = 0
        int_table[lst[i]] += 1
    min = float('inf')
    res = None
    for i in lst:
        if int_table[i] == 1:
            return i
    return None


lst = [5,9,2,9,0,5,9,7]
print(most_frequent(lst))
print(first_unique(lst))