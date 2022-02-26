# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:36:08 2022

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

# starting node
s = 1

from collections import deque
import numpy as np

def BFT_ShortestReach(adj, s):
    
    visited = set()
    reach = [np.Inf for _ in range(len(adj))]
    reach[s] = 0
    queue = deque()
    queue.append((s,0))
    
    while queue:
        popped = queue.popleft()
        curr = popped[0]
        r    = popped[1]
        print("current node: " + str(curr))
        if not curr in visited:
            reach[curr] = min(reach[curr], r)
            for node in adj[curr]:
                queue.append((node,r+1))
            visited.add(curr)
            
    reach = np.where(np.isinf(reach), -1, reach)
    return reach

adj
s = 0
BFT_ShortestReach(adj, s)
    
#%%

def BFSShortestReach(adj,s):
    visited = set()
    reach = [np.Inf for _ in range(len(adj))]
    q = deque()
    q.append((s,0))
    while q:
        popped = q.popleft()
        node = popped[0]
        r = popped[1]
        if not node in visited:
            reach[node] = min(reach[node],(r)*6)
            for adj_node in adj[node]:
                q.append((adj_node,(r+1)))
            visited.add(node)
       
    reach.pop(s)
    # reach = [xx*6 for xx in reach]
    reach = np.where(np.isinf(reach), -1, reach).tolist()
    return reach
    
adj
s = 0
BFSShortestReach(adj, s)

#%%

def BFSShortestReach(adj,s):
    visited = set()
    reach = [float('inf') for _ in range(len(adj))]
    q = deque()
    q.append((s,0))
    while q:
        popped = q.popleft()
        node = popped[0]
        r = popped[1]
        if not node in visited:
            reach[node] = min(reach[node],(r)*6)
            for adj_node in adj[node]:
                q.append((adj_node,(r+1)))
            visited.add(node)
       
    del reach[s]
    # reach.pop(s)
    for i in range(len(reach)):
        if reach[i] == float('inf'):
            reach[i] = -1
    return reach

adj
s = 2-1
BFSShortestReach(adj, s)



