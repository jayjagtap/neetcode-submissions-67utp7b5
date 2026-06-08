# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return 0, True

            left_h, left_b = dfs(root.left)
            #short circuit at first occurence
            if not left_b: return 0, False

            right_h, right_b = dfs(root.right)
            # Short Circuit at first occurence
            if not right_b: return 0, False

            return max(left_h, right_h) + 1, abs(left_h-right_h) <= 1

        _ , balance = dfs(root)

        return balance

        