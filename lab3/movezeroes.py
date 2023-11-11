def move_zeroes(nums):
    nonzero_count = 0
    length = len(nums)
    for i in range(length):
        if nums[i] != 0:
            nums[nonzero_count] = nums[i]
            nonzero_count+=1
    for i in range(nonzero_count, length):
        nums[i] = 0
    print(nums)


lst1 = [1, 0, 2, 4, 0, 0, 3, 0, 0]
move_zeroes(lst1)
