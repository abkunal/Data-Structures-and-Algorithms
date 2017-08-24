""" Average of Levels in Binary Tree - 
    https://leetcode.com/problems/average-of-levels-in-binary-tree/

    Given a non-empty binary tree, return the average value of the nodes on 
    each level in the form of an array.

    Example 1:
    
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, 
    and on level 2 is 11. Hence return [3, 14.5, 11].
    
    Note:
    The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def inorder(root, level, avg):
            if root:
                if level in avg:
                    avg[level].append(root.val)
                else:
                    avg[level] = [root.val]
                inorder(root.left, level + 1, avg)
                inorder(root.right, level + 1, avg)
        
        avg = {}
        inorder(root, 0, avg)

        if avg == {}:
            return []

        res = []
        for i in range(max(avg)+1):
            x = sum(avg[i]) / len(avg[i])
            res.append(x)
        return res


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

# print(a.averageOfLevels(None))