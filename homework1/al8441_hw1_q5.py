def fibs(n):
    first = 0
    second = 1
    for i in range(n):
        temp = first + second
        first = second
        second = temp
        yield first




# for curr in fibs(8):
#     print(curr)
