""" Flatten Binary Tree to Linked List - 
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

    Given a binary tree, flatten it to a linked list in-place.

    For example,
    Given

             1
            / \
           2   5
          / \   \
         3   4   6
    The flattened tree should look like:
       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flat(root):
            if root:
                stl, enl = flat(root.left)
                right = root.right

                if enl is not None:
                    enl.right = root.right
                    root.right = stl
                
                root.left = None
                strr, enr = flat(right)

                if enr is not None:
                    return root, enr
                elif enl is not None:
                    return root, enl
                return root, root
            return None, None
        flat(root)

    def print_tree(self, root):
        if root:
            print(root.val)
            self.print_tree(root.right)


# a = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)
# t6 = TreeNode(6)
# t1.left = t2
# t2.left = t3
# t2.right = t4
# t1.right = t5
# t5.right = t6

# a.flatten(t1)
# a.print_tree(t1)