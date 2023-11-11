def shift(lst, key, dir = 'left'):
    if dir == 'right':
        for i in range(key):
            lst.insert(0, lst.pop())
        return lst
    else:
        for i in range(key):
            lst.append(lst.pop(0))
        return lst

