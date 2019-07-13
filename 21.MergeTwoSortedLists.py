# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        t1 = l1
        t2 = l2
        t = head
        while t1 and t2:
            if t1.val > t2.val:
                temp = ListNode(t2.val)
                t.next = temp
                t = t.next
                t2 = t2.next
            elif t1.val < t2.val:
                temp = ListNode(t1.val)
                t.next = temp
                t = t.next
                t1 = t1.next
            else:
                temp1 = ListNode(t1.val)
                t.next = temp1
                t = t.next
                temp2 = ListNode(t2.val)
                t.next = temp2
                t = t.next
                t1 = t1.next
                t2 = t2.next
        if t1:
            while t1:
                temp = ListNode(t1.val)
                t1 = t1.next
                t.next = temp
                t = t.next
        if t2:
            while t2:
                temp = ListNode(t2.val)
                t2 = t2.next
                t.next = temp
                t = t.next
        return head.next
