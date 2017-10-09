class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        numbers = list(range(1, n+1))
        perm = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            perm += str(numbers[index])
            numbers.remove(numbers[index])
        return perm


a = Solution()
print(a.getPermutation(5,33))