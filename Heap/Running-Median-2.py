# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:08:52 2022

@author: nicco
"""

exec(open(r"D:\Coding\HackerRank-Solutions\Heap\myHeaps.py").read())
  
# input
v_in = [12, 4, 5, 3, 8, 7]
#v_in = [10,1,2,3,4,5,6,7,8,9,10]
print(v_in)

# initialize heaps
# minheap contains elements bigger than median
maxh = MaxHeap()
# maxhep contains elements smaller than median
minh = MinHeap()

#
median = None

for el in v_in:
    
    if not median:
        maxh.push(el)
        median = el
        
    else:
        
        # insert el in one heap
        if el < median:
            print("inserting %d in maxheap" %el)
            maxh.push(el)
        else:
            print("inserting %d in minheap" %el)
            minh.push(el)
                
        # restore balancing balancing between heaps
        if maxh.size() - minh.size() > 1:
            print("moving %d to minheap" %maxh.top())
            minh.push(maxh.pop())
        elif minh.size() - maxh.size() > 1:
            print("moving %d to maxheap" %minh.top())
            maxh.push(minh.pop())
        # if el==3:
        #     break
        
        if maxh.size() == minh.size():
            median = (minh.top() + maxh.top())/2
        elif maxh.size() == minh.size() + 1:
            median = maxh.top()
        elif minh.size() == maxh.size() + 1:
            median = minh.top()
        
    print(float(median))
    




