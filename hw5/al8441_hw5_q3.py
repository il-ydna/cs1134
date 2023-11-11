from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def __len__(self):
        res = len(self.stack) + len(self.deque)
        return res

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.deque.enqueue_first(val)
        self.reorganize()

    def reorganize(self):
        while len(self.stack) > len(self.deque):
            self.deque.enqueue_last(self.stack.pop())
        while len(self.stack) < len(self.deque):
            self.stack.push(self.deque.dequeue_last())


    def top(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.deque.first()

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if not self.deque.is_empty():
            return self.deque.dequeue_first()
        else:
            return self.stack.pop()

    def mid_push(self, val):
        self.stack.push(val)
        self.reorganize()

midS = MidStack()
midS.push(1)
midS.push(2)
midS.push(3)
midS.push(4)
midS.push(5)
#midS.push(6)
midS.mid_push(1000)
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())