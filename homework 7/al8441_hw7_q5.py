from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_expr_str):
    expr_lst = prefix_expr_str.split(" ")
    #print(expr_lst)
    res_tree = LinkedBinaryTree()
    def create_helper(pref_expr, start_pos):
        if start_pos == len(expr_lst):
            return ''
        if pref_expr[start_pos].isdigit():
            #print(pref_expr[start_pos], start_pos)
            return LinkedBinaryTree.Node(int(pref_expr[start_pos])), start_pos
        else:
            #print(pref_expr[start_pos], start_pos)
            new_node = LinkedBinaryTree.Node(pref_expr[start_pos])
            left = create_helper(pref_expr, start_pos+1)
            right = create_helper(pref_expr, left[1] + 1)
            new_node.left = left[0]
            new_node.right = right[0]
            return new_node, max(left[1], right[1])

    res_tree.root = create_helper(expr_lst, 0)[0]
    res_tree.size = len(expr_lst)
    #print(res_tree.size)
    return res_tree


tr = create_expression_tree('* 2 + - 15 6 4')

def prefix_to_postfix(prefix_exp_str):
    pref_tree = create_expression_tree(prefix_exp_str)
    def pref_to_post_helper(root):
        if root == None:
            return
        else:
            res_lst = []
            yield from pref_to_post_helper(root.left)
            yield from pref_to_post_helper(root.right)
            yield root.data
    return " ".join([str(elem) for elem in pref_to_post_helper(pref_tree.root)])

print(prefix_to_postfix('* 2 + - 15 6 4'))