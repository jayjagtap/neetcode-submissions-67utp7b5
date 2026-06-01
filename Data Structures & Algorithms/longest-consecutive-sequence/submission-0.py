class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        maxLength = 0
        for num in nums: #O(n)
            length = 0
            print(num)
            if num-1 not in numSet: #O(1)    
                while num in numSet:
                    length+=1
                    num += 1
                    
            maxLength = max(maxLength, length)
    
        return maxLength
