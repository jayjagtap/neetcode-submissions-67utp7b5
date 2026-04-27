class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Sort the integers
        then have a left and right pointer traverse the array.
        if left + right < target, we need to increase the number so left+=1, and right-=1 if target > left + right
        Time complexity: O(nlogn), space complexity: O(1)
        """

        left, right = 0, len(numbers)-1

        nums = sorted(numbers)

        while left < right:
            num_sum = nums[left] + nums[right]
            if  num_sum == target:
                return [left+1, right+1]
            elif target < num_sum:
                right-=1
            else:
                left+=1

        return 
        