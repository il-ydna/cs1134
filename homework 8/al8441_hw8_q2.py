from BinarySearchTreeMap import BinarySearchTreeMap
def create_chain_bst(n):
    res_tree = BinarySearchTreeMap()
    for i in range(1, n+1):
        res_tree.insert(i, i)
    return res_tree

t = create_chain_bst(4)
print(t.root.item.key)
print(t.root.right.item.key)
print(t.root.right.right.item.key)
print(t.root.right.right.right.item.key)

def add_items(bst, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    bst.insert(mid, mid)
    add_items(bst, low, mid - 1)
    add_items(bst, mid + 1, high)
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst
