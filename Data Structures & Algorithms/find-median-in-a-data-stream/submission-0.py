import heapq
class MedianFinder:
    """
    Time Complexity Analysis
    Add operation:
        1. Add to heap O(logn)
        2. Rebalance O(logn)
        total: O(logn)
    find_median: O(1)
    Space Complexity: 2 heaps. O(n)
    """

    def __init__(self):
        self.right_heap = [] # min Heap
        self.left_heap = [] # max heap
        

    def addNum(self, num: int) -> None:
        
        # First number goes to left side
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
            return
        
        left_size, right_size = len(self.left_heap), len(self.right_heap)
        
        if num > -self.left_heap[0]: # move to right_heap
            heapq.heappush(self.right_heap, num)
            right_size+=1
            # rebalance
            if right_size-left_size > 1:
                swap_element = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -swap_element)
        else:
            heapq.heappush(self.left_heap, -num)
            left_size+=1
            #rebalance

            if left_size-right_size > 1:
                swap_element = heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, -swap_element)

        
        
    def findMedian(self) -> float:
        left_size, right_size = len(self.left_heap), len(self.right_heap)
        if left_size == right_size:
            return (-self.left_heap[0] + self.right_heap[0])/2
        
        return -self.left_heap[0] if left_size > right_size else self.right_heap[0]
        
        