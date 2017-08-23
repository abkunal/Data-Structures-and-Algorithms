""" Island Perimeter - https://leetcode.com/problems/island-perimeter

    You are given a map in form of a two-dimensional integer grid where 1 
    represents land and 0 represents water. Grid cells are connected 
    horizontally/vertically (not diagonally). The grid is completely surrounded 
    by water, and there is exactly one island (i.e., one or more connected land cells). 
    The island doesn't have "lakes" (water inside that isn't connected to the water 
    around the island). One cell is a square with side length 1. 
    The grid is rectangular, width and height don't exceed 100. 

    Determine the perimeter of the island.

    Example:

    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Answer: 16
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count_neighbours(grid, x, y):
            c = 0
            # upper neighbours
            if x > 0:
                if grid[x-1][y] == 1:   
                    c += 1
            # lower neighbours
            if x < len(grid)-1:
                if grid[x+1][y] == 1:
                    c += 1
            # left neighbours
            if y > 0:
                if grid[x][y-1] == 1:
                    c += 1
            # right neighbours
            if y < len(grid[0])-1:
                if grid[x][y+1] == 1:
                    c += 1
            return c
                
            
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    nh = count_neighbours(grid, i, j)
                    if nh == 3:
                        peri += 1
                    elif nh == 2:
                        peri += 2
                    elif nh == 1:
                        peri += 3
                    elif nh == 0:
                        peri += 4
        return peri