from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):

    def isBalanced(root):
        if root is None:
            return 0, True
        else:
            left_height, left_bal = isBalanced(root.left)
            if not left_bal:
                return 0, False
            right_height, right_bal = isBalanced(root.right)
            if not right_bal:
                return 0, False
            curr_height = max(left_height, right_height) + 1
            curr_balance = abs(left_height - right_height) <= 1
            return curr_height, curr_balance and left_bal and right_bal

    return isBalanced(bin_tree.root)[1]
