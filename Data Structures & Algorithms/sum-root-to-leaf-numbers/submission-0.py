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

        leafNodes = []

        def dfs(node, path):
            
            if not node: return
            path += str(node.val)
            if not node.left and not node.right:
                leafNodes.append(path[:])
                return
             
            dfs(node.left,path)
            dfs(node.right,path)

        dfs(root, "")
        print(leafNodes)
        return sum([int(x) for x in leafNodes])
        