# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Apply bottom up approach, use postorder, and travel up. operation: switch left and right pointers.
        Time Complexity: O(n)
        Space Complexity: O(height) == O(logn)
        """

        if not root: return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left , root.right = root.right, root.left

        return root




    
        