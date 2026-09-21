class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexit: 
            - Each node has 3/4 branches.
            - Loop once over all digits.
            - set count 3**n and less than 4**n

            3**n <= O(n) <4**n
        
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

        def backtrack(path, start):

            if len(path) == size:
                if path:
                    ans.append("".join(path[:]))
                return
            
            for i in range(start, size): # outside digit 
                for letter in digit_map[digits[i]]: # letters
                    path.append(letter)  
                    backtrack(path, i+1)
                    path.pop()
        
        backtrack([],0)

        return ans
        