# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Find the centre of the linkedlist.
        Reverse the second half of the list
        Interleave the nodes.

        Time Complexity: O(n), Space Complexity: O(1)
        """

        # Find middle. slow and fast pointer, fast moves twice as fast

        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = self.reverse(slow.next)

        # Terminate list 1. 
        slow.next = None

        # Interleave
        dummy = ListNode(0, head)
        curr, l1 = dummy, head

        alternate = 1
        while l2:
            if alternate:
                curr.next = l1
                alternate = 0
                l1 = l1.next  
            else:
                curr.next = l2
                alternate = 1
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1
    
    def reverse(self, head):
        prev, curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev        


"""
This is O(n2)time and O(1) solution but this works and is better than no solution :)


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

"""