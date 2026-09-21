class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexit: 
            - Each node has 3/4 branches.
            - Loop once over all digits.
            - set count 3**n and less than 4**n

            Time Complexity: O(n*4**n)
        
        Space Complexity:
            - Depth of the tree == number of digits.

            O(n)
        """

        ans = []

        digit_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        size = len(digits)

        def backtrack(path, idx):

            if idx == size:
                if path:
                    ans.append("".join(path[:]))
                return
            
            for letter in digit_map[digits[idx]]:
                path.append(letter)
                backtrack(path, idx+1)
                path.pop()
            
        backtrack([],0)

        return ans
        