# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:36:17 2022

@author: nicco
"""

px, py = list(map(int, input().split()))
fx, fy = list(map(int, input().split()))
nx, ny = list(map(int, input().split()))

grid = []
for _ in range(ny):
    grid.append(input())

0 0
1 2
3 3
.-%
-%P
---

#%%
px, py = [0, 0]
fx, fy = [1, 2]
nx, ny = [3, 3]
grid = ['.-%', '-%P', '---']

grid

def can_I_go_there(x,y,there,grid,nx,ny):
    if grid[x][y]=="%":
        print("I am in an invalid grid point")
        return
    # se sono sul lato nord
    if x==0 and there=="UP":
        return False
    # se sono sul lato sud
    if x==(nx-1) and there=="DOWN":
        return False
    # se sono sul lato ovest
    if y==0 and there=="LEFT":
        return False
    # se sono sul lato est
    if y==(nx-1) and there=="RIGHT":
        return False
    # altrimenti guardo la griglia
    if there=="UP":
        return (grid[x-1][y]!="%")
    if there=="DOWN":
        return (grid[x+1][y]!="%")
    if there=="LEFT":
        return (grid[x][y-1]!="%")
    if there=="RIGHT":
        return (grid[x][y+1]!="%")
    return 5

#%%

# lato nord
can_I_go_there(0,0,"RIGHT",grid,nx,ny)
can_I_go_there(0,0,"DOWN",grid,nx,ny)
can_I_go_there(0,0,"UP",grid,nx,ny)
can_I_go_there(0,0,"LEFT",grid,nx,ny)

# lato ovest
can_I_go_there(1,0,"LEFT",grid,nx,ny)
can_I_go_there(1,0,"RIGHT",grid,nx,ny)
can_I_go_there(1,0,"UP",grid,nx,ny)
can_I_go_there(1,0,"DOWN",grid,nx,ny)

# lato est
can_I_go_there(1,2,"LEFT",grid,nx,ny)
can_I_go_there(1,2,"RIGHT",grid,nx,ny)
can_I_go_there(1,2,"UP",grid,nx,ny)
can_I_go_there(1,2,"DOWN",grid,nx,ny)

# lato sud
can_I_go_there(2,2,"LEFT",grid,nx,ny)
can_I_go_there(2,2,"RIGHT",grid,nx,ny)
can_I_go_there(2,2,"UP",grid,nx,ny)
can_I_go_there(2,2,"DOWN",grid,nx,ny)

# invalid points
can_I_go_there(1,1,"LEFT",grid,nx,ny)
can_I_go_there(0,2,"LEFT",grid,nx,ny)

#%%

from collections import deque

# def dfs(nx, ny, px, py, fx, fy, grid):
    
#     visited = set()
#     stack = deque()
#     stack.append((px,py))
#     saved = []
    
#     while stack:
#         curr = stack.pop()
#         cx, cy = curr
#         if cx == fx and cy==fy:
#             saved.append(curr)
#             break
#         if not curr in visited:
#             saved.append(curr)
#             visited.add(curr)
#             # visit *valid* adjacent nodes
#             if can_I_go_there(cx,cy,"UP",grid,nx,ny):
#                 stack.append((cx-1,cy))
#             if can_I_go_there(cx,cy,"LEFT",grid,nx,ny):
#                 stack.append((cx,cy-1))
#             if can_I_go_there(cx,cy,"RIGHT",grid,nx,ny):
#                 stack.append((cx,cy+1))
#             if can_I_go_there(cx,cy,"DOWN",grid,nx,ny):
#                 stack.append((cx+1,cy))
    
#     print(len(saved))
#     for node in saved:
#         print(node[0], node[1], sep=" ")
        
        
def dfs(nx, ny, px, py, fx, fy, grid):
    
    visited = set()
    stack = deque()
    stack.append((px,py))
    explored = []
    path = []
    
    while stack:
        curr = stack.pop()
        cx, cy = curr
        if cx == fx and cy==fy:
            explored.append(curr)
            break
        if not curr in visited:
            visited.add(curr)
            explored.append(curr)
            # visit *valid* adjacent nodes
            if can_I_go_there(cx,cy,"UP",grid,nx,ny):
                stack.append((cx-1,cy))
            if can_I_go_there(cx,cy,"LEFT",grid,nx,ny):
                stack.append((cx,cy-1))
            if can_I_go_there(cx,cy,"RIGHT",grid,nx,ny):
                stack.append((cx,cy+1))
            if can_I_go_there(cx,cy,"DOWN",grid,nx,ny):
                stack.append((cx+1,cy))
    
    print(len(explored))
    for node in explored:
        print(node[0], node[1], sep=" ")
        
    # print(len(path)-1)
    # for node in path:
    #     print(node[0], node[1], sep=" ")

#%%
px, py = [1, 2]
fx, fy = [0, 0]
nx, ny = [3, 3]
grid = ['.-%', 
        '-%P', 
        '---']
dfs(nx, ny, px, py, fx, fy, grid)


#%%

px, py = [3, 9]
fx, fy = [5, 1]
nx, ny = [7, 20]

grid = [
"%%%%%%%%%%%%%%%%%%%%",
"%--------------%---%",
"%-%%-%%-%%-%%-%%-%-%",
"%--------P-------%-%",
"%%%%%%%%%%%%%%%%%%-%",
"%.-----------------%",
"%%%%%%%%%%%%%%%%%%%%"
]

dfs(nx, ny, px, py, fx, fy, grid)

#%%

32
3 9
3 10
3 11
3 12
3 13
3 14
3 15
3 16
2 16
1 16
1 17
1 18
2 18
3 18
4 18
5 18
5 17
5 16
5 15
5 14
5 13
5 12
5 11
5 10
5 9
5 8
5 7
5 6
5 5
5 4
5 3
5 2
