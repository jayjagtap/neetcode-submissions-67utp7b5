# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Approach: Post order traversal, bubble up if either of the node found upwards,
        when a node finds both the nodes are found, return that node.
        Time Complexity: O(n)
        Space Complexity: O(logn), O(n) worst case scenario
        """

        def dfs(node):

            if not node: return None

            left = dfs(node.left)
            right = dfs(node.right)

            if (node == p or node == q): return node
            elif left and right: return node
            elif left: return left
            else: return right

            
        return dfs(root)
