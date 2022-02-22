# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:41:02 2022

@author: nicco
"""

from collections import deque
    
class myQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
    # O(1)
    def front(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
            
    # O(n) at WORST
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()       
    # O(1)
    def enqueue(self, newval):
        self.s1.append(newval)

queue = myQueue()

q = int(input())
for j in range(q):
    temp = list(map(int, input().split()))
    if temp[0]==1:
        queue.enqueue(temp[1])
    elif temp[0]==2:
        queue.dequeue()
    elif temp[0]==3:
        print(queue.front())
        
