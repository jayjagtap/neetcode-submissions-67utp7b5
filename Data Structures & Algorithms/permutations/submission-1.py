class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity:
        n*n! Since this is permutation, n! chocies are possible and each choice needs to checked(n)

        Space Complexity:
        Auxiliary Space: O(n) Depth of the stack + used array
        Output Space: O(n!)
        """

        permutations = []
        size = len(nums)

        used = [0 for x in nums]
        def backtrack(path, used):

            if len(path) == size:
                permutations.append(path[:]) # store the copy if end condn is satisfied.
                return

            for i in range(size):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = 1
                backtrack(path, used)  
                used[i] = 0
                path.pop()
                
        
        backtrack([], used)    

        return permutations
        