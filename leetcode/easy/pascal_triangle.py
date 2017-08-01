""" Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/

    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # return empty list
        if numRows <= 0:
            return []

        # initialize the required array
        p = [[] for i in range(numRows)]

        # first value
        p[0].append(1)
        count = 2

        # generate pascal's triangle
        for i in range(1,numRows):
            l = 0
            for j in range(count):
                if j - 1 < 0:
                    p[i].append(1)
                elif j + 1 == count:
                    p[i].append(1)
                else:
                    p[i].append(p[i-1][j-1] + p[i-1][j])
            count += 1

        return p

#a = Solution()
#a.generate(5)