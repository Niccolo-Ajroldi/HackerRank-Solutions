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
    print (root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
preOrder(tree.root) # 7 3 2 4 9 

#%% Breadth-First Traversal

from collections import deque

def print_BFT_iterative(root):
    
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        if curr:
            print(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
            
print_BFT_iterative(tree.root)

#     7
#    / \
#   3   9
#  / \
# 2   4

def print_BFT_recursive(queue):
    
    if not queue:
        return
    curr = queue.popleft()
    if curr:
        print(curr.val)
        queue.append(curr.left)
        queue.append(curr.right)
        print_BFT_recursive(queue)
    
queue = deque()        
queue.append(tree.root)
print_BFT_recursive(queue)

#%% Breadth-First Search

from collections import deque

def search_BFT_iterative(root, el):
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        if curr:
            if curr.val==el:
                return True
            queue.append(curr.left)
            queue.append(curr.right)
    return False

search_BFT_iterative(tree.root, 7)
search_BFT_iterative(tree.root, 8)
search_BFT_iterative(tree.root, 3)
search_BFT_iterative(tree.root, 4)

def search_BFT_recursive(queue, el):
    if not queue:
        return
    curr = queue.popleft()
    if curr:
        if curr.val==el:
            return True
        queue.append(curr.left)
        queue.append(curr.right)
        return search_BFT_recursive(queue, el)
    else:
        return False

queue = deque(); queue.append(tree.root)
search_BFT_recursive(queue, 7)

queue.clear(); queue.append(tree.root)
search_BFT_recursive(queue, 8)

queue.clear(); queue.append(tree.root)
search_BFT_recursive(queue, 4)

#%% Print in ordine crescente
# O(N) + O()

from ordered_set import OrderedSet

def visit_and_order(root, my_set):
    if root == None:
        return
    my_set.add(root.val)
    preOrder(root.left)
    preOrder(root.right)

ordered_set = OrderedSet()
type(ordered_set)

ordered_set.add(1)
ordered_set.add(10)
ordered_set.add(3)
ordered_set

visit_and_order(tree.root, ordered_set)
ordered_set

print(ordered_set)
[print(a) for a in ordered_set]


type({})

a= {2,3,1}
type(a)        
a


a = {10:"c" ,3:"a", 1:"b"}
a
type(a)        




