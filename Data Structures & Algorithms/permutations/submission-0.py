class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity:
        n*n! Since this is permutation, n! chocies are possible and each choice needs to checked(n)

        Space Complexity:
        Auxiliary Space: O(n) Depth of the stack
        Output Space: O(n!)
        """

        permutations = []
        size = len(nums)

        def backtrack(path, remaining):

            if len(path) == size:
                permutations.append(path[:]) # store the copy if end condn is satisfied.
                return

            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])  
                path.pop()
                
        
        backtrack([], nums)    

        return permutations
        