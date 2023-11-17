from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    res_lst = DoublyLinkedList()
    for val in lnk_lst:
        res_lst.add_last(val)
    return res_lst

# def deep_copy_linked_list(lnk_lst):
#     res_lst = DoublyLinkedList()
#     for i in lnk_lst:
#         if isinstance(i, int):
#             res_lst.add_last(i)
#         else:
#             new_lst = DoublyLinkedList()
#             for j in i:
#                 new_lst.add_last(j)
#             res_lst.add_last(new_lst)
#     return res_lst

def deep_copy_linked_list(lnk_lst):
    print(lnk_lst)
    def deep_copy_helper(l_list, res_lst):
        if l_list.data is None:
            return
        else:
            new_lst = DoublyLinkedList()

            if isinstance(l_list.data, int):
                res_lst.add_last(l_list.data)
                print(res_lst)
            elif len(l_list.data) == 0:
                empty = DoublyLinkedList()
                res_lst.add_last(empty)
            else:
                res_lst.add_last(deep_copy_helper(l_list.data.header.next, new_lst))
            deep_copy_helper(l_list.next, res_lst)
            return res_lst
    node = lnk_lst.header.next
    res = deep_copy_helper(node, DoublyLinkedList())
    print(res)
    return res
