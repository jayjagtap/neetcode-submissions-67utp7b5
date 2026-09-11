import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(n)

        """

        stones = [-x for x in stones]
        heapq.heapify(stones) # heapify takes O(n)
        print(stones)

        while len(stones) >= 2:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones) # Pop takes O(nlogn),  heap peek is O(1)
            new_stone = stone1-stone2
            if new_stone != 0:
                heapq.heappush(stones, new_stone) # Heappush takes O(logn), n times means O(nlogn)


        return -stones[0] if stones else 0     