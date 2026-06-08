# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        nums = []
        
        def dfs(root, nums):
            
            if not root: return nums
        
            dfs(root.left, nums)
            nums.append(root.val)
            if len(nums) == k:
                return nums
            dfs(root.right, nums)

            return nums
        
        return dfs(root, nums)[k-1]

