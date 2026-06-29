from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time and Space
        """

        # Build Graph
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nbor in graph[node]:
                if nbor == parent:
                    continue
                if not dfs(nbor, node):
                    return False
        
            return True
           
            
            

        
        return dfs(0, -1) and len(visited) == n
        