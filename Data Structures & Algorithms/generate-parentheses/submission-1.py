class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time Complexity: 
        "The tree has depth 2n and branches ≤ 2 ways, so a loose upper bound is O(4ⁿ·n). But pruning means every leaf is a valid string, 
        and the number of valid parenthesizations is the nth Catalan number, ≈ 4ⁿ/n^1.5. Times O(n) to build each string, that's O(4ⁿ/√n). 
        It's optimal because the output itself is Catalan-sized — you can't produce that many strings faster."
        """

        ans = []
        open_b = "("
        close_b = ")"

        def backtrack(path, counter):

            if len(path) == 2*n:
                if counter == 0:
                    ans.append("".join(path[:]))
                return

            for bracket in [open_b, close_b]:
               
                if bracket == open_b and counter >=n:
                    continue
                if bracket == close_b and counter <= 0:
                    continue

                path.append(bracket)
                backtrack(path, counter + 1 if bracket == open_b else counter-1)
                path.pop()

        backtrack([], 0)

        return ans