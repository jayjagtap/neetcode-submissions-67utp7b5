# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(h)
        """

        def dfs(root):
            if not root: return 0 , 0

            left_h , left_d = dfs(root.left)
            right_h, right_d = dfs(root.right)

            return max(left_h, right_h) + 1 , max(left_h + right_h, left_d, right_d)
        
        _ , maxD = dfs(root)

        return maxD




