class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            search = target - num
            if search in seen:
                return [seen[search], i]
            else:
                seen[num] = i
        
        return 

        