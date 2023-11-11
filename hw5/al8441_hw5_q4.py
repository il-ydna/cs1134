from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.data_arr = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.data_arr) + len(self.stack2)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        self.data_arr.push(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.stack2.is_empty():
            for i in range(len(self.data_arr)):
                self.stack2.push(self.data_arr.pop())
        return self.stack2.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.stack2.is_empty():
            for i in range(len(self.data_arr)):
                self.stack2.push(self.data_arr.pop())
        return self.stack2.top()


q = Queue()
q.enqueue(1)
print(q.first())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.dequeue())
# q.enqueue(4)
# # print(q.dequeue())
# # print(q.dequeue())
# print(q.first())
