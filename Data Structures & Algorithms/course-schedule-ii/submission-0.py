from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Can be solved both using Kahns indegree algorithm and
        dfs solution
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        """

        # Build graph
        graph = defaultdict(list)

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        finished, currPath, post = set(), set(), []

        def dfs(node):
            if node in currPath:
                return True
            if node in finished:
                return False
            
            currPath.add(node)
            nbors = graph[node]
            for nbor in nbors:
                if dfs(nbor):
                    return True
            currPath.remove(node)
            finished.add(node)
            post.append(node)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
                
        return post[::-1]

        