""" Minimum Absolute Difference in BST - 
    https://leetcode.com/problems/minimum-absolute-difference-in-bst

    Given a binary search tree with non-negative values, find the minimum 
    absolute difference between values of any two nodes.

    Example:

    Input:

       1
        \
         3
        /
       2

    Output:
    1

    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
    Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Solution with O(n) time and O(n) space
        """
        # find the inorder sequence of all elements in bst
        self.sequence = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.sequence.append(root.val)
                inorder(root.right)
                
        inorder(root)

        # find the absolute diff between adjacent nodes and take the minimum
        mini = self.sequence[1] - self.sequence[0]
        for i in range(1, len(self.sequence)-1):
            if self.sequence[i+1] - self.sequence[i] < mini:
                mini = self.sequence[i+1] - self.sequence[i]
        
        return mini

    def getMinimumDifference2(self, root):
        """ Solution with O(n) time and O(1) space """

        # find the minimum absolute difference between adjacent nodes according to
        # to inorder sequence during tree traversal
        self.mini = float('inf')
        self.last_seen = None
        
        def inorder(root):
            if root:
                inorder(root.left)
                if self.last_seen:
                    self.mini = min(self.mini, root.val - self.last_seen.val)
                self.last_seen = root
                inorder(root.right)
        
        inorder(root)
        return self.mini        
        
# a = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(3)
# t3 = TreeNode(2)

# t1.right = t2
# t2.left = t3
# a.getMinimumDifference2(t1)