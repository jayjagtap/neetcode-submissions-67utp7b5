from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-Source BFS. Initial Seeds is 2
        Time Complexity: O(r.c)
        Space Complexity: O(r*c), worst case Q space
        """

        nr, nc = len(grid), len(grid[0])
        delta = [(0,1), (0,-1), (1,0), (-1,0)]
        Q = deque()
        mins = 0
        fresh_fruits = 0
        
        # Add initial seeds: rotten fruits (2)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 2:
                    Q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1

        # Start BFS one level at 1 time and count the mins:
        while Q:
            level_size = len(Q)
            
            fruit_spoiled_this_round = False
            for _ in range(level_size):
                r, c = Q.popleft()
                
                for dr, dc in delta:
                    if 0 <= r+dr <nr and 0 <= c+dc <nc and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        Q.append((r+dr,c+dc))
                        fresh_fruits-=1
                        fruit_spoiled_this_round = True
                    
            if fruit_spoiled_this_round:
                mins += 1
        
        return mins if fresh_fruits == 0 else -1










        