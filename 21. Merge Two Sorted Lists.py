
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy_head = ListNode(0)
        # Reference node
        cur = dummy_head

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            cur = cur.next
            # If l2 is exhausted
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = ListNode(l2.val)
            l2 = l2.next
            cur = cur.next

        return dummy_head.next



if __name__ == '__main__':
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l11.next = l12
    l12.next = l13
    l21.next = l22
    l22.next = l23

    cur = Solution().mergeTwoLists(l11,l21)
    while cur:
        print (cur.val)
        cur = cur.next
