""" Spiral Matrix II - https://leetcode.com/problems/spiral-matrix-ii/

    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,

    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for j in range(n)] for i in range(n)]
        row = 0
        col = -1
        count = 1
        bounds = n
        while count <= n*n:
            # right
            for i in range(bounds):
                col += 1
                matrix[row][col] = count
                count += 1
            
            bounds -= 1
            
            # down
            for i in range(bounds):
                row += 1
                matrix[row][col] = count
                count += 1

            # left
            for i in range(bounds):
                col -= 1
                matrix[row][col] = count
                count += 1

            bounds -= 1
            # up
            for i in range(bounds):
                row -= 1
                matrix[row][col] = count
                count += 1
        return matrix


# a = Solution()
# a.generateMatrix(3)