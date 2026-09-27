# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Bottom up can solve it, we can calculate height from leaves and bubble it up, postorder. operation is return the max of left,right and add 1 for that level
        Time Complexity: O(n)
        Space Complexity: O(logn), worst case: O(n) for skewed tree
        """

        if not root: return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1+max(left, right)
