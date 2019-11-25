# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev







if __name__ == '__main__':
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(3)
    l14 = ListNode(4)
    l15 = ListNode(5)

    l11.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15
    head = Solution().reverseList(l11)
    while(head):
        print(head.val)
        head = head.next