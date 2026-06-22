class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Strategy: Flip the condition. Start from nodes which are connected to ocean and check for neighboring nodes
        which are greater than them (water flows from those nodes to the curr nodes)
        Time Complexity: O(r.c) (run dfs twice over the grid)
        Space Complexity: O(r.c) 2 sets to hold island cells
        """
        
        pacific = set()
        atlantic = set()
        nr, nc = len(heights), len(heights[0])

        def dfs(node, reachable):
            if node in reachable:
                return
            r, c = node[0], node[1]
            reachable.add(node)
            nbors = [(r+1,c), (r-1,c), (r,c+1),(r,c-1)]

            for nbor_r, nbor_c in nbors:
                if 0<=nbor_r<nr and 0<=nbor_c<nc and heights[nbor_r][nbor_c] >= heights[r][c]:
                    dfs((nbor_r, nbor_c), reachable)

        # water from 0th row and 0th col always flows to pacific
        starts = set()
        starts.update((0,c) for c in range(nc))
        starts.update((r,0) for r in range(nr))
        # perform dfs traversal from the points
        for node in starts:
            dfs(node, pacific)

        # water from nth row and nth col always flows to atlantic
        starts = set()
        starts.update((x,nc-1) for x in range(nr))
        starts.update((nr-1, x) for x in range(nc))

        for node in starts:
            dfs(node, atlantic)
        
        return list(pacific & atlantic)
        

            

        


        