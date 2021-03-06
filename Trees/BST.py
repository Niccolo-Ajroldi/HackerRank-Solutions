class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None
    
    def insert(self, val):
        #Enter you code here.
        self.root = insert_node(self.root, val)
        return self.root
           
        
def insert_node(root, val):
    
        if root == None:
            root = Node(val)
            return root
        
        if root.info == val:
            return root
        
        if root.info > val:
            root.left = insert_node(root.left, val)
            
        elif root.info < val:
            root.right = insert_node(root.right, val)
        
        return root

# initialize a BST
tree = BinarySearchTree()
arr = [7,3,9,2,4]
#     7
#    / \
#   3   9
#  / \
# 2   4

for t in arr:
    tree.insert(t)

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
preOrder(tree.root) # 7 3 2 4 9

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)
    
inOrder(tree.root) # 2 3 4 7 9 

def Postorder(root):
    if root == None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.info, end=" ")
    
Postorder(tree.root) # 2 4 3 9 7

# (a) Inorder (Left, Root, Right) 
# (b) Preorder (Root, Left, Right)   
# (c) Postorder (Left, Right, Root) 

# %% Breadth-First or Level Order Traversal: 4 3 5 2 1








