# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxVal):

            if not root: return 0

            good = 1 if root.val >= maxVal else 0

            return (good + dfs(root.left, max(root.val, maxVal)) + 
            dfs(root.right, max(root.val, maxVal)))

        return dfs(root, -math.inf)

            