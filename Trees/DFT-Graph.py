# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:48:44 2022

@author: nicco
"""

q = 2

# number of nodes
n = 4 

# number of edges
m = 2

adj_input = [[3,1], [2, 3]]

# list of sets
# adj[i] = nodes adjacent to node i
adj = [set() for _ in range(n)]
adj

for lis in adj_input:
    v1 = lis[0]-1
    v2 = lis[1]-1
    adj[v1].add(v2)
    adj[v2].add(v1)

adj


from collections import deque

def DFS(adj, s):
    
    n = len(adj)
    visited = set()
    
    reach = [float('inf')]*n
    
    stack = deque()
    stack.append((adj[0],0))
    
    while stack:
        popped = stack.pop()
        curr = popped[0]
        r = popped[1]
        if not curr in visited:
            reach[curr] = min(r, reach[curr])
            visited.add(curr)
            for node in adj[curr]:
                stack.append((node,r+1))
    del reach[s]
    # reach.pop(s)
    for i in range(len(reach)):
        if reach[i] == float('inf'):
            reach[i] = -1
    return reach
            
    
    
    
    
    









