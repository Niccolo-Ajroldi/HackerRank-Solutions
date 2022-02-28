# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:14:38 2022

@author: nicco
"""

import heapq as heapq

# MIN-HEAP --------------------------------------------------------------------

heap = []
heapq.heapify(heap)
heapq.heappush(heap,4)
heapq.heappush(heap,3)
heapq.heappush(heap,1)
heapq.heappush(heap,8)
heapq.heappush(heap,0)
heapq.heappush(heap,9)

heap

heapq.heappop(heap)
heap

# MAX-HEAP --------------------------------------------------------------------

heap = []
heapq._heapify_max(heap)

heapq.heappush(heap, 4)
heap

heapq.heappush(heap,3)
heap

# heapq DOES NOT SUPPORT maxheap push

# Solution:

class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def print(self):
        [print(-d) for d in self.data]

max_heap = MaxHeap()

max_heap.push(3)
max_heap.print()

max_heap.push(5)
max_heap.print()

max_heap.push(1)
max_heap.print()

max_heap.top()

max_heap.pop()
max_heap.print()

# MIN and MAX HEAPS -----------------------------------------------------------

class MinHeap:
    def __init__(self):
        self.data = []
        
    def top(self):
        return self.data[0]
    
    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)
    
    def print(self):
        [print(d) for d in self.data]
    
        
class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def print(self):
        [print(-d) for d in self.data]


min_heap = MinHeap()

min_heap.push(3)
min_heap.print()

min_heap.push(5)
min_heap.print()

min_heap.push(1)
min_heap.print()

min_heap.top()

min_heap.pop()
min_heap.print()













