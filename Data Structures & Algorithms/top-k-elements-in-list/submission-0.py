from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create a hashmap and then iterate over deque with max_length = 3
        (freq, char) sorted on freq
        """

        c = Counter(nums) # O(n)
        h = []
        for num, freq in c.items(): # O(nlogn)
            heapq.heappush(h, (-freq, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res
