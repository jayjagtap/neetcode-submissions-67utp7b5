# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(n) since we visit all n nodes.
        Space Complexity: O(h), O(logn), balanced O(n)
        """

        BFS = []
        if not root: return BFS
        Q = deque([root])
        
        while Q:
            levelSize = len(Q)
            curr = None
            for _ in range(levelSize):
                curr = Q.popleft()
                if curr.left: Q.append(curr.left)
                if curr.right: Q.append(curr.right)
            BFS.append(curr.val)
        return BFS
        