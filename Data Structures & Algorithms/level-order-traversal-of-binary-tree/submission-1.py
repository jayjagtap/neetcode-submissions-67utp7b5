# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Level Orfer Traversal can be done using queue's FIFO.
        At each level, we append the children of the current node to the queue to 
        maintain the level order traversal

        Time Complexity: O(n) since we visit each node
        Space Complexity: In a fully balanced tree, max elements at any point in the queue 
        will be n/2 so space complexity is O(N)
        """

        BFS = []
        if not root: return BFS
        Q = deque([root])
        
        while Q:
            level = []
            levelSize = len(Q)
            for _ in range(levelSize):
                curr = Q.popleft()
                level.append(curr.val)
                if curr.left: Q.append(curr.left)
                if curr.right: Q.append(curr.right)
            BFS.append(level)
        return BFS





        