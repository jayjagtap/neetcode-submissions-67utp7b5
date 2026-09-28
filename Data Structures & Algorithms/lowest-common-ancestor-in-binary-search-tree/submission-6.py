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
        Time Complexity: O(h), since we only travel to one branch of a BST, we ignore the 
        other
        Space Complexity: O(h) where h is the height of the tree, O(n) for a skewed tree
        """

        if p.val > q.val: p,q = q, p

        def dfs(node):

            if not node: return

            if node == p:
                return p
            elif node == q:
                return q
            elif p.val < node.val and q.val > node.val:
                return node
            elif p.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)
        









                

        