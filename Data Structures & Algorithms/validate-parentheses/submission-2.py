class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        match = {
            '}':'{',
            ']':'[',
            ')':'(',
            }

        for char in s:
            if stack and char in ['}', ']', ')'] and match[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
        
        