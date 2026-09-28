# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach: In a BST, inorder (left root right) order will give the sorted order
        we can do dfs with inorder traversal.
        
        Time Complexity: O(h+k) where k, worst case O(n), h is the height and you will need
        to go to the leftmost node, so h will be constant.
        Space Complexity: O(h)
        """

        counter = 0
        ans = None
        def dfs(node):

            nonlocal counter, ans
            if not node or counter > k: return 

            dfs(node.left)
            counter += 1

            if counter == k:
                ans = node.val
            dfs(node.right)
                
        
        dfs(root)

        return ans
            
            


        




