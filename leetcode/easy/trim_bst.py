# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node, L, R):
            if node:
                if node.val > R:
                    return trim(node.left, L, R)
                elif node.val < L:
                    return trim(node.right, L, R)
                else:
                    node.left = trim(node.left, L, R)
                    node.right = trim(node.right, L, R)
                    return node
        
        return trim(root,L,R)


# a = Solution()
# t1 = TreeNode(0)
# t2 = TreeNode(1)
# t3 = TreeNode(2)

# t2.left = t1
# t2.right = t3
# a.trimBST(t2, 1,2)