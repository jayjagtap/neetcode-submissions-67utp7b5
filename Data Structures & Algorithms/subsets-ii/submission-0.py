class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n*2^n)
        Space Complexity: Depth of stack, O(n)
        """

        ans = []
        size = len(nums)
        nums.sort() # O(nlogn)

        def backtrack(path, start):
            
            ans.append(path[:])  
            
            for i in range(start, size): # O(n*2^n)
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([],0)
    
        return ans
        