# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 19:44:39 2022

@author: nicco
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return(str(self.val))
    
class BST:
    def __init__(self):
        self.root = None
    def insert(self, val):
        self.root = self.rec_insert(self.root, val)
        return self.root
    def rec_insert(self, node, val):
        if node==None:
            node = Node(val)
        elif node.val == val:
            return node
        elif node.val > val:
            node.left = self.rec_insert(node.left, val)
        elif node.val < val:
            node.right = self.rec_insert(node.right, val)
        return node

# initialize a BST
tree = BST()
arr = [4,3,2,1,5]
#     4
#    / \
#   3   5
#  / \
# 1   2

for t in arr:
    tree.insert(t)


def preOrder(root):
    if root == None:
        return
    print (root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
preOrder(tree.root) # 4 3 2 1 5

#%% Breadth-First Traversal


#%% Print in ordine crescente
# O(N) + O()

from ordered_set import OrderedSet

def visit_and_order(root, my_set):
    if root == None:
        return
    my_set.add(root.val)
    preOrder(root.left)
    preOrder(root.right)

ordered_set = {}
type(ordered_set)

visit_and_order(tree.root, ordered_set)

ordered_set


type({})

a= {2,3,1}
type(a)        
a


a = {10:"c" ,3:"a", 1:"b"}
a
type(a)        




