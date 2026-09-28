# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Approach: pre-order traversal since we want to do a top-down approach, and send the value down till the leaf node, once leaf node is reached, record the value.
        Time Complexity: O(n)
        Space Complexity: O(logn), O(n) worst case
        """

        def dfs(node, num):
            if not node: return 0
            num = num*10 + node.val
            if not node.left and not node.right:
                return num
             
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)
        