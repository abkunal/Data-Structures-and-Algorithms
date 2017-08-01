""" Path Sum - https://leetcode.com/problems/path-sum/
    
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path
    such that adding up all the values along the path equals the given sum.

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # store path sum of all the leaf nodes
        def inorder(root, path, level, sofar):
            if root:
                sofar += root.val
                if root.left is None and root.right is None:
                    path.append((level, sofar, root.val))

                inorder(root.left, path, level + 1, sofar)
                inorder(root.right, path, level + 1,sofar)

        path = []
        inorder(root, path, 1, 0)
        
        # check leaf nodes for sum
        for i in path:
            if i[1] == sum:
                return True
        return False


a = Solution()

t1 = TreeNode(1)
t2 = TreeNode(-2)
t3 = TreeNode(-3)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(-2)
t7 = TreeNode(-1)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t4.left = t7

#print(a.hasPathSum(t1, 2))