# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lo, hi = -math.inf, math.inf
        def dfs(root, lo, hi):

            if not root: return True

            return (lo < root.val
                and hi > root.val 
                and dfs(root.left, lo, root.val)
                and dfs(root.right, root.val, hi))
        
        return dfs(root, lo, hi)
