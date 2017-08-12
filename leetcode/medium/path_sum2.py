""" Path Sum II - https://leetcode.com/problems/path-sum-ii

    Given a binary tree and a sum, find all root-to-leaf paths where 
    each path's sum equals the given sum.

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    return
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def inorder(root, path, sofar, target, all_paths):
            if root:
                if root.left is None and root.right is None:
                    if sofar + root.val == target:
                        all_paths.append(path + [root.val])
                else:
                    inorder(root.left, path + [root.val], sofar + root.val, target, all_paths)
                    inorder(root.right, path+ [root.val], sofar + root.val, target, all_paths)
                    
        path = []
        sofar = 0
        all_paths = []
        inorder(root, path, sofar, sum, all_paths)
        return all_paths

# a = Solution()
# n1 = TreeNode(5)
# n2 = TreeNode(4)
# n3 = TreeNode(8)
# n4 = TreeNode(11)
# n5 = TreeNode(13)
# n6 = TreeNode(4)
# n7 = TreeNode(7)
# n8 = TreeNode(2)
# n9 = TreeNode(5)
# n10 = TreeNode(1)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n4.left = n7
# n4.right = n8
# n3.left = n5
# n3.right = n6
# n6.left = n9
# n6.right = n10

# a.pathSum(n1, 22)