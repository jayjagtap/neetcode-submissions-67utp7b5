# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy, prev, carry = ListNode(0, l1), ListNode(0, l1), 0
        connectL2 = True
        while l1 or l2:
            if l1 and l2:
                nodeSum = l1.val + l2.val + carry
                carry = nodeSum//10
                l1.val = nodeSum%10
                prev = l1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                nodeSum = l1.val + carry
                carry = nodeSum//10
                l1.val = nodeSum%10
                prev = l1
                l1 = l1.next
            else:
                if connectL2:
                    prev.next = l2
                    connectL2 = False
                nodeSum = l2.val + carry
                l2.val = nodeSum%10
                carry = nodeSum//10
                prev = l2
                l2 = l2.next

        if carry:
            prev.next = ListNode(1,None)
        
        return dummy.next

        