def is_palindrome(s):
    left_curr = 0
    right_curr = len(s) - 1
    palindrome = True
    while (palindrome is True) and (left_curr <= right_curr):
        if s[left_curr] != s[right_curr]:
            palindrome = False
        left_curr += 1
        right_curr -= 1
    return palindrome


print(is_palindrome('12321'))


def reverse_vowels(input_str):
    list_str = list(input_str)
    left_curr = 0
    right_curr = len(list_str) - 1
    vowels = "a e i o u"
    while left_curr <= right_curr:
        if list_str[left_curr] not in vowels:
            left_curr += 1
        else:
            if list_str[right_curr] not in vowels:
                right_curr -= 1
            else:
                temp = list_str[left_curr]
                list_str[left_curr] = list_str[right_curr]
                list_str[right_curr] = temp
                left_curr += 1
                right_curr -= 1
    return "".join(list_str)


print(reverse_vowels("hello"))


def max_sum_subarray(nums, k):
    subarray_length = len(nums)//k
    left_curr = 0
    right_curr = subarray_length-1
    running_sum = 0
    max_sum = 0
    for i in range(subarray_length):
        running_sum += nums[i]
        max_sum = running_sum
    for i in range(len(nums) - subarray_length):
        running_sum -= nums[i]
        running_sum += nums[i + subarray_length]
        if running_sum > max_sum:
            max_sum = running_sum
    return max_sum


print(max_sum_subarray([1, 12, -5, -6, 50, 3], 2))


def find_missing(lst):
    for num in range(len(lst) + 1):
        if num not in lst:
            return num

# worst case is n^2 (missing is the last val)


def find_missing_2(lst):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low+high)//2

        if lst[mid]-1 != lst[mid-1]:
            return lst[mid] - 1

        if lst[mid] == mid + 1:   # missing elem is ABOVE
            low = mid + 1
        elif lst[mid] == mid + 2:   # missing elem is BELOW
            high = mid - 1


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(find_missing_2(lst1))


def find_missing_unsorted(lst):
    comparison_list = [0] * (len(lst)+1)
    print(comparison_list)

    for i in range(len(lst)):
        comparison_list[lst[i]-1] = 1

    for i in range(len(comparison_list)):
        if comparison_list[i] == 0:
            return i + 1


lst2 = [8, 7, 6, 4, 3, 2, 5]
print(find_missing_unsorted(lst2))





