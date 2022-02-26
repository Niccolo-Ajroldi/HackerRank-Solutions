# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:14:04 2022

@author: nicco
"""

matrix = [[True , False, True , False],
          [True , False, True , True ],
          [False, False, True , False],
          [False, False, False, True ],
          [True , False, True , False]
          ]
matrix
# sol=5

def mark_island(i, j, matrix, visited):
    
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    
    if (i,j) in visited:
        return
    
    visited.add((i,j))
    
    print(i,j)
    # if it is not a valid index
    if i<0 or i>n_rows-1 or j<0 or j>n_cols-1:
        return
    
    # if I am outside an island
    if not matrix[i][j]:
        return
    
    # mark as False
    matrix[i][j] = False
    
    # visit all the directions
    # UP
    mark_island(i-1, j, matrix, visited)
    # DOWN
    mark_island(i+1, j, matrix, visited)
    # LEFT
    mark_island(i, j-1, matrix, visited)
    # RIGHT
    mark_island(i, j+1, matrix, visited)
    
    
def count_islands(matrix):
    
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j]:
                count += 1
                visited = set()
                mark_island(i, j, matrix, visited)
    return count
    
count_islands(matrix)
    
