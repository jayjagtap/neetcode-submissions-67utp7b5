import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time Complexity: O(n + klogn)
        Space Complexity: O(n)
        """

        distance = [(math.sqrt(x**2 + y**2), (x,y)) for [x,y] in points]
        print(distance)

        heapq.heapify(distance) # O(n)

        closest = []
        for i in range(k): # total: O(klogN)
            d, p = heapq.heappop(distance) # O(logn)
            closest.append(p)

        return closest
        
        