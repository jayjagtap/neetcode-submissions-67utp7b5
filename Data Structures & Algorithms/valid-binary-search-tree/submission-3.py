# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """
        Approach: Pre-order traversal since we are going top-down.
        We need to pass low and high down each node and check if low <= node <=high
        While going left, we need to update high with curr nodes value and
        while going right, we need to update the low with curr nodes value
        if any node does not satisy the condn return False
        """

        def dfs(node, low, high):

            if not node: return True
            if node.val<=low or node.val>=high: return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))











