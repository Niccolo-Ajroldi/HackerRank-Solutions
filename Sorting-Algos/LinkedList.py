# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 21:23:44 2022

@author: nicco
"""

""""
Sì, però parallelamente vorrei aprire anche avanti anche il discorso RNN.
"""

#%% 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # O(1)
    def push_back(self, data):
        node = Node(data)
        self.head
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
        
    # O(1)
    def push_front(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        self.size += 1
    
    # O(1)
    def pop_front(self):
        if not self.head:
            return
        else:            
            top = self.head
            self.head = top.next
            self.size -= 1
            return top.data
    
    # O(n)
    def pop_back(self):
        
        if not self.head:
            return
        
        elif self.size==1:
            return self.pop_front()
            
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            back = curr.next
            curr.next = None
            self.tail = curr
            self.size -= 1
            return back.data
            
    # O(n)
    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

#%% 
            
l = LinkedList()
l.push_back(1)
l.print()
l.push_back(2)
l.print()
l.push_front(8)
l.print()

l.pop_back()
l.print()

l.push_back(4)
l.print()

l.pop_front()
l.print()

l.push_back(9)
l.print()

l.push_front(9)
l.print()

l.pop_front()
l.pop_back()
l.pop_back()
l.print()

l.pop_back()
l.print()

l.pop_back()
l.print()
