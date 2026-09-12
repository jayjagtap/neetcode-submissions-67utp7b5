import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n + klogn)
        Space Complexity: O(n)
        """

        # make a hashmap to get count
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num]+=1

        freq_map = [(-count, num) for num,count in freq_map.items()] # O(n)
        heapq.heapify(freq_map) # O(n)

        topk = []
        while len(topk) < k:   # O(k log n)
            count, num = heapq.heappop(freq_map)
            topk.append(num)

        return topk
