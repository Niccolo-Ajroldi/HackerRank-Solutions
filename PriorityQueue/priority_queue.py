# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:09:50 2022

@author: nicco
"""

#------------------------------------------------------------------------------
# MAX HEAP

# import heapq as heapq
        
# class MaxHeap_tuple:
    
#     def __init__(self):
#         self.data = []

#     def top(self):
#         return -self.data[0]

#     def push(self, val):
#         heapq.heappush(self.data, -val)

#     def pop(self):
#         return -heapq.heappop(self.data)
    
#     def size(self):
#         return len(self.data)
    
#     def print(self):
#         [print(-d) for d in self.data]
        

import heapq as heapq
        
class MaxHeap_tuple:
    
    def __init__(self):
        self.data = []

    def top(self):
        tup = self.data[0]
        return (-tup[0], -tup[1])

    def push(self, val):
        tup = (-val[0], -val[1])
        heapq.heappush(self.data, tup)

    def pop(self):
        tup = heapq.heappop(self.data)
        return (-tup[0], -tup[1])
    
    def size(self):
        return len(self.data)
    
    def print(self):
        
        [print(d) for d in self.data]

#------------------------------------------------------------------------------
# PRIORITY QUEUE

class PriorityQueue:
    
    def __init__(self):
        self.maxheap = MaxHeap_tuple()
        self.order = 0
        
    def getfront(self):
        key = self.maxheap.top()
        return key[0]
    
    def dequeue(self):
        key = self.maxheap.pop()
        return key[0]
    
    def enqueue(self, el):
        key = (el, self.order)
        self.order += 1
        self.maxheap.push(key)
    
    def size(self):
        return self.maxheap.size()
    
    def print(self):
        self.maxheap.print()

#------------------------------------------------------------------------------
# PRIORITY QUEUE

pq = PriorityQueue()

pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(3)
pq.enqueue(4)



