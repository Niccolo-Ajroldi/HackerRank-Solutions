# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:12:10 2022

@author: nicco
"""

#%%
#------------------------------------------------------------------------------
# LIBRARIES

import math 
import sys
import numpy as np
from abc import ABC, abstractmethod

#%%
#------------------------------------------------------------------------------
# BASE CLASS

class Heap(ABC):
    
    # constructor
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
    
    # return boolean
    def empty(self):
        return (self.size==0)
        
    # return boolean
    def full(self):
        return (self.size==self.maxsize)      
    
    # return index of the parent node of the i-th node        
    def parent(self, i):
        if i==0:
            return 0
        else:
            return math.floor((i-1)/2)
    
    # return index of the left child of the i-th node       
    def left_child(self, i):
        return 2*i + 1
    
    # return index of the left child of the i-th node   
    def right_child(self, i):
        return 2*i + 2
    
    # return the depth of the tree
    def depth(self):
        if self.empty():
            return 0
        else:
            return math.floor(math.log(self.size, 2))
    
    # returns True if the i-th node is a leaf node
    def is_leaf(self, i):
        depth = self.depth()
        return i >= 2**depth - 1
        
    # swap two nodes
    def swap(self, i,j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    # compare two elements v1 and v2
    # return true if v1 SHOULD be under v2 in the heap tree
    # a MinHeap will return true if v1 > v2
    # a MaxHeap will return true if v1 < v2
    @abstractmethod
    def under(self, v1, v2):
        pass
    
    # heapify node in position i
    # hepify(i) controlla che i sia piu' piccolo dei suoi figli,
    # Se questo e' il caso, la procedura fa scivolare l’elemento arr[i] lungo
    # un cammino dell’albero in modo da ristabilire la proprietà della heap.
    def heapify(self, i):
        
        # if the node is not a leaf
        if not self.is_leaf(i):
            
            # if node[i] should be under its left child:
            if self.under(self.arr[i], self.arr[self.left_child(i)]):
                # swap with the left child and heapify the left child
                self.swap(i, self.left_child(i))
                self.heapify(self.left_child(i))
            
            # if node[i] should be under its right child:
            elif self.under(self.arr[i], self.arr[self.right_child(i)]):
                # swap with the right child and heapify the right child
                self.swap(i, self.right_child(i))
                self.heapify(self.right_child(i))     
            
            # if the node should be under one of its children
            # if the node is greater than one of its children
            if self.under(self.arr[i], self.arr[self.left_child(i)]) or \
                self.under(self.arr[i], self.arr[self.right_child(i)]):
                    
                    # if left child should be above right child, swap parent with left child and heapify
                    if not self.under(self.arr[self.left_child(i)], self.arr[self.right_child(i)]):
                        self.swap(i, self.left_child(i))
                        self.heapify(self.left_child(i))
                    # if right child should be above right child, swap parent with right child and heapify
                    else:
                        self.swap(i, self.right_child(i))
                        self.heapify(self.right_child(i))
    
    # insert
    def insert(self, el):
                
        if self.full():
            print("Error: full heap")
            return np.nan
                
        # insert at the end
        self.arr[self.size] = el
                
        # increase size
        self.size += 1
        
        # partendo dal'ultimo nodo
        current = self.size - 1
        # while the parent node should be under the current child node
        while self.under(self.arr[self.parent(current)], self.arr[current]):
            # swap parent and current child
            self.swap(current, self.parent(current))
            # update current
            current = self.parent(current)
            
            
    # get root element of the heap
    def pop_root(self):
        
        if self.empty():
            print("Empty heap")
            return
        
        # pop min
        popped = self.arr[0]
        
        # reduce size
        self.size -= 1
        
        # put another elemnet as root
        self.arr[0] = self.arr[self.size]
        self.arr[self.size] = self.VAL
        
        # call heapify to restore heap property
        self.heapify(0)

        return popped
    
    def get_root(self):
        if self.empty():
            print("Empty heap")
            return
        return self.arr[0]
    
    # print tree structure    
    def print(self):
        depth = self.depth()
        # for each level of depth, print the nodes in that level
        for d in range(depth+1):
            print([self.arr[i] for i in range(2**d-1, 2**(d+1)-1)], sep=" ")
    
#------------------------------------------------------------------------------
# CHILD CLASS

# Minheap --------------------------------------
class MinHeap(Heap):
    
    # constructor
    def __init__(self, maxsize):
        # inherit all the methods and properties from the parent class
        Heap.__init__(self, maxsize)
        self.VAL = sys.maxsize
        self.arr = [self.VAL] * maxsize

    # overriding abstract method
    # v1 should be under v2 if v1 > v2
    def under(self, v1, v2):
        return v1 > v2
    
    # pop minimum element of the heap
    def pop_min(self):        
        return self.pop_root()    
    
    # get minimum element of the heap
    def get_min(self):        
        return self.get_root()    
    

# Maxheap --------------------------------------
class MaxHeap(Heap):
    
    # constructor
    def __init__(self, maxsize):
        # inherit all the methods and properties from the parent class
        Heap.__init__(self, maxsize)
        self.VAL = -sys.maxsize
        self.arr = [self.VAL] * maxsize

    # overriding abstract method
    # v1 should be under v2 if v1 > v2
    def under(self, v1, v2):
        return v1 < v2
    
    # get minimum element of the heap
    def pop_max(self):        
        return self.pop_root()   
                             
    # get minimum element of the heap
    def get_max(self):        
        return self.get_root()    
    
    
    
    