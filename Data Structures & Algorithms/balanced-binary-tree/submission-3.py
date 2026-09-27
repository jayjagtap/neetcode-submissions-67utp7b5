# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True

        def dfs(node):

            nonlocal isBalanced
            if not node: return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            isBalanced = isBalanced and (abs(lh-rh)<=1)
            return 1 + max(lh, rh)
        
        dfs(root)

        return isBalanced