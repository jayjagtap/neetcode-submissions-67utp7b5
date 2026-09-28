# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Level Orfer Traversal can be done using queue's FIFO.
        At each level, we append the children of the current node to the queue to 
        maintain the level order traversal

        Time Complexity: O(n) since we visit each node
        Space Complexity: In a fully balanced tree, max elements at any point in the queue 
        will be n/2 so space complexity is O(N)

        DFS approach is also possible. Time Complexity: O(n) and Space : O(h), worst case
        O(n) for a skewed tree
        """

        res = []
        def dfs(node, depth):

            if not node: return
            
            if len(res) < depth+1:
                res.append([node.val])
            else:
                res[depth].append(node.val)
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
    
        dfs(root, 0)

        return res
            

        





        