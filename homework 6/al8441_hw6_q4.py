from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    res_lst = DoublyLinkedList()
    for val in lnk_lst:
        res_lst.add_last(val)
    return res_lst

def deep_copy_linked_list(lnk_lst):
    def dcll_helper(l_lst, res_lst):
        if isinstance(l_lst, int):
            return l_lst
        else:   # l_lst.next.data is another linked list
            dcll_helper(l_lst.data, res_lst)



lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)
lnk_lst2 = deep_copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
