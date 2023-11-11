def two_sum(srt_lst, target):
    left_curr = len(srt_lst)//2 - 1
    right_curr = len(srt_lst)//2
    not_found = True
    while not_found:
        total = srt_lst[left_curr] + srt_lst[right_curr]
        print(total)
        if total < target:
            right_curr += 1
        elif total > target:
            left_curr -= 1
        else:
            not_found = False
            return left_curr, right_curr


sorted_lst = [-2, 7, 11, 15, 20, 21]
print(two_sum(sorted_lst, 22))
