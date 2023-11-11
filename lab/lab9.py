from ArrayQueue import ArrayQueue
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.current_sum = None

    def __len__(self):
        return self.data.n

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, val):
        if not isinstance(val, int) and not isinstance(val, float):
            raise TypeError("not a valid value for queue")
        self.data.enqueue(val)

        if self.current_sum == None:
            self.current_sum = val
        else:
            self.current_sum += val

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        self.current_sum -= self.first
        self.dequeue()

    def first(self):
        self.first()

    def sum(self):
        return self.current_sum

    def mean(self):
        return self.current_sum / self.data.n

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def last_enqueue(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def first_dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first_enqueue(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            self.front_ind = (self.front_ind - 1) % self.capacity
            self.data_arr[self.front_ind] = elem
            self.n += 1

    def last_dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        back_ind = (self.n +self.front_ind - 1) % self.capacity
        value = self.data_arr[back_ind]
        self.data_arr[back_ind] = None
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + self.n) % self.capacity
        return self.data_arr[back_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0


def flatten_list_by_depth(lst):
    q = ArrayQueue()
    new_lst = []

    for i in range(len(lst)):
        q.enqueue(lst[i])

    while not q.is_empty():
        if isinstance(q.first(), int):
            new_lst.append(q.dequeue())
        else:
            for i in range(len(q.first())):
                q.enqueue(q.first()[i])
            q.dequeue()
    return new_lst

class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val): # constant
        self.data.enqueue(val)
    def pop(self): # worst case 2n (linear)
        temp_lst = []
        len = self.data.n
        for i in range(len):
            temp_lst.append(self.data.dequeue())
        res = temp_lst[-1]
        for i in range(len-1):
            self.data.enqueue(temp_lst[i])
        return res
    def top(self): # worst case 2n (linear)
        temp_lst = []
        len = self.data.n
        for i in range(len):
            temp_lst.append(self.data.dequeue())
        res = temp_lst[-1]
        for i in range(len):
            self.data.enqueue(temp_lst[i])
        return res

class QueueStack2:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val): # worst case 2n (linear)
        temp_lst = []
        len = self.data.n
        for i in range(len):
            temp_lst.append(self.data.dequeue())
        self.data.enqueue(val)
        for i in range(len):
            self.data.enqueue(temp_lst[i])
    def pop(self): #constant
        return self.data.dequeue()
    def top(self): #constant
        return self.data.first()

mqueue = MeanQueue()
mqueue.enqueue(1)
mqueue.enqueue(2)
mqueue.enqueue(3)
mqueue.enqueue(4)
print(mqueue.sum())
print(mqueue.mean())
print()
dqueue = ArrayDeque()
dqueue.first_enqueue(1)
dqueue.first_enqueue(2)
dqueue.first_enqueue(3)
dqueue.last_enqueue(10)
dqueue.last_enqueue(20)
dqueue.last_enqueue(30)
print()
print(dqueue.first_dequeue())
print(dqueue.first_dequeue())
print(dqueue.first_dequeue())
print(dqueue.first_dequeue())
print(dqueue.first_dequeue())
print(dqueue.first_dequeue())
dqueue.first_enqueue(1)
dqueue.first_enqueue(2)
dqueue.first_enqueue(3)
dqueue.last_enqueue(10)
dqueue.last_enqueue(20)
dqueue.last_enqueue(30)
print()
print(dqueue.last_dequeue())
print(dqueue.last_dequeue())
print(dqueue.last_dequeue())
print(dqueue.last_dequeue())
print(dqueue.last_dequeue())
print(dqueue.last_dequeue())
print()
lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth(lst)
print(new_lst)
print()
qstack = QueueStack()
qstack.push(1)
qstack.push(2)
qstack.push(3)
print(qstack.top())
print(qstack.pop())
print(qstack.pop())
print(qstack.pop())
print()
qstack2 = QueueStack2()
qstack.push(1)
qstack.push(2)
qstack.push(3)
print(qstack.top())
print(qstack.pop())
print(qstack.pop())
print(qstack.pop())