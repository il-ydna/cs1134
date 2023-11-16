from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(sublist1, sublist2, res_lst):
        if len(sublist1) == 0 and len(sublist2) == 0:
            pass
        elif len(sublist2) == 0:
            for n in sublist1:
                res_lst.add_last(n)
        elif len(sublist1) == 0:
            for n in sublist2:
                res_lst.add_last(n)
        else:
            if sublist1.header.next.data <= sublist2.header.next.data:
                next_node = sublist1.delete_first()
            elif sublist1.header.next.data > sublist2.header.next.data:
                next_node = sublist2.delete_first()
            res_lst.add_last(next_node)
            merge_sublists(sublist1, sublist2, res_lst)
            return res_lst
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, DoublyLinkedList())

sll1 = DoublyLinkedList()
sll1.add_last(1)
sll1.add_last(3)
sll1.add_last(5)
sll1.add_last(6)
sll1.add_last(8)
sll2 = DoublyLinkedList()
sll2.add_last(2)
sll2.add_last(3)
sll2.add_last(5)
sll2.add_last(10)
sll2.add_last(15)
sll2.add_last(18)
print(merge_linked_lists(sll1, sll2))