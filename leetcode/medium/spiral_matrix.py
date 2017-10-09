""" Spiral Matrix - https://leetcode.com/problems/spiral-matrix

    Given a matrix of m x n elements (m rows, n columns), return all elements 
    of the matrix in spiral order.

    For example,
    Given the following matrix:

    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        spiral = []
        row = 0
        col = -1
        row_limit = len(matrix)
        col_limit = len(matrix[0])
        counter = 0
        while row_limit > 0 and col_limit > 0:
            # right
            for i in range(col_limit):
                col += 1
                spiral.append(matrix[row][col])

            row_limit -= 1
            if row_limit == 0 or col_limit == 0: break
            # down
            for i in range(row_limit):
                row += 1
                spiral.append(matrix[row][col])

            col_limit -= 1
            if row_limit == 0 or col_limit == 0: break
            # left
            for i in range(col_limit):
                col -= 1
                spiral.append(matrix[row][col])

            row_limit -= 1
            if row_limit == 0 or col_limit == 0: break
            # up
            for i in range(row_limit):
                row -= 1
                spiral.append(matrix[row][col])
            col_limit -= 1
        return spiral


# a = Solution()
# a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# a.spiralOrder([])