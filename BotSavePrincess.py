# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 09:38:27 2022

@author: nicco
"""

def displayPathtoPrincess(n,grid):
    
    m_flag = False
    p_flag = False
    
    # cycle over the matrix to get the position of both the characters
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='m':
                m_pos = [i,j]
                m_flag = True
            if grid[i][j]=='p':
                p_pos = [i,j]
                p_flag = True
            if p_flag & m_flag:
                break
    
    delta_x = p_pos[0] - m_pos[0]
    delta_y = p_pos[1] - m_pos[1]
    
    if delta_x > 0:
        cmd_x = "DOWN"
    else:
        cmd_x = "UP"
    
    if delta_y > 0:
        cmd_y = "RIGHT"
    else:
        cmd_y = "LEFT"

    for _ in range(abs(delta_x)):
        print(cmd_x)
    for _ in range(abs(delta_y)):
        print(cmd_y)

"""
3
---
-m-
p--
"""

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input.strip()) # grid is a list of lists!

displayPathtoPrincess(m,grid)