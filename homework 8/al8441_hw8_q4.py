def find_min_abs_difference(bst):
    def min_helper(node, prev_value, min_diff):
        if node is None:
            return
        min_helper(node.left, prev_value, min_diff)
        # Update minimum absolute difference
        if prev_value is not None:
            new_min_diff = min(min_diff, abs(node.value - prev_value))

        # Update previous value
        new_prev_value = node.value

        # Traverse right subtree
        min_helper(node.right, new_prev_value, new_min_diff)



    return min_helper(bst.root, None, float('inf'))[2]