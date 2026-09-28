# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach: Since it a binary search tree, we can traverse the tree in pre-order
        until we stumble opon a node where it branches out to 2 different direction
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of the tree, O(n) for a skewed tree
        """

        val1 = p.val
        val2 = q.val

        if val1 > val2: val1, val2 = val2, val1
        def dfs(node):

            if not node: return
            if node == p or node == q or (val1 < node.val and val2 > node.val):
                return node
            return dfs(node.left) or dfs(node.right)

        return dfs(root)









                

        