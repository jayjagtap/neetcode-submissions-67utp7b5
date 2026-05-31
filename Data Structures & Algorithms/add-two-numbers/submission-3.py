# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, None)
        carry = 0
        curr = dummy

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            nodeSum = v1 + v2 + carry
            carry = nodeSum//10

            curr.next = ListNode(nodeSum%10)
            curr = curr.next

            if l1: l1=l1.next
            if l2: l2=l2.next
        
        if carry: curr.next = ListNode(1,None)
        
        return dummy.next


        