import random



rand_lst = [0] * 100

for i in range(1000):
    rand = random.randint(1, 100)
    rand_lst[rand-1] += 1

max_app = 0
max_app_val = 0
for i in range(len(rand_lst)):
    if rand_lst[i] > max_app:
        max_app = rand_lst[i]
        max_app_val = i + 1

min_app = 1001
min_app_val = 0
for i in range(len(rand_lst)):
    if rand_lst[i] < min_app:
        min_app = rand_lst[i]
        min_app_val = i + 1

lowest_val = 0
while rand_lst[lowest_val] == 0:
    lowest_val += 1
lowest_val += 1
highest_val = 99
while rand_lst[highest_val] == 0:
    lowest_val -= 1
highest_val += 1
# print(rand_lst)
# print(max_app_val)
# print(min_app_val)
# print(lowest_val)
# print(highest_val)

dict = {1:2, 3:4, 5:6}
for i in dict:
    # print(i)
    print(dict[i])