# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Using Hash Tables
        d = {}
        h1 = headA
        h2 = headB
        
        while h1 is not None:
            d[h1.val] = True
            h1 = h1.next
        while h2 is not None:
            if h2.val in d:
                return h2
            h2 = h2.next
        return None

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # using two pointers
        h1 = headA
        h2 = headB

        i = 0
        j = 0
        while i < 2 and j < 2:
            if h1 and h2:
                if h1.val == h2.val:
                    return h1
            # when the first list reaches the end, point h1 to second list
            if h1 is None:
                h1 = headB
                i += 1
            else:
                h1 = h1.next

            # when the second list reaches the end, point h2 to first list
            if h2 is None:
                h2 = headA
                j += 1
            else:
                h2 = h2.next

        return None



# a = Solution()
# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l1.next = l2
# l2.next = l3
# l3.next = l4


# l5 = ListNode(8)
# l6 = ListNode(9)
# l5.next = l6
# l6.next = l3

# a.getIntersectionNode(l1, l2)
# print(a.getIntersectionNode2(l1, l3).val)