""" Pascal's Triangle II - https://leetcode.com/problems/pascals-triangle-ii/

    Given an index k, return the kth row of the Pascal's triangle.

    For example, given k = 3,
    Return [1,3,3,1].

    Note:
    Could you optimize your algorithm to use only O(k) extra space?
    
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # first row
        p = [1]
        count = 2

        # generate row with given index using O(k) extra space
        for i in range(1,rowIndex+1):
            l = 0
            a = []
            a.append(1)
            
            for j in range(1, count-1):
                a.append(p[j-1] + p[j])
            
            a.append(1)
            p = a
            count += 1

        return p

#a = Solution()
#print(a.getRow(0))