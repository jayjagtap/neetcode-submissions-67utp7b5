# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Bottom Up, record if tree is balanced at every node on the path up and return the height of that node
        Time Complexity: O(n)
        Space Compexity: O(logn), worst case O(n) when tree is skewed
        """

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