""" Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

    Remove all elements from a linked list of integers that have value val.

    Example
    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # list is empty
        if head is None:
            return head

        # points cur to second node and prev to first node
        cur = head.next
        prev = head
        while cur is not None:
            # if val found in the list, remove it
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        # if first element in the list is val, remove it
        if head.val == val:
            head = head.next
        return head

# a = Solution()
# l1 = ListNode(10)
# l2 = ListNode(20)
# l3 = ListNode(10)
# l4 = ListNode(30)

# l1.next = l2
# l2.next = l3
# l3.next = l4
# b = a.removeElements(l1, 10)