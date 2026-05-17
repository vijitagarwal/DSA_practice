class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder(root):
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

#driver code
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)

print("preorder traversal: ")
print(preorder(root))

print("inorder traversal")
print(inorder(root))

print("postorder traversal")
print(postorder(root))