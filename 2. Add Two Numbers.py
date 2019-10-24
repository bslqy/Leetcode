# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Be mindful of the carry
Create dummy head
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        curr = dummyhead
        carry = 0
        while l1 or l2:
            if not l1:
                x = 0
            else:
                x = l1.val
            if not l2:
                y = 0
            else:
                y = l2.val
            s = x + y + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l1.next
        if carry > 0:
            curr.next = ListNode(1)

        return dummyhead.next




if __name__ == '__main__':
    pass