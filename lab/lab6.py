def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n-1)

    return n + sum_to(n - 1) if n > 0 else 0

def product_evens(n):
    if n == 0:
        return 1
    else:
        return n * product_evens(n-2)


def find_max(list_in):

    def find_max_helper(low, high, lst):
        if low == high:
            return lst[low]
        else:
            if lst[low] > lst[high]:
                return find_max_helper(low, high-1, lst)
            else:
                return find_max_helper(low+1, high, lst)

    return find_max_helper(0, len(list_in)-1, list_in)


def is_palindrome(low, high, string):
    if low >= high:
        return True
    else:
        if string[low] == string[high]:
            return True and is_palindrome(low+1, high-1, string)
        else:
            return False


def binary_search(lst, low, high, val):
    if low == high:
        return low
    else:
        if lst[(low+high)//2] == val:
            return (low+high)//2
        elif lst[(low+high)//2] > val:
            high = (low + high) // 2
        else:
            low = (low + high) // 2
        return binary_search(lst, low, high, val)


def vc_count(word):
    vowels = "aeiouAEIOU"
    def vc_count_helper(word, low, high, vowel_count, cons_count):
        if low - 1 == high:
            return vowel_count, cons_count
        else:
            if word[low] in vowels:
                vowel_count += 1
            else:
                cons_count += 1
            return vc_count_helper(word, low + 1, high, vowel_count, cons_count)
    return vc_count_helper(word, 0, len(word)-1, 0, 0)


def vc_count_2(word, low, high):
    vowels = "aeiouAEIOU"
    if low == high:
        if word[low] in vowels:
            return 1, 0
        else:
            return 0, 1
    else:

        if word[low] in vowels:
            temp_tuple = vc_count_2(word, low + 1, high)
            return 1 + temp_tuple[0], 0 + temp_tuple[1]
        else:
            temp_tuple = vc_count_2(word, low + 1, high)
            return 0 + temp_tuple[0], 1 + temp_tuple[1]


print(sum_to(8))
print(product_evens(10))
print(find_max([1, 3, 4, 6, 2]))
print(is_palindrome(0, 6, "racecar"))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 0, 7, 7))
print(vc_count_2('NYUTandonEngineering', 0, 19))

