""" Add Binary - https://leetcode.com/problems/add-binary/


    Given two binary strings, return their sum (also a binary string).

    For example,
    a = "11"
    b = "1"
    Return "100"

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = (len(a)-1,len(b)-1)
        add = []
        carry = 0

        # while both binary strings are not empty, perform binary addition
        while i >= 0 and j >= 0:
            z = int(a[i]) + int(b[j]) + carry
            if z == 1:
                add.append(str(z))              # 1 + 0 = 1, carry = 0
                carry = 0
            elif z == 2:                        # 1 + 1 = 0, carry = 1
                add.append("0")
                carry = 1
            elif z == 3:
                add.append("1")                 # 1 + 1 + 1 = 1, carry = 1
                carry = 1
            else:
                add.append("0")                 # 0 + 0 = 0, carry = 0
                carry = 0
            i -= 1
            j -= 1
        
        # executes when string a is greater than string b
        while i >= 0:
            z = int(a[i]) + carry
            if z == 1:
                add.append("1")
                carry = 0
            elif z == 2:
                add.append("0")
                carry = 1
            else:
                add.append("0")
                carry = 0
            i -= 1
        
        # executes when string b is greater than string a
        while j >= 0:
            z = int(b[j]) + carry
            if z == 1:
                add.append("1")
                carry = 0
            elif z == 2:
                add.append("0")
                carry = 1
            else:
                add.append("0")
                carry = 0
            j -= 1
        
        # if carry is left, include it
        if carry:
            add.append(str(carry))
        return ''.join(add[::-1])

a = Solution()
print(a.addBinary("11", "1"))