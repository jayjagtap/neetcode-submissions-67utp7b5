class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Start once you find first 1, do dfs and replace 1s with 0, updated count
        Do same for next 1

        Time Complexity: (n2)
        """

        num_islands = 0
        visited = set()
        nr, nc = len(grid) , len(grid[0])

        def dfs(node):
            r, c = node[0], node[1]
            if node in visited or grid[r][c] == "0":
                return
            
            visited.add(node)
            grid[r][c] = "0"
            nbors = [(r+1,c), (r-1, c), (r, c+1), (r, c-1)]
            for r, c in nbors:
                if (r>=0 and r<nr) and (c>=0 and c<nc):
                    dfs((r,c))

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands+=1
                    dfs((r,c))
    
        return num_islands

