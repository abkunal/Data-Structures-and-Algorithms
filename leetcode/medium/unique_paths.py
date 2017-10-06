""" Unique Paths - https://leetcode.com/problems/unique-paths

    A robot is located at the top-left corner of a m x n grid 
    (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid 
    (marked 'Finish' in the diagram below).

    How many possible unique paths are there?

    Above is a 3 x 7 grid. How many possible unique paths are there?

    Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fact(m):
            x = 1
            while m > 1:
                x *= m
                m -= 1
            return x

        return (fact(m+n-2)) // (fact(m-1) * fact(n-1))

    def uniquePaths2(self, m, n):
        maze = [[1 for i in range(n)] for j in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    maze[row][col] = 1
                else:
                    maze[row][col] = maze[row-1][col] + maze[row][col-1]
        return maze[-1][-1]


# a = Solution()
# print(a.uniquePaths2(3,3))