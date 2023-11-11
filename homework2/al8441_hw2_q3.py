import math


def factors(num):
    first_half = []
    curr = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            first_half.append(i)
            curr += 1
            yield i

    for i in range(curr-1, -1, -1):
        if first_half[i]**2 == num:
            pass
        else:
            yield int(num / first_half[i])


for curr_factor in factors(100):
    print(curr_factor)

