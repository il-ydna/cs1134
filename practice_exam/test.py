import copy
lst1 = [1,[2,3],[4,5],6]
lst2 = lst1
lst3 = lst1[:]
lst4 = copy.deepcopy(lst1)

lst1[0] = 10
lst1[1][1] = 30

print(lst1)
print(lst2)
print(lst3)
print(lst4)

def is_sorted(lst,low,high):
    if low == high:
        return True
    else:
        bool1 = is_sorted(lst, low+1, high)
        bool2 = False
        if lst[low] < lst[low+1]:
            bool2 = True

        return (bool1 and bool2)

lst1=[1,2,3,4,3,5]
print(is_sorted(lst1, 0, len(lst1)-1))