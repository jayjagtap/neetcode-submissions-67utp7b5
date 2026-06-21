class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(r*c) or O(nodes)
        Space Complexity: O(r*c) recursion stack takes up place
        """
        
        nr, nc = len(grid), len(grid[0])
        max_area, area = 0,0

        def dfs(node, area):
            
            r, c = node[0], node[1]
            if grid[r][c] == 0:
                return area
            grid[r][c] = 0
            
            nbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

            for r,c in nbors:
                if (r>=0 and r<nr) and (c>=0 and c<nc):
                    if grid[r][c] == 1:
                        area = dfs((r,c), area+1)
            return area
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    area = dfs((r,c), 1)
                    max_area = max(max_area, area)
        
        return max_area
                    

            

            
