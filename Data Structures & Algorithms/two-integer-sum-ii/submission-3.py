class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        if left + right < target, we need to increase the number so left+=1, and right-=1 if target > left + right
        Time complexity: O(nlogn), space complexity: O(1)
        """

        left, right = 0, len(numbers)-1

        while left < right:
            num_sum = numbers[left] + numbers[right]
            if  num_sum == target:
                return [left+1, right+1]
            elif target < num_sum:
                right-=1
            else:
                left+=1

        return 
        