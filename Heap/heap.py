# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:56:26 2022

@author: nicco
"""

#%%
#------------------------------------------------------------------------------
# LIBRARIES

import math 
import sys


#%%
#------------------------------------------------------------------------------
# BASE CLASS

class Heap:
    
    # constructor
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.depth = 0
        self.arr = [sys.maxsize] * maxsize

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
    
    # returns True if the i-th node is a leaf node
    def is_leaf(self, i):
        return i > 2*self.depth
    
    # return root
    def root(self):
        return self.arr[0]
    
    
    def print_arr(self):
        print(self.arr)
        
    def print(self):
        # for each level of depth, print the nodes in that level
        for d in range(self.depth+1):
            print([self.arr[i] for i in range(2**d-1, 2**(d+1)-1)], sep=" ")
    
#------------------------------------------------------------------------------
# CHILD CLASS
        
class MinHeap(Heap):
    
    # constructor
    def __init__(self, maxsize):
        # inherit all the methods and properties from the parent class
        Heap.__init__(self, maxsize)

    # swap two nodes
    def swap(self, i,j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def insert(self, el):
                
        if self.full():
            print("Error: full heap")
            return
        
        # increase size
        self.size += 1
        
        # if necessary, increase depth
        self.depth = math.floor(math.sqrt(self.size))
        
        # insert at the end
        self.arr[self.size] = el
        
        # swap parent and child
        current = self.size
        while self.arr[current] < self.arr[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
    
    # heapify node in position i
    # hepify(i) controlla che i sia più piccolo dei suoi figli,
    # Se questo è il caso, la procedura fa scivolare l’elemento arr[i] lungo
    # un cammino dell’albero in modo da ristabilire la proprietà della heap.
    def min_heapify(self, i):
        
        # if the node i snot a leaf
        if not self.is_leaf(i):
            
            # if the node is greater than the left child:
            if self.arr[i] > self.arr[self.left_child(i)]:
                # swap with the left child and heapify the left child
                self.swap(i, self.left_child(i))
                self.min_heapify(self.left_child(i))
                
                
            # if the node is greater than the right child:
            elif self.arr[i] > self.arr[self.right_child(i)]:
                # swap with the right child and heapify the right child
                self.swap(i, self.right_child(i))
                self.min_heapify(self.right_child(i))
    
    # check the heap property
    def check_heap_property(self):
        
        if self.empty():
            return True
        
        # if there is only one element, return True
        elif self.size==1:
            return True
        
        # otherwise check nodes
        else:
            
            # initialize flag
            flag = True
            
            # loop over nodes
            for i in range(1, self.size):
                
                # if node[i] has a leftchild
                if self.left_child(i) <= self.size:
                    
                    # if left child is greater than node[i]
                    if self.arr[self.left_child(i)] < self.arr[i]:
                        flag = False
                        break
                
                # if node[i] has a rightchild
                if self.right_child(i) >= self.size:
                    
                    # if right child is smaller than node[i]
                    if self.arr[self.left_child(i)] > self.arr[i]:
                        flag = False
                        break
            
            # return
            if flag:
                return True
            else:
                return False
            
                    
#%%         
#------------------------------------------------------------------------------
# MAIN

h = MinHeap(10)

h.empty()
h.print_arr()
h.print()

h.insert(el=2)    
h.size
h.arr

h.insert(3)
h.size
h.arr

h.insert(1)
h.size
h.arr

h.insert(8)
h.size
h.arr

h.insert(0)
h.size
h.arr

h.print()

