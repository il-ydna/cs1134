from DoublyLinkedList import DoublyLinkedList
class Integer:
    def __init__(self, num_str):
        self.num_list = DoublyLinkedList()
        self.num_length = len(num_str)
        for i in range(self.num_length):
            self.num_list.add_last(int(num_str[i]))

    def __add__(self, other):
        res_int = Integer("")
        self_curr = self.num_list.trailer.prev
        other_curr = other.num_list.trailer.prev
        carry_over = 0
        while self_curr is not self.num_list.header and other_curr is not other.num_list.header:
            temp_sum = self_curr.data + other_curr.data + carry_over
            ones_digit = temp_sum % 10
            carry_over = temp_sum // 10

            res_int.num_list.add_first(ones_digit)
            res_int.num_length += 1

            self_curr = self_curr.prev
            other_curr = other_curr.prev

        while self_curr is not self.num_list.header:
            res_int.num_list.add_first(self_curr.data + carry_over)
            res_int.num_length += 1
            self_curr = self_curr.prev
            carry_over = 0
        while other_curr is not other.num_list.header:
            res_int.num_list.add_first(other_curr.data + carry_over)
            res_int.num_length += 1
            other_curr = other_curr.prev
            carry_over = 0

        return res_int

    

    def __repr__(self):
        res_int = 0
        curr_node = self.num_list.trailer.prev
        for i in range(self.num_length):
            res_int += (10 ** i) * curr_node.data
            curr_node = curr_node.prev
        return str(res_int)

i1 = Integer("001234")
i2 = Integer("000034")
i3 = i1 + i2
print(i3)
#i3 = i1 * i2
#print(i3)