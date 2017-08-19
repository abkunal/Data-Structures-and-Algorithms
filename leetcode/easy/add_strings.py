""" Add Strings - https://leetcode.com/problems/add-strings

    Given two non-negative integers num1 and num2 represented as string, 
    return the sum of num1 and num2.

    Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    
    You must not use any built-in BigInteger library or convert the inputs 
    to integer directly.
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            n1 = ord(num1[i]) % 48          # equivalent to -> int(num1[i])
            n2 = ord(num2[j]) % 48
            x = (n1+n2 + carry) % 10
            carry = (n1+n2 + carry) // 10
            
            res.append(str(x))
            i -= 1
            j -= 1
        
        while i >= 0:
            x = ((ord(num1[i])%48) + carry) % 10
            carry = ((ord(num1[i]) % 48) + carry) // 10
            res.append(str(x))
            i -= 1
            print(carry)
            
        while j >= 0:
            x = ((ord(num2[j]) % 48) + carry) % 10
            carry = ((ord(num2[j]) % 48) + carry) // 10
            res.append(str(x))
            j -= 1
            

        if carry:
            res.append(str(carry))
        return "".join(res[::-1])


a = Solution()
print(a.addStrings("9", "99"))