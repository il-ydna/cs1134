import ctypes  # provides low-level arrays
from ArrayList import ArrayList


def make_array(n):
    return (n * ctypes.py_object)()


class MaxStack:
    def __init__(self):
        self.data = ArrayList()
        self.current_max = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if self.current_max == None or val > self.current_max:
            self.current_max = val
        res = val, self.current_max
        self.data.append(res)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1][0]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        tup = self.data.pop()
        return tup[0]

    def max(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1][1]


# mstack = MaxStack()
# mstack.push(1)
# mstack.push(5)
# mstack.push(3)
# print(mstack.max())
# print(mstack.pop())
# print(mstack.max())
# print(mstack.pop())
# print(mstack.max())
# print(mstack.pop())
# print(mstack.max())