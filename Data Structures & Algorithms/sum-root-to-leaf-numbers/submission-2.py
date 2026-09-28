# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Hybrid DFS. The number built so far comes DOWN (num*10 + val, preorder work);
the sum of leaf numbers comes back UP (postorder work). Leaves return their full number.
Time: O(n). Space: O(h), which is O(log n) balanced and O(n)
        """

        def dfs(node, num):
            if not node: return 0
            num = num*10 + node.val
            if not node.left and not node.right:
                return num
             
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)
        