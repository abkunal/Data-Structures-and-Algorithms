""" Count and Say- https://leetcode.com/problems/count-and-say/

    The count-and-say sequence is the sequence of integers with the 
    first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.

    Example 1:
    
    Input: 1
    Output: "1"
    

    Example 2:

    Input: 4
    Output: "1211"

"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # generate the next value based on the current value passed
        def count(s):
            new = ""
            c = 1
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    c += 1
                else:
                    new += str(c) + str(s[i-1])
                    c = 1
            new += str(c) + str(s[-1])
            return new
        
        initial = "1"
        for i in range(1, n):
            initial = count(initial)
        return initial

a = Solution()