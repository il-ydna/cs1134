def find_duplicates(lst):
    tracking_list = [0] * len(lst)
    res = []
    for i in range(len(lst)):
        tracking_list[lst[i]-1] += 1
    for i in range(len(lst)):
        if tracking_list[i] > 1:
            res.append(i + 1)
    return res

# lst = [2, 4, 4, 2, 1]
# print(find_duplicates(lst))

# should be linear, even in worst case, since append is amortized into constant time
# adding values to tracking list is constant as well
# we have two constant operations running n times, which means the function is linear
