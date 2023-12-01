from LinkedBinaryTree import LinkedBinaryTree

tree = LinkedBinaryTree
tree.root = LinkedBinaryTree.Node(1)
tree.root.left = LinkedBinaryTree.Node(2)
tree.root.right = LinkedBinaryTree.Node(3)
tree.size = 3
def min_and_max(tree):
    if tree.root is None:
        raise Exception()

    def min_helper(root):
        if root is None:
            return float('inf')
        res = root.data
        left = min_helper(root.left)
        right = min_helper(root.right)
        if left < res:
            res = left
        if right < res:
            res = right
        return res

    def max_helper(root):
        if root is None:
            return float('-inf')
        res = root.data
        left = max_helper(root.left)
        right = max_helper(root.right)
        if left > res:
            res = left
        if right > res:
            res = right
        return res
    minimum = min_helper(tree.root)
    maximum = max_helper(tree.root)
    min_and_max = minimum, maximum
    return min_and_max