from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        use Kahns algorithm
        """

        # Build graph and indegree.
        graph , indegree = defaultdict(list) , {x:0 for x in range(numCourses)}

        for edge in prerequisites:
            v1, v2 = edge[1], edge[0] # v1 -> v2, flip it
            graph[v1].append(v2)
            indegree[v2] += 1
        
        # Find all sources
        sources = deque([x for x in indegree if indegree[x] == 0])
        topo = []
        while sources:
            node = sources.popleft()
            topo.append(node)
            for nbor in graph[node]:
                indegree[nbor] -= 1
                if indegree[nbor] == 0:
                    sources.append(nbor)
        
        return len(topo) == numCourses
        







        