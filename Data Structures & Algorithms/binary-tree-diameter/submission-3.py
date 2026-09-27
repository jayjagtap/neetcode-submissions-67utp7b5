# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Postorder height problem. return max(Lh, Rh) but maxD = max(maxD, Lh+Rh) since it can be a non-root node but we can only return one branch above to form a path
        Time Complexity: O(n)
        Space Complexity: O(logn), worst case O(n)
        """

        maxD = 0

        def dfs(node):

            nonlocal maxD
            if not node: return 0

            Lh = dfs(node.left)
            Rh = dfs(node.right)

            maxD = max(maxD, Lh+Rh)
            return 1+ max(Lh, Rh)
        
        dfs(root)

        return maxD


