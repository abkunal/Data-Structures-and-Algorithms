""" Maximum Product Subarray - 
    https://leetcode.com/problems/maximum-product-subarray/

    Find the contiguous subarray within an array (containing at least one number) 
    which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_product(arr, start, end):
            if arr == [] or start == len(arr): 
                return 0
            product = arr[start]
            
            for i in range(start+1, end):
                product *= arr[i]
            return product

        def find_max_product(arr):
            ''' find the maximum product subarray 
                Approach -
                1. First find whether number of negatives in the array is odd or even
                2. If no. of negatives are even, take product of the whole array
                3. else, take the product of subarray skipping the first and last negative number
            '''
            if arr == []: 
                return 0
            negatives = 0
            pos = []
            product = 1
            
            for i in range(len(arr)):
                if arr[i] < 0:
                    negatives += 1
                    if len(pos) < 2:
                        pos.append(i)
                    else:
                        pos[-1] = i
                product *= arr[i]
            
            if len(arr) == 1 and negatives == 1:
                return arr[0]
            
            if negatives % 2 == 0:
                return product
            return max(find_product(arr, 0, pos[-1]), find_product(arr, pos[0]+1, len(arr)))

        zero_pos = []
        max_product = 0

        # first find whether there are any zeroes in the array or not
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_pos.append(i)

        # if there are no zeroes, find the maximum product subarray of the whole array
        if len(zero_pos) == 0:
            return find_max_product(nums)
        
        # if there is only one zero, find maximum product of subarrays divided by 0
        if len(zero_pos) == 1:
            max_product = max(find_max_product(nums[:zero_pos[0]]), find_max_product(nums[zero_pos[0]+1:]))
        else:
            # otherwise find the maximum product of subarrays sandwiched between
            # two occurences of zeroes
            for i in range(len(zero_pos)):
                if i == 0:
                    x = find_max_product(nums[:zero_pos[i]])
                else:
                    x = find_max_product(nums[zero_pos[i-1]+1:zero_pos[i]])
                if x > max_product:
                    max_product = x
            x = find_max_product(nums[zero_pos[-1]+1:])
            if x > max_product:
                max_product = x

        # if maximum product is less than zero then return 0 as 0 > negatives
        if max_product < 0:
            return 0
        return max_product


# a = Solution()
# print(a.maxProduct([2,3,-2,4]))