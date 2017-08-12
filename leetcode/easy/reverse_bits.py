""" Reverse Bits - https://leetcode.com/problems/reverse-bits/ 

    Reverse bits of a given 32 bits unsigned integer.

    For example, given input 43261596 (in binary - 00000010100101000001111010011100), 
    return 964176192 (represented in binary as 00111001011110000010100101000000).
"""


class Solution:
    def reverse_bits(self, n):
        """ Generic Style """
        l = [0 for i in range(32)]
        index = 31
        while n != 0:
            l[index] = n % 2
            n = n // 2
            index -= 1
        number = 0
        for i in range(len(l)):
            number += l[i] * (2**i)
        return number
    
    def reverse_bits2(self, n):
        """ Python Style """
        num = bin(n)[2:]
        num = str((32-len(num))*"0" + num)[::-1]
        return int(num, 2)


#a = Solution()
#print(a.reverse_bits2(20))
