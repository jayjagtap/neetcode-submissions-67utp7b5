import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # make a hashmap to get count
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num]+=1

        topk = []
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, count in freq_map.items():
            buckets[count].append(num)
        
        for i in range(n, 0, -1):
            if buckets[i] and len(topk)<k:
                for num in buckets[i]:
                    topk.append(num)
                    if len(topk) == k:
                        return topk

        return topk
