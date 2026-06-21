"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time Complexity: O(V+E)
        Spcae Complexity: O(V+E) Recursion stack
        """

        if not node: return node
        visited = {}

        def dfs(node):

            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone

            for nbor in node.neighbors:
                clone.neighbors.append(dfs(nbor))
            
            return clone
        
        dfs(node)
    
        return visited[node]
            

        