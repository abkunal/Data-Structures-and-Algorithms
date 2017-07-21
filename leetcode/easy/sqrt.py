""" Sqrt(x) - https://leetcode.com/problems/sqrtx/

    Implement int sqrt(int x).
    Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def function(x, n):
            """ Square root function f(x) = x^2 - n """
            return x**2 - n

        def newton_raphson(x1, fx1, f1):
            """ newton raphson formula -> x2 = x1 - fx1 / f1  
                here f1 is derivative of fx1
            """
            return x1 - f1/fx1

        # trivial cases
        if x == 0 or x == 1:
            return x

        # finding initial approximation for newton raphson method
        root = x // 2
        while root ** 2 > x:
            root = root // 2

        # performing six iterations of newton raphson method
        for i in range(6):
            f1 = function(root, x)
            root = newton_raphson(root, f1, 2*root)
        
        return int(root)

    def mySqrt2(self, x):
        """ Alternative method using newton integer division method """
        root = x
        while root**2 > x:
            root = (root + x // root) / 2
        return root

        
a = Solution()