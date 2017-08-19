""" Sum of left leaves - https://leetcode.com/problems/sum-of-left-leaves

    Find the sum of all left leaves in a given binary tree.

    Example:

        3
       / \
      9  20
        /  \
       15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root, pos):
            if root:
                if root.left is None and root.right is None and pos == "l":
                    return root.val
                else:
                    return inorder(root.left, "l") + inorder(root.right, "r")
            else:
                return 0
        
        x = inorder(root, "m")
        return x


# a = Solution()
# t1 = TreeNode(3)
# t2 = TreeNode(9)
# t3 = TreeNode(20)
# t4 = TreeNode(15)
# t5 = TreeNode(7)

# t1.left = t2
# t1.right = t3
# t3.left = t4
# t3.right = t5

# print(a.sumOfLeftLeaves(t1))