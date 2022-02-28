# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:35:58 2022

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
    
    def size(self):
        return len(self.data)
    
    def print(self):
        [print(-d) for d in self.data]