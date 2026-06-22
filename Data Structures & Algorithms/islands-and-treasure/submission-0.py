from collections import deque
import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Multi-source BFS — seed the queue with all chests, expand in lockstep.
        Time:  O(R · C) — each cell visited once
        Space: O(R · C) — queue can hold all cells in the worst case
        """

        nr, nc = len(grid), len(grid[0])
        Q = deque()
        INF = 2**31-1
        # Seed queue with treasure chests
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 0:
                    Q.append((r,c))
        
        # Do a BFS
        while Q:
            r, c = Q.popleft()

            nbors = [(r+1,c),(r-1,c),(r,c+1),(r, c-1)]
            for nbor_r, nbor_c in nbors:
                if 0 <= nbor_r < nr and 0 <= nbor_c <nc and grid[nbor_r][nbor_c] == INF:
                    grid[nbor_r][nbor_c] = grid[r][c]+1
                    Q.append((nbor_r, nbor_c))
        



        
        