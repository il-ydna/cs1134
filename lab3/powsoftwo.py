def powers_of_two(n):
    for i in range(n):
        yield 2**i


pow_gen = powers_of_two(6)
# print(next(pow_gen))
# print(next(pow_gen))
# print(next(pow_gen))
# print(next(pow_gen))
# print(next(pow_gen))
# print(next(pow_gen))
# print(next(pow_gen))

