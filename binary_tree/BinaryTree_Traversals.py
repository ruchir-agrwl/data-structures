class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        print("Binary Tree Object created.")

    def pre_order(self, node):
        if node is None:
            return
        print("Pre order traversal Node ->", node.data),
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print("In order traversal Node ->", node.data)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print("Post order traversal Node ->", node.data)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
bt = BinaryTree()
bt.pre_order(root)
bt.in_order(root)
bt.post_order(root)
