import ctypes  # provides low-level arrays
import math
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, collection = None):

        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

        if hasattr(collection, '__iter__'):
            for i in collection:
                self.append(i)

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def __getitem__(self, ind):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError('invalid index')
        if -len(self) <= ind < 0:
            return self.data_arr[self.n + ind]
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        printstring = '['
        counter = 0
        for i in self:
            counter += 1
            printstring += str(i)
            if counter != self.n:
                printstring += ", "
        printstring += ']'
        return printstring

    def __add__(self, other):
        result = ArrayList()
        for i in self:
            result.append(i)
        for j in other:
            result.append(j)
        return result

    def __iadd__(self, other):
        for i in other:
            self.append(i)
        return self

    def __mul__(self, other):
        result = ArrayList()
        for i in range(other):
            result += self
        return result

    def __rmul__(self, other):
        result = self * other
        return result

    def remove(self, val):
        curr = 0
        while(self[curr] != val):
            curr += 1
        for i in range (curr, self.n - 1):
            self[i], self[i+1] = self[i+1], self[i]
        self.n -= 1

    def remove_all(self, val):
        curr = 0
        val_count = 0
        first_val = 0
        first_non_val = 1
        finished = False
        for i in self:
            if i == val:
                val_count += 1

        while self.n - first_val != val_count:
            while self[curr] != val:
                curr += 1
            first_val = curr

            while self[curr] == val and curr < self.n - 1:
                curr += 1
            first_non_val = curr

            self[first_val], self[first_non_val] = self[first_non_val], self[first_val]

            print(self)
            curr = first_val

        self.n -= val_count

    def insert(self, index, val):
        if index > 11 or index < -12:
            raise IndexError
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        self.n += 1
        if index >= 0:
            stop_val = index
        else:
            stop_val = self.n + index

        for i in range(self.n-1, stop_val, -1):
            self[i] = self[i-1]
        self[stop_val] = val

    def pop(self):
        if self.n == 0:
            raise IndexError
        if self.capacity > self.n*4:
            self.resize(self.capacity//2)
        temp = self[self.n-1]
        self[self.n-1] = None
        self.n -= 1
        return temp




