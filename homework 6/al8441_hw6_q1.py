from DoublyLinkedList import DoublyLinkedList
class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        return self.data.delete_first()

    def first(self):
        return self.data.header.next.data

lq = LinkedQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
print(lq.first())
print(lq.dequeue())
print(lq.first())
print(lq.dequeue())
print(lq.first())
print(lq.dequeue())
