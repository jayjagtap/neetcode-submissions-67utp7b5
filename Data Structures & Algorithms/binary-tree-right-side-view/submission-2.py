# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

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
            BFS.append(level[-1])
        return BFS
        