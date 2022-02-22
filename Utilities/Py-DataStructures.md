# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:17:26 2022

@author: nicco
"""
https://wiki.python.org/moin/TimeComplexity

#s = set(map(int, input().split()))

# list, dictionaries: mutable
# string, tuple: not mutable

#------------------------------------------------------------------------------
# set (Hash set)

# lookup, insert, delete: O(1)
# but if hash table load factor is high -> collisions, O(n)

.add()
.update(an_iterable_obj) # O(|an_iterable_obj|)
.discard()
s.union(t) # O(|s|+|t|) 
s.intersection(t) # O(min(|s|,|t|))
s.difference(t) # O(|s|)
s.symmetric_difference(t)
.pop() # pops a randdom element
k in s # O(1)

#------------------------------------------------------------------------------
# useful functions 

sorted() # returns a list, O(n log n) both on average and in the worst case


#------------------------------------------------------------------------------
# tuple: immutable, random access

a = tuple()
a = (1,2)

#------------------------------------------------------------------------------
# list: mutable, random access

.insert(i,x): insert x at index i
.remove(x) : Delete the first occurrence of x
.append(x) O(1)
.sort()
.pop(): Pop the last element
.reverse()
.copy()
del my_list[2] # delete item at index 2

#------------------------------------------------------------------------------
# dictionary (Hash Table)

maintain insertion order

.get(idx)
.pop(idx)
.clear()
.copy()
.items() # returns pairs key-value

del dict[idx]

# sort by key
dict(sorted(dic.items()))

d = {"a": 1, "b": 2}  # becomes {'a': 1, 'b': 3}

#------------------------------------------------------------------------------
# DEQUE

should have:
.pop_front()
.push_front()
.pop_back()
.push_back()
.front()
.rear()

from collections import deque
dq = deque(['name','age','DOB']) 

.append()     # O(1)
.appendleft() # O(1)
.pop()        # O(1)
.popleft()    # O(1)

.clear()
.copy()

dq[0]  : access first  element O(1) (equivalent to front)
dq[-1] : access last   element O(1) (equivalent to rear)
dq[idx]: access other  element O(n)

#------------------------------------------------------------------------------
# STACK: LIFO

use collections.deque with:

dq.append()
dq.pop()
dq[-1]

#------------------------------------------------------------------------------
# QUEUES: FIFO

use collections.deque with:
.appendleft()
.pop()

#------------------------------------------------------------------------------
# QUEUES: FIFO

should have:
.pop()
.push()
.front()
.rear()

Queues may be implemented using list, BUT insert or delete an item at the front would cost O(N)
python queue.Queue does not implement front and back methods
In case they are needed, just use a dque from collections.deque

from queue import Queue 

q = Queue(maxsize = 3)
q = Queue([1,2,3])
print(q)

type(q.queue)

.put() # O(1)
.get() # O(1) (equivalent of pop)

.size()
.empty()
.full()
.deque() return a collections.deque object




















