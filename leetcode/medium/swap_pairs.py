""" Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs

    
    Given a linked list, swap every two adjacent nodes and return its head.

    For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space. You may not modify the 
    values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # when list is empty or contains a single element
        if not head or head.next is None: return head

        # swap first two elements, prev and cur are the swapped nodes
        # point is used to connect the list to cur when it is swapped by prev
        prev = head
        cur = head.next
        prev.next= cur.next
        cur.next = prev
        head = cur
        point = prev
        prev = prev.next
        if prev:
            cur = prev.next
        else:
            return head

        while cur is not None:
            prev.next = cur.next
            cur.next = prev
            point.next = cur
            point = prev
            prev = prev.next
            if prev:
                cur = prev.next
            else:
                break

        return head

    def swapPairs2(self, head):
        """ An amazing value replacing solution by a fellow coder. Loved it! """
        cur = head
        while cur is not None and cur.next is not None:
            cur_val = cur.val
            cur.val = cur.next.val
            cur.next.val =cur_val
            cur = cur.next
            cur = cur.next
        return head

    def print_list(self, head):
        cur = head
        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next
        print()


# a = Solution()
# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l5 = ListNode(5)
# l6 = ListNode(6)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
# a.print_list(l1)
# a.print_list(a.swapPairs2(l1))