# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:47:49 2022

@author: nicco
"""

import heapq as heapq

def HeapSort(v):
    
    res = []
    
    heap = v
    heapq.heapify(heap)
    
    while v:
        res.append(heapq.heappop(heap))
    
    return res
        
v = [8,4,1,2,7]

HeapSort(v)
    
    
    