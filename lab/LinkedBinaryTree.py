from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None



    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def __contains__(self, item):
        def contains_helper(node):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                return node.data == item
            else:
                res = contains_helper(node.left) or contains_helper(node.right)
                return res or node.data == item

        return contains_helper(self.root)

    def bt_even_sum(self):
        def bt_sum_helper(node):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return node.data
            else:
                res = bt_sum_helper(node.left) + bt_sum_helper(node.right)
                return res + node.data

        return bt_sum_helper(self.root)

    def is_full(self):
        def is_full_helper(node):
            # print(node.data)
            if node == None:
                return True
            elif node.left is None and node.right is None:
                return True
            else:
                res = False
                if isinstance(node.left, LinkedBinaryTree.Node) and isinstance(node.right, LinkedBinaryTree.Node):
                    res = True
                return is_full_helper(node.left) and is_full_helper(node.right) and res
        return is_full_helper(self.root)

    def preorder_with_stack(self):
        stack = ArrayStack()
        stack.push(self.root)
        while not stack.is_empty():
            curr = stack.pop()
            print(curr.data)
            yield (curr.data)
            if curr.right is not None:
                stack.push(curr.right)
            if curr.left is not None:
                stack.push(curr.left)



    def count_nodes(self):
        def subtree_count(root):
            if(root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)





