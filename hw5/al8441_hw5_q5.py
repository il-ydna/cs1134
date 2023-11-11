from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()

    counter = 0
    res_lst = []

    for i in range(len(lst)):
        stack.push(lst[i])

    queue.enqueue([stack.pop()])
    counter = 2

    for i in range(len(lst) - 1):
        new_val = stack.pop()
        for j in range(len(queue)):
            existing_elem = queue.first()
            for k in range(counter):
                new_elem = existing_elem[0:k] + [new_val] + existing_elem[k:]
                queue.enqueue(new_elem)
            print(queue.dequeue())
        counter += 1

    return [queue.dequeue() for i in range(len(queue))]


lst = [1, 2, 3, 4]
print(permutations(lst))
