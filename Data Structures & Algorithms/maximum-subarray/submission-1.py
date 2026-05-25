import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        If all nos are +ve, return array sum
        If all nos are -ve, return smallest num

        Combination.
        Whenever the sliding window sum goes less than 0, discard prev array and start new
        Time Complexity: O(n)
        Space Complexity; O(1)
        """

        maxSum, currSum = -math.inf, 0
        i = 0

        while i<len(nums):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
            i+=1

        return maxSum


