from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time Complexity: O(V+E) Adjacency List
        Space Compexity: O(V+E) Adjacencny list and O(V) dfs
        """

        # Build graph
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nbor in graph[node]:
                dfs(nbor)
        
        # Count connected components
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        
        return count

        