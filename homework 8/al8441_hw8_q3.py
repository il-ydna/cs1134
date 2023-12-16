from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    def restore_bst_helper(prefix_lst):
        if not prefix_lst:
            return None
        else:
            root_value = prefix_lst[0]
            new_item = BinarySearchTreeMap.Item(root_value, root_value)
            root = BinarySearchTreeMap.Node(new_item)

            left_subtree = [val for val in prefix_lst[1:] if val < root_value]
            right_subtree = [val for val in prefix_lst[1:] if val > root_value]

            root.left = restore_bst_helper(left_subtree)
            root.right = restore_bst_helper(right_subtree)
            return root
    root = restore_bst_helper(prefix_lst)
    res_bst = BinarySearchTreeMap()
    res_bst.root = root
    res_bst.n = len(prefix_lst)
    return res_bst

res_bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
print(res_bst)
print(res_bst.root.item.key)
print(res_bst.root.left.item.key)
print(res_bst.root.left.left.item.key)
print(res_bst.root.left.left.left.item.key)