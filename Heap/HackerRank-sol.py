# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:40:09 2022

@author: nicco
"""

import heapq as heapq

class MinHeap:
    def __init__(self):
        self.data = []
        
    def top(self):
        return self.data[0]
    
    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)
    
    def size(self):
        return len(self.data)
        
        
class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def size(self):
        return len(self.data)
        

maxh = MaxHeap()
minh = MinHeap()
median = None

for el in arr:
    
    if not median:
        maxh.push(el)
        median = el
        
    else:
        
        # insert el in one heap
        if el < median:
            maxh.push(el)
        else:
            minh.push(el)
                
        # restore balancing balancing between heaps
        if maxh.size() - minh.size() > 1:
            minh.push(maxh.pop())
        elif minh.size() - maxh.size() > 1:
            maxh.push(minh.pop())
        
        if maxh.size() == minh.size():
            median = (minh.top() + maxh.top())/2
        elif maxh.size() == minh.size() + 1:
            median = maxh.top()
        elif minh.size() == maxh.size() + 1:
            median = minh.top()
        
    print(float(median))
    




