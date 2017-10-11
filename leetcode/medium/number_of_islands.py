""" Number of Islands - https://leetcode.com/problems/number-of-islands

    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands 
    horizontally or vertically. You may assume all four edges of the grid are all 
    surrounded by water.

    Example 1:

    11110
    11010
    11000
    00000
    Answer: 1

    Example 2:

    11000
    11000
    00100
    00011
    Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row, col, grid,seen):
            for i,j in [(1,0),(0,-1),(-1,0),(0,1)]:
                row_valid = 0 <= row + i < len(grid)
                col_valid = 0 <= col + j < len(grid[0])
                if row_valid and col_valid and grid[row+i][col+j] == '1' and (row+i,col+j) not in seen:
                    seen.add((row+i,col+j))
                    dfs(row + i, col + j, grid,seen)
        
        seen = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    seen.add((i,j))
                    islands += 1
                    dfs(i,j,grid, seen)
        return islands