from BinarySearchTreeMap import BinarySearchTreeMap

def min_max_BST(bst):
    res_tup = (None, None)
    curr = bst.root
    while(curr.left is not None):
        curr = curr.left
    res_tup[0] = curr.item.key

    curr = bst.root
    while (curr.right is not None):
        curr = curr.right
    res_tup[1] = curr.item.key
    return res_tup


def glt_n(bst, n):
    if not bst.root:
        return -1

    current = bst.root
    greatest_less_than_n = -1

    while current:
        if current.item.value < n:
            greatest_less_than_n = current.item.key
            current = current.right
        else:
            current = current.left

    return greatest_less_than_n

bst_map = BinarySearchTreeMap()
bst_map[5] = "a"
bst_map[3] = "b"
bst_map[8] = "c"
bst_map[1] = "d"
bst_map[4] = "e"
bst_map[6] = "f"
bst_map[9] = "g"

def compare_bst(bst1, bst2):
    def get_values(bst):
        vals = []
        def get_vals_helper(root):
            if root is None:
                pass
            else:
                get_vals_helper(root.left)
                vals.append(root.item.key)
                get_vals_helper(root.right)
        get_vals_helper(bst.root)
        return vals

    bst1_vals = set(get_values(bst1))
    bst2_vals = set(get_values(bst2))
    return bst1_vals == bst2_vals and len(bst1_vals) == len(bst1_vals)

def is_BST(root):
    def is_BST_helper(root):
        if root is None:
            return None, None, True
        else:

            left_min, left_max, left_valid = is_BST_helper(root.left)
            right_min, right_max, right_valid = is_BST_helper(root.right)

            if left_valid and right_valid and (left_max is None or left_max < root.item.key) and (right_min is None or root.item.key < right_min):
                if left_min is not None:
                    curr_min = left_min
                else:
                    curr_min = root.item.key
                if right_max is not None:
                    curr_max = right_max
                else:
                    curr_max = root.item.key
                return curr_min, curr_max, True
            else:
                return None, None, False

    return is_BST_helper(root)[2]

print(is_BST(bst_map.root))

print(compare_bst(bst_map, bst_map))