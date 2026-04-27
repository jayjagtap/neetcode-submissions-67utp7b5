class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        One way is to solve using set(), which has a time complexity of O(1) and space complexity of O(1)

        Other way is to sort it and traverse, time complexity O(nlogn), space complexity O(1)
        
        """

        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False