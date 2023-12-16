from ChainingHashTableMap import ChainingHashTableMap

def two_sum(lst, target):
    hash_table = ChainingHashTableMap()
    half_count = 0
    for i in range(0,len(lst)):
        hash_table[lst[i]] = target - lst[i]
        if lst[i] == target/2:
            half_count += 1

    if half_count >= 2:
        return int(target/2)

    for i in hash_table:
        print(i, hash_table[i])
        try:
            curr = hash_table[hash_table[i]]
            if curr != target/2:
                return curr
        except:
            continue



lst = [-2, 11, 15, 21, 20, 7]
print(two_sum(lst, 22))