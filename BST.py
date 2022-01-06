class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
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
arr = [4, 2, 1, 3, 7, 6]

for t in arr:
    tree.insert(t)

preOrder(tree.root)
