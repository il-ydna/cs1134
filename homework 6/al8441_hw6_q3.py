from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data_list = DoublyLinkedList()  # data in each node will be a tuple with char and count
        self.data_list.add_last((orig_str[0], 1))

        curr_node = self.data_list.header.next

        for i in range(1, len(orig_str)):
            if orig_str[i] == orig_str[i-1]:
                curr_node.data = (curr_node.data[0], curr_node.data[1] + 1)
            else:
                self.data_list.add_last((orig_str[i], 1))
                curr_node = curr_node.next

    def __add__(self, other):
        res_str = CompactString(" ")
        res_str.data_list = self.data_list

        self_last = self.data_list.trailer.prev
        other_first = other.data_list.header.next

        check = True

        for elem in other.data_list:
            if self_last.data[0] == other_first.data[0] and check:
                res_str.data_list.trailer.prev.data = (self_last.data[0], self_last.data[1] + other_first.data[1])
                check = False
            else:
                res_str.data_list.add_last(elem)
        return res_str

    def lex_val(self):
        lex_val = 0
        for tup in self.data_list:
            lex_val += ord(tup[0]) * tup[1]
        return lex_val
    def __lt__(self, other):
        self_lex_val = self.lex_val()
        other_lex_val = other.lex_val()
        return self_lex_val < other_lex_val

    def __le__(self, other):
        self_lex_val = self.lex_val()
        other_lex_val = other.lex_val()
        return self_lex_val <= other_lex_val

    def __gt__(self, other):
        self_lex_val = self.lex_val()
        other_lex_val = other.lex_val()
        return self_lex_val > other_lex_val

    def __gt__(self, other):
        self_lex_val = self.lex_val()
        other_lex_val = other.lex_val()
        return self_lex_val >= other_lex_val

    def __repr__(self):
        res_str = ""
        for tup in self.data_list:
            res_str += tup[0] * tup[1]
        return res_str

cs1 = CompactString("ab")
cs2 = CompactString("b")
print(cs1 <= cs2)
print(cs1 >= cs2)
print(cs1)
print(cs2)