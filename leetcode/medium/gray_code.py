""" Gray Code - 

    The gray code is a binary numeral system where two successive values 
    differ in only one bit.

    Given a non-negative integer n representing the total number of bits in 
    the code, print the sequence of gray code. A gray code sequence must begin with 0.

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
    Note:
    For a given n, a gray code sequence is not uniquely defined.

    For example, [0,2,3,1] is also a valid gray code sequence according to the 
    above definition.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        def gray(code, counter, target):
            if counter == target:
                return code
            rcode = code[::-1]
            for i in range(len(code)):
                code[i] = "0" + code[i]
            for i in range(len(rcode)):
                rcode[i] = "1" + rcode[i]
            return gray(code + rcode, counter + 1, target)
        code = gray(["0", "1"], 1, n)
        intCode = [int(c, 2) for c in code]
        return(intCode)

    def grayCode2(self, n):
        """ An amazing more efficient solution by a fellow coder """
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results


# a = Solution()
# a.grayCode(3)