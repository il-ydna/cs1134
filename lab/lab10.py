from DoublyLinkedList import *


class LinkedStack:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self.dll) == 0

    def push(self, data):
        self.dll.add_last(data)

    def top(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.dll.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("List is empty")
        res = self.dll.trailer.prev.data
        self.dll.delete_last()
        return res


class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, data):
        self.data.add_last(data)
        if self.mid == None:
            self.mid = self.data.header.next
        elif len(self.data) % 2 == 1:
            self.mid = self.mid.next

    def top(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.data.trailer.prev

    def pop(self):
        if self.is_empty():
            raise Exception("List is empty")
        res = self.data.trailer.prev.data
        self.data.delete_last()
        if len(self.data) % 2 == 1:
            self.mid = self.mid.prev
        return res

    def mid_push(self, elem):
        if self.is_empty():
            raise Exception("List is empty")
        mid_node = self.mid
        self.data.add_after(mid_node, elem)
        if len(self.data) % 2 == 1:
            self.mid = self.mid.next


def reverse_dll_by_data(dll):
    front_curr = dll.header
    back_curr = dll.trailer
    for i in range(len(dll)//2):
        front_data = front_curr.next.data
        back_data = back_curr.prev.data
        front_curr.next.data = back_data
        back_curr.prev.data = front_data

        front_curr = front_curr.next
        back_curr = back_curr.prev


def reverse_dll_by_node(dll):
    curr = dll.header.next
    for i in range(len(dll)):
        curr_next = curr.next
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr_next
    dll.header.next, dll.trailer.prev = dll.trailer.prev, dll.header.next
    dll.header.next.prev = dll.header
    dll.trailer.prev.next = dll.trailer
    dll.header.prev = None
    dll.trailer.next = None

    #dll.header, dll.trailer = dll.trailer, dll.header

# ls = LinkedStack()
# ls.push(1)
# ls.push(2)
# ls.push(3)
# print(ls.pop())
# print(ls.pop())
# print(ls.pop())

# ms = MidStack()
# ms.push(1)
# ms.push(2)
# ms.push(3)
# ms.push(4)
# ms.push(5)
# ms.push(6)
# ms.push(7)
# ms.mid_push(100)
# #ms.mid_push(200)
# #ms.mid_push(300)
# while not ms.is_empty():
#     print(ms.pop())

# dll = DoublyLinkedList()
# dll.add_last(1)
# dll.add_last(2)
# dll.add_last(3)
# dll.add_last(4)
# dll.add_last(5)
# print(dll)
# reverse_dll_by_node(dll)
# print(dll)
#
dll = DoublyLinkedList()
dll.add_last(1)
dll.add_last(2)
dll.add_last(3)
#print(dll)
reverse_dll_by_node(dll)
print(dll)
