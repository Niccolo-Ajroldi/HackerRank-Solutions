# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:08:25 2022

@author: nicco
"""

#%% Bucketize

import math
v = [12,4,23,2,5,14,31]

def BucketSort(v, k):
    # determine the maximum of v -> O(n)
    M = max(v)
    bck_size = math.floor(M/k)
    buckets = [[] for _ in range(k)]
    for x in v:
        idx = math.floor(x/bck_size)
        idx = min(idx, k-1)
        buckets[idx].append(x)
        
    print(buckets)
    
k = 5
BucketSort(v, k) 


#%% Insertion Sort

def InsertionSort(arr, val):
    "arr should be sorted or empty"
    
    arr.append(val)
    n = len(arr)
        
    if n==1:
        return
    
    # check if val is less then arr[0]
    # loop from end-1 to start
    for i in range(n-2,-1,-1):
        if arr[i] > val:
            arr[i+1] = arr[i] # shift up arr[i]
        else:
            arr[i+1] = val
            return
    arr[0] = val
        
    return 

arr = [1,2,4,5,8]
InsertionSort(arr, 3)
arr
InsertionSort(arr, 0)
arr

#%% Bucketize + Insertion Sort
    
def BucketSort(v, k):
    # determine the maximum of v -> O(n)
    M = max(v)
    bck_size = math.floor(M/k)
    buckets = [[] for _ in range(k)]
    for x in v:
        idx = math.floor(x/bck_size)
        idx = min(idx, k-1)
        InsertionSort(buckets[idx], x)
        
    out = []
    for b in buckets:
        out += b
    return out
    
BucketSort(v, k)
    
#%% Versione migliorata

v = [12,4,23,2,5,14,31]

def BucketSort(v, k):
    if len(v)==0:
        return []
    
    # determine the maximum of v -> O(n)
    M = max(v)
    
    sz = M//k + 1
    buckets = [[] for _ in range(k)]
    for x in v:
        idx = x//sz
        buckets[idx].append(x)
        
    return buckets
    
k = 3
BucketSort(v, k) 

#%% Recursive Bucket Sort

def BucketSort(v, k):
    
    if len(v)<=1:
        return v
    
    # determine the maximum of v -> O(n)
    M = max(v)
    
    sz = M//k + 1
    buckets = [[] for _ in range(k)]
    for x in v:
        idx = x//sz
        buckets[idx].append(x)
        
    for i in range(len(buckets)):
        buckets[i] = BucketSort(buckets[i], k+1)
    
    out = []
    for b in buckets:
        out += b
    return out
    
v = [12,4,23,2,5,14,31]
print(BucketSort(v, 3))



