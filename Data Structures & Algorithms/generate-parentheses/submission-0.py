class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        open_b = "("
        close_b = ")"

        def backtrack(path, counter):

            if counter < 0 or counter > n:
                return

            if len(path) == 2*n:
                if not counter:
                    ans.append("".join(path[:]))
                return

            for bracket in [open_b, close_b]:
               
                path.append(bracket)
                if bracket == open_b:
                    backtrack(path, counter+1)
                else:
                    backtrack(path, counter-1)
                
                path.pop()

        backtrack([], 0)

        return ans