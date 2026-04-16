class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Start dfs traversal, for each 1, add islandCount to 1
        At each pass compare with maxCount and updated maxCount
        base condition, grid[r][c] = 0 and not out of bounds and not visited
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r,c, visited, islandCount):

            if (r < 0 or r >= rows
                or c < 0 or c >= cols
                or (r,c) in visited
                or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))

            nbors = [(r+1, c),(r-1,c),(r,c+1),(r, c-1)]
            area = 1

            for nei in nbors:
               area += dfs(nei[0], nei[1], visited, islandCount)
            
            return area
        
        # traverse the graph
        maxCount = 0

        for r in range(rows):
            for c in range(cols):
                islandCount = 0
                if grid[r][c] == 1:
                    islandCount = dfs(r,c,visited,islandCount)
                maxCount = max(maxCount, islandCount)
        
        return maxCount

            

            
