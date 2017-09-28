""" Sum Root to Leaf Numbers - 

    Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
    could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.

    For example,

        1
       / \
      2   3
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.

    Return the sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.numbers = []
        def inorder(root, sofar):
            if root:
                if root.left is not None and root.right is not None:
                    inorder(root.left, sofar + str(root.val))
                    inorder(root.right, sofar + str(root.val))
                elif root.left is not None:
                    inorder(root.left, sofar + str(root.val))
                elif root.right is not None:
                    inorder(root.right, sofar + str(root.val))
                else:
                    self.numbers.append(int(sofar + str(root.val)))
            else:
                if sofar != "":
                    self.numbers.append(int(sofar))
        inorder(root, "")
        #print(self.numbers)
        return sum(self.numbers)


# a = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)

# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5
# print(a.sumNumbers(t1))