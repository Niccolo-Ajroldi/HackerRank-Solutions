# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:27:33 2022

@author: nicco
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data) 
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        self.root = insert_rec(self.root, val)
        
def insert_rec(root, val):
    if root == None:
        root = Node(val)
        return root
    if root.data == val:
        return root
    if root.data > val:
        root.left = insert_rec(root.left, val)
    if root.data < val:
        root.right = insert_rec(root.right, val)
    return root

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
t = BST()
arr = [7,3,9,2,4,7]
for val in arr:
    t.insert(val)

preOrder(t.root)
#     7
#    / \
#   3   9
#  / \
# 2   4


#%% Depth-First Print

def DF_print(root):
    if root == None:
        return
    print(root.data)
    DF_print(root.left)
    DF_print(root.right)
    

from collections import deque

def iterative_DF_print(root):
    
    if not root:
        return
    stack = deque()
    stack.append(root)
    while stack:
        curr = stack.pop()
        if not curr:
            continue
        print(curr.data)
        stack.append(curr.right)
        stack.append(curr.left)
    
iterative_DF_print(t.root)


#%% Depth-First Search

def DFS(root, val):
    if root == None:
        return 0
    if root.data == val:
        return 1
    lft = DFS(root.left, val)
    rgt = DFS(root.right, val)
    return lft or rgt

DFS(t.root, 1)
DFS(t.root, 10)
DFS(t.root, 7)
DFS(t.root, 2)
DFS(t.root, 4)
DFS(t.root, 9)
DFS(t.root, 3)

#%% Depth-First Search Iterative

def iterative_DFS(root, val):
    if not root:
        return 0
    
    stack = deque()
    stack.append(root.data)
    while stack:
        curr = stack.pop()
        if not curr:
            continue
        if curr.data == val:
            return 1
        stack.append(curr.left)
        stack.append(curr.right)
        
DFS(t.root, 1)
DFS(t.root, 10)
DFS(t.root, 7)
DFS(t.root, 2)
DFS(t.root, 4)
DFS(t.root, 9)
DFS(t.root, 3)










