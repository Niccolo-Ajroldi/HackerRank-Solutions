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
        self.MAX = sys.maxsize
        self.arr = [self.MAX] * maxsize

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
    
    # return root
    def root(self):
        return self.arr[0]
    
    
    def print_arr(self):
        print(self.arr)
        
    def print(self):
        depth = self.depth()
        # for each level of depth, print the nodes in that level
        for d in range(depth+1):
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
                
        # insert at the end
        self.arr[self.size] = el
                
        # increase size
        self.size += 1
        
        # swap parent and child
        current = self.size - 1
        while self.arr[current] < self.arr[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
    # get minimum element of the heap
    def getmin(self):
        
        if self.empty():
            print("Empty heap")
        
        # pop min
        popped = self.arr[0]
        
        # reduce size
        self.size -= 1
        
        # put another elemnet as root
        self.arr[0] = self.arr[self.size]
        self.arr[self.size] = self.MAX
        
        # call heapify to restore heap property
        self.heapify(0)

        return popped
    
    # heapify node in position i
    # hepify(i) controlla che i sia più piccolo dei suoi figli,
    # Se questo è il caso, la procedura fa scivolare l’elemento arr[i] lungo
    # un cammino dell’albero in modo da ristabilire la proprietà della heap.
    def heapify(self, i):
        
        # if the node i snot a leaf
        if not self.is_leaf(i):
            
            # if the node is greater than the left child:
            if self.arr[i] > self.arr[self.left_child(i)]:
                # swap with the left child and heapify the left child
                self.swap(i, self.left_child(i))
                self.heapify(self.left_child(i))
                
                
            # if the node is greater than the right child:
            elif self.arr[i] > self.arr[self.right_child(i)]:
                # swap with the right child and heapify the right child
                self.swap(i, self.right_child(i))
                self.heapify(self.right_child(i))
        
        
            # if (self.arr[i] > self.arr[self.left_child(i)] or
            #    self.arr[i] > self.arr[self.right_child(i)]):
 
            #     # Swap with the left child and heapify
            #     # the left child
            #     if self.arr[self.left_child(i)] < self.arr[self.right_child(i)]:
            #         self.swap(i, self.left_child(i))
            #         self.heapify(self.left_child(i))
 
            #     # Swap with the right child and heapify
            #     # the right child
            #     else:
            #         self.swap(i, self.right_child(i))
            #         self.heapify(self.right_child(i))
    
    
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

h.insert(4)    
h.print()

h.insert(3)    
h.print()

h.insert(1)    
h.print()

h.insert(8)    
h.print()

h.insert(0)    
h.print()

h.insert(9)
h.print()

h.print()
h.depth()
h.size

h.getmin()
h.print()


