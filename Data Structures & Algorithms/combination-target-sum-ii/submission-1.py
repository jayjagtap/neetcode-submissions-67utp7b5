class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(number of branches* work per node) = O(n*n!)
        Space Complexity: Stack Depth = number of total elements, since we dont want to repeat = O(n)

        """

        ans = []
        candidates.sort()
        size = len(candidates)
        
        def backtrack(path, start, runningSum):

            if runningSum == target:
                ans.append(path[:]) # Store a copy
            elif runningSum > target:
                return
            
            for i in range(start, size):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
                choice = candidates[i]
                path.append(choice)
                backtrack(path, i+1, runningSum+choice)
                path.pop()
            
        backtrack([],0,0)

        return [list(x) for x in ans] # O(n)
