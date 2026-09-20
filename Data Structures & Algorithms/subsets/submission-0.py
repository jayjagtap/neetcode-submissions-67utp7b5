class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Use backtracking to record all subsets.
        Time Complexity: n*2**n ( Number of nodes(solutions)* depth(work on each node))
        Space Complexity: 
        Auxialiary space: O(n) recursion stack depth
        Output space: 2**n (to hold the answer)
        """

        subsets = []

        def backtrack(path, idx): # (path, remaning)

            subsets.append(path[:]) # Store a copy

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([],0)

        return subsets
