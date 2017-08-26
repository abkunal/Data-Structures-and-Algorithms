""" Binary Tree Tilt - https://leetcode.com/problems/binary-tree-tilt

    Given a binary tree, return the tilt of the whole tree.

    The tilt of a tree node is defined as the absolute difference between 
    the sum of all left subtree node values and the sum of all right subtree 
    node values. Null node has tilt 0.

    The tilt of the whole tree is defined as the sum of all nodes' tilt.

    Example:
    Input: 
             1
           /   \
          2     3
    
    Output: 1
    
    Explanation: 
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1
    
    Note:

    The sum of node values in any subtree won't exceed the range of 32-bit integer.
    All the tilt values won't exceed the range of 32-bit integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tilt(root, tilts):
            if root:
                left = tilt(root.left, tilts)
                right = tilt(root.right, tilts)

                tilts.append(abs(left-right))
                return root.val + left + right
            return 0
        tilts = []
        tilt(root, tilts)
        return sum(tilts)


# a = Solution()

# t1 = TreeNode(91)
# t2 = TreeNode(542)
# t3 = TreeNode(32)
# t4 = TreeNode(345)
# t5 = TreeNode(67)

# t1.left = t2
# t1.right = t3
# t2.left = t4
# t3.right = t5

# print(a.findTilt(t1))