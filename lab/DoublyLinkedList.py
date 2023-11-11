class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.n += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        data = node.data
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.n -= 1
        node.disconnect()
        return data

    def delete_first(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " <--> ".join([str(elem) for elem in self]) + ']'

    def remove_all(self, elem):
        cursor = self.header.next
        while(cursor is self.trailer):
            if(cursor.data == elem):
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next

    def __getitem__(self, i):
        if i > self.n:
            raise IndexError()
        if i < self.n // 2:
            node = self.header
            for j in range(i+1):
                node = node.next
        else:
            node = self.trailer
            for k in range(self.n, i, -1):
                node = node.prev
        return node.data
# dll = DoublyLinkedList()
# dll.add_first(1)
# dll.add_last(3)
# dll.add_last(5)
# dll.add_after(dll.header.next, 2)
# dll.add_before(dll.trailer.prev, 4)
# dll.delete_node(dll.trailer.prev)
# dll.add_first(0)
# print(dll)
# print(dll[0])
# print(dll[1])
# print(dll[2])
# print(dll[3])
# print(dll[4])

#
# def mystery(dll):
#     if len(dll) >= 2:
#         node = dll.trailer.prev.prev
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#         node.next = None
#         node.prev = None
#         return node
#     else:
#         raise Exception("dll must have length of 2 of greater")
#
# print(mystery(dll))
# print(dll)