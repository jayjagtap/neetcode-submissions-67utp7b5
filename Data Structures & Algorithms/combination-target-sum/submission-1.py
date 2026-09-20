class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(n**(t/m))
        Space Complexity: O(t/m)

        """


        ans = []

        def backtrack(path, runningSum, start):

            # End condition
            if runningSum == target:
                ans.append(path[:])
                return
            elif runningSum > target:
                return
            
            for i in range(start, len(nums)): # Number of choices at each step is n
                choice = nums[i]
                path.append(choice)
                runningSum+=choice
                backtrack(path, runningSum, i) # recursion call total/smalles_element times, stack depth is t/m
                runningSum-=choice
                path.pop()
            
        backtrack([], 0, 0)

        return ans

        