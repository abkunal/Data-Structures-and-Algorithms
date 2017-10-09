""" Rotate Image - https://leetcode.com/problems/rotate-image/

    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:
    You have to rotate the image in-place, which means you have to modify the input 
    2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:

    Given input matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotate4(x, y, n, matrix):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n+x-y][x]
            matrix[n+x-y][x] = matrix[n][n+x-y]
            matrix[n][n+x-y] = matrix[y][n]
            matrix[y][n] = temp

        
        x = 0
        n = len(matrix) - 1
        while x < n:
            y = x
            for i in range(n-x):
                rotate4(x,y,n, matrix)
                y += 1
            x += 1
            n -= 1
           

# a = Solution()
# a.rotate([[1,2,3],[4,5,6],[7,8,9]])
# a.rotate([[1,2],[3,4]])
# a.rotate([[1]])
# x = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
# d = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],
#     [31,32,33,34,35,36]]