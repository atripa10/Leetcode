# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # create a temp node to point to head
        temp = head
        count =0
        # get lenght of the list
        while temp:
            count+=1
            temp=temp.next
        temp = head
        i=0
        while i != count/2:
            temp=temp.next
            i+=1
        return temp
