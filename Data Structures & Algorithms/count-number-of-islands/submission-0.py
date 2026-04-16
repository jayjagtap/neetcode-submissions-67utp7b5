class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        perform DFS search when you encounter a 1
        add the coordinate to visited set, increment + 1
        if you encounter a new 1 which is not visited, continue.
        """
        num_islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    self.dfs(r, c, grid, visited)
                    num_islands += 1

        return num_islands
    
    def dfs(self, r, c, grid: List[List[str]], visited: set):

        rows = len(grid)
        cols = len(grid[0])

        # Check out of bounds and base case
        if (r<0 or r >= rows       # row out of bounds
            or c < 0 or c >= cols  # col out of bounds
            or grid[r][c] == "0"     # water
            or (r,c) in visited):             # visited already
            return 
        
        visited.add((r,c))

        nbors = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]

        for nei in nbors:
            self.dfs(nei[0], nei[1], grid, visited)
        

    


        