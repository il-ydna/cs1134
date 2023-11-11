def sum_to(n): #also known as triangle numbers
    for i in range(1, n+1):
        total = i * (i + 1)//2
    yield total


for i in sum_to(10):
    print(i, end=', ')
