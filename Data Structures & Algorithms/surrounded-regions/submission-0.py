from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Approach: Flip the condn. I can use multi-source BFS and mark all non-surrounded islands with
        N, whatever remains are surrounded islands. replace the Ns with Xs once done.
        Time Complexity: O(r*cc)
        Space Complexity: O(r*c)
        """

        nr, nc = len(board), len(board[0])

        # BFS starting seeds
        seeds = set()

        # Check left and right borders
        for r in range(nr):
            if board[r][0] == "O":      seeds.add((r, 0))
            if board[r][nc - 1] == "O":  seeds.add((r, nc - 1))

        # Check top and bottom borders
        for c in range(nc):
            if board[0][c] == "O":      seeds.add((0, c))
            if board[nr - 1][c] == "O":  seeds.add((nr - 1, c))

        Q = deque(seeds)
        visited = set(seeds)

        while Q:
            r, c = Q.popleft()
            board[r][c] = "N"

            nbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nbor_r, nbor_c in nbors:
                if 0<=nbor_r<nr and 0<=nbor_c<nc and board[nbor_r][nbor_c] == "O":
                    Q.append((nbor_r, nbor_c))
                    visited.add((nbor_r, nbor_c))
        
        # Update remaining surrounded regions by X and replce Ns by 0s in second pass

        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "N":
                    board[r][c] = "O"

        







        