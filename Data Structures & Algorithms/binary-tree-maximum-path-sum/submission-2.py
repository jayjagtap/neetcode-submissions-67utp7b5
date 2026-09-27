# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Bottom up. For each node record: maxSum = max(maxSum, L+R+node, L+node, R+node, node) and return max(node, L+node, R+node). Postorder traversal since its bottom up.
        Time Complexity: O(n)
        Space Complexity: O(logn), or worst case O(n)
        """

        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node: return 0

            L = dfs(node.left)
            R = dfs(node.right)

            maxSum = max(maxSum, L+node.val, R+node.val, L+R+node.val, node.val)
            return max(L+node.val, R+node.val, node.val)
        
        dfs(root)
        return maxSum

        