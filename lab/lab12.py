from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
tree = LinkedBinaryTree()
tree.root = LinkedBinaryTree.Node(1)
tree.root.left = LinkedBinaryTree.Node(2)
tree.root.left.left = LinkedBinaryTree.Node(3)
tree.root.left.right = LinkedBinaryTree.Node(4)
tree.root.right = LinkedBinaryTree.Node(5)
tree.root.right.left = LinkedBinaryTree.Node(6)
# tree.root.right.right = LinkedBinaryTree.Node(7)

tree.size = 6

# s = tree.preorder_with_stack()
# print([elem for elem in s])

def ip(tree):
    def find_tree_height(root):
        if root is None:
            return 0
        left = find_tree_height(root.left)
        right = find_tree_height(root.right)
        max_height = max(left, right)+1
        return max_height
    height = find_tree_height(tree.root)
    # print(height)
    def is_perfect(root,height,level=1):
        if root is None:
            return True
        if root.left is None and root.right is None:
            # print(level, height)
            return level == height

        if root.left is not None and root.right is not None:
            return (is_perfect(root.left, height, level + 1) and
                    is_perfect(root.right, height, level + 1))
        # print('hi')
        return False
    return is_perfect(tree.root, height)

print(ip(tree))


def is_perfect_iterative(root):
    q = ArrayQueue()
    q.enqueue(root)
    still_perfect = True
    current_level = 0
    while not q.is_empty():
        if len(q) != 2 ** current_level:
            still_perfect = False
        for i in range(2**current_level):
            # print(len(q), current_level)
            curr = q.dequeue()
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        current_level += 1
        # print(current_level)

    return still_perfect

def invert_bt(root):
    if root is None:
        return
    else:
        root.left, root.right = root.right, root.left
        invert_bt(root.left)
        invert_bt(root.right)

def invert_bt_iterative(root):
    q = ArrayQueue()
    while not q.is_empty():
        curr = q.dequeue()
        curr.left, curr.right = curr.right, curr.left
        if curr.left is not None:
            q.enqueue(curr.left)
        if curr.left is not None:
            q.enqueue(curr.right)

# invert_bt(tree.root)
print(is_perfect_iterative(tree.root))

def merge_bt(root1, root2):
    def merge_helper(root1, root2):
        if root1 is None and root2 is None:
            pass
        elif root1 is not None:
            return root1
        elif root2 is not None:
            return root2

        merged_root = LinkedBinaryTree.Node(root1.data + root2.data)
        if root1.left is not None and root2.left is not None:
            merged_root.left = merge_helper(root1.left, root2.left)
        if root1.right is not None and root2.right is not None:
            merged_root.right = merge_helper(root1.right, root2.right)

        return merged_root


