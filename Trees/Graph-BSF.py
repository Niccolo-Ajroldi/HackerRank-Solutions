# Enter your code here. Read input from STDIN. Print output to STDOUT

q = int(input())

graphs = []
starts = []
nn = []
mm = []

for _ in range(q):
    n, m = list(map(int, input().split()))
    adj = [set() for _ in range(n)]
    nn.append(n)
    mm.append(m)
    for _ in range(m):
        lis = list(map(int, input().split()))
        v1 = lis[0]-1
        v2 = lis[1]-1
        adj[v1].add(v2)
        adj[v2].add(v1)
    s = int(input())
    graphs.append(adj)
    starts.append(s)

from collections import deque

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
    for i in range(len(reach)):
        if reach[i] == float('inf'):
            reach[i] = -1
    return reach
                
        
for i in range(q):
    adj = graphs[i]
    s = starts[i]
    #print(adj, s)
    res = BFSShortestReach(adj,s-1)
    print(*res)
