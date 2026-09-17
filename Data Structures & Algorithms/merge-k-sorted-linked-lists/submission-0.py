# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Diff ways to solve this:
        1. Merge 2 lists sequentially until it cover all lists. Time Complexity: O(N*k) , Space Complexity: O(1)
        2. Use a min_heap of size k and add smallest node in the heap and pop until heap is empty. Time Complexity: O(NlogK), space complexity: O(k)
        """

        min_heap = []
        dummy = ListNode()
        # Initialization Add 1 element each from the list

        counter = 0
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, counter, node)) # O(logk)
                counter+=1
              
        
        curr = dummy
        while min_heap:
            _ , _ , top  = heapq.heappop(min_heap)  # O(log k)
            curr.next = top
            curr = top
            if top and top.next:
                counter+=1
                heapq.heappush(min_heap, (top.next.val, counter, top.next))  # O(logk)
        
        return dummy.next

