from LinkedBinaryTree import LinkedBinaryTree





a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
bin_tree = LinkedBinaryTree(f)
print(bin_tree.bt_even_sum())
print(10 in bin_tree)

a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)

x = LinkedBinaryTree.Node(1)
y = LinkedBinaryTree.Node(2)
z = LinkedBinaryTree.Node(3, x, y)

fbt1 = LinkedBinaryTree(f)
fbt2 = LinkedBinaryTree(z)
print(fbt1.is_full())
print(fbt2.is_full())
