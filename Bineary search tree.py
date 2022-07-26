class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+"->",end='')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node




    
root=None
root=insert(root,8)
root=insert(root,10)
root=insert(root,7)
print("Inorder traversal:",end='')
inorder(root)
