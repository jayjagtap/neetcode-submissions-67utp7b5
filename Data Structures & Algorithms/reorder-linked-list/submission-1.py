# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        This is O(n2)time and O(1) solution but this works and is better than no solution :)
        """

        curr = head

        while curr:
            curr.next = self.reverse(curr.next)
            curr = curr.next
        
        return curr
    
    
    def reverse(self, head):

        prev , curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev




        
        