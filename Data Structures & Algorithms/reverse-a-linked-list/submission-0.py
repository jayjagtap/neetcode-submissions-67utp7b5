# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        A -> B -> C -> D -> None

        prev     curr.    nextNode.   LL
        None     A         B           None<-A B->...
        A        B         C           None <- A <- B C->D-> None
        B        C         D           None <- A <- B <- C D-> None
        C        D         None        None <- A <- B <- C <- D None
        
        return curr
        """

        # Empty Linked List

        curr = head
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


        