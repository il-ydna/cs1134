num = 6


def sum_smaller(n):
    total = 0
    for i in range(1, n):
        total += i ** 2
    return total


print(sum_smaller(num))

print(sum([x**2 for x in range(1, num)]))


def sum_smaller_odd(n):
    total = 0
    for i in range(1, n):
        if i % 2 != 0:
            total += i ** 2
    return total


print(sum_smaller_odd(num))

print(sum([x**2 for x in range(1, num) if x % 2 != 0]))
