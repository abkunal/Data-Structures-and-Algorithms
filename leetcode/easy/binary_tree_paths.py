""" Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/

    Given a binary tree, return all root-to-leaf paths.

    For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
    All root-to-leaf paths are:

    ["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # inorder traversal of binary tree
        def inorder(root, path, all_paths):
            if root:
                if root.left is None and root.right is None:
                    path += str(root.val)
                    all_paths.append(path)
                else:
                    inorder(root.left, path + str(root.val) + "->", all_paths)
                    inorder(root.right, path + str(root.val) + "->", all_paths)
        
        path = ""
        all_paths = []
        inorder(root, path, all_paths)
        return all_paths

# a = Solution()
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n5 = TreeNode(5)

# n1.left = n2
# n1.right = n3
# n2.right = n5
# a.binaryTreePaths(n1)