""" Next Permutation - https://leetcode.com/problems/next-permutation

    Implement next permutation, which rearranges numbers into the lexicographically 
    next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible 
    order (ie, sorted in ascending order).

    The replacement must be in-place, do not allocate extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding 
    outputs are in the right-hand column.
    
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        swap = False
        if nums:
            dic = {nums[-1]: len(nums)-1}
        pos = None
        def find(num, dic):
            maxi = float('inf')
            for key in dic:
                if key > num and key < maxi:
                    maxi = key
            return maxi
            
        for i in range(len(nums)-2, -1, -1):
            a = find(nums[i], dic)
            if a != float('inf'):
                nums[i], nums[dic[a]] = nums[dic[a]], nums[i]
                pos = i + 1
                swap = True
                break
            else:
                dic[nums[i]] = dic.get(nums[i], i)
        
        if swap:
            nums[pos:] = sorted(nums[pos:])
        else:
            nums.sort()