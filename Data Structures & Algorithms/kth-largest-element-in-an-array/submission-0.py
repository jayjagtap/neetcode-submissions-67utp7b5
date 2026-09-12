import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approaches
        1. Sorting O(nlogn)
        2. Use min_heap of size k and keep adding to the heap. Time complexity O(nlogk) , space Complexity O(k)
        3. Use max_heap and keep popping k times. Time Complexity: O(n + klogn), Space complexity O(n)

        (3)'s time complexity is better than (2)s
        (2) is a streaming array and is preferred if all n numbers do not fit into memory

        Lets implement 2nd

        """

        min_heap = []

        for num in nums: # n times, O(nlogk)
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif min_heap[0] < num:
                heapq.heappop(min_heap) # O(logk)
                heapq.heappush(min_heap, num) # O(logk)


        return min_heap[0]