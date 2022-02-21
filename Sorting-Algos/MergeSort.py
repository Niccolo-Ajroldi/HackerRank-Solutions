# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:15:23 2022

@author: nicco
"""

from collections import deque

def MergeSort(v):
    
    if len(v) == 1:
        return v
    
    # split the list
    lis = list(v)
    left  = deque(lis[:len(v)//2])
    right = deque(lis[len(v)//2:])
    
    # recursively sort both sublist
    left  = MergeSort(left)
    right = MergeSort(right)
    
    # merge the now-sorted sublists.
    return merge(left, right)
    

def merge(v1, v2):
    res = deque()
    while v1 or v2:
        if v1 and v2:
            if v1[0] < v2[0]:
                res.append(v1.popleft())
            else:
                res.append(v2.popleft())
        elif v1:
            res.append(v1.popleft())
        elif v2:
            res.append(v2.popleft())
    return res

v1 = deque([4,8])  
v2 = deque([1,2,7])  
v1
v2
merge(v1, v2)


v = deque([8,4,1,2,7]) 
MergeSort(v)


