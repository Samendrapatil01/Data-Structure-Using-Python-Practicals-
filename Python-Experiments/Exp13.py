# Experiment 13: Binary Tree and Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Preorder: Root, Left, Right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Inorder: Left, Root, Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Postorder: Left, Right, Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print("Preorder traversal:")
preorder(root)

print("\nInorder traversal:")
inorder(root)

print("\nPostorder traversal:")
postorder(root)
print()
