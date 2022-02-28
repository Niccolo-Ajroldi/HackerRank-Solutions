# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:11:57 2022

@author: nicco
"""

v1 = [1,4,7]
v2 = [0,2,5,9,12]

def Merge(v1, v2):
    "v1, v2, sorted"
    i = 0; j = 0;
    v = []
    while i<len(v1) and j<len(v2):
        if v1[i] < v2[j]:
            v.append(v1[i])
            i+=1
        else:
            v.append(v2[j])
            j+=1
    if i<len(v1):
        v += v1[i:]
    if j<len(v2):
        v += v2[j:]
    return v
        
Merge(v1,v2)
Merge([],v2)
Merge([],[])
Merge([1],[2])

def MergeSort(v):
    
    n = len(v)
    
    if n<=1:
        return v
    
    v1 = v[:(n//2)]
    v2 = v[(n//2):]
    
    v1 = MergeSort(v1)
    v2 = MergeSort(v2)
    
    return Merge(v1, v2)
    
v = [42,3,8,5,1,0,4,7,23,2]
MergeSort(v)











