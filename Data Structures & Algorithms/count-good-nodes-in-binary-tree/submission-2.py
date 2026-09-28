# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    """
    Approach: pre-order traversal (operation, left, right) , top down, send max value encountered down, record node
    Time Complexity: O(n)
    Space Complexity: O(logn), O(n) worst case (height of the tree)
    """
    def goodNodes(self, root: TreeNode) -> int:

        goodNodes = 0

        def dfs(node, maxVal):
            nonlocal goodNodes
            if not node: return
            if node.val >= maxVal:
                goodNodes+=1
            maxVal = max(node.val, maxVal)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal) 

        dfs(root, float('-inf'))           
        return goodNodes










