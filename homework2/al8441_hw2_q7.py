def findChange(lst01):
    not_found = True
    curr = len(lst01)//2
    while not_found:
        if lst01[curr] == 0 and lst01[curr+1] == 1:
            not_found = False
            return curr + 1
        elif lst01[curr] == 0:
            curr = (curr + len(lst01))//2 - 1
        else:
            curr = curr//2 + 1


lst = [0, 0, 0, 1, 1, 1]
print(findChange(lst))
