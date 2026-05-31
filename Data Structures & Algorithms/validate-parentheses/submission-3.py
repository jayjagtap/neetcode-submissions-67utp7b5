class Solution:
    def isValid(self, s: str) -> bool:
        """
        Space Complexity: O(n) since we need to create a new stack which can hold atmost n chars.
        1 pass, so time complexity: O(n)
        """

        stack = []

        match = {
            '}':'{',
            ']':'[',
            ')':'(',
            }

        for char in s:
            if stack and char in match and match[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
        
        