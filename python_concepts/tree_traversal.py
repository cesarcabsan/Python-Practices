class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data), '', end='')
        inOrder(root.right)

def preOrder(root):
    if root:
        print(str(root.data), '', end='')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.data), '', end='')

root = Node(20)
root.left = Node(15)
root.right = Node(3)
root.left.left = Node(16)
root.left.right = Node(4)
print('Inorder traversal: ')
inOrder(root)

print('\nPreorder traversal: ')
preOrder(root)

print('\nPostorder traversal: ')
postOrder(root)