# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Approach: use is same tree on the nodes where the root value matches. Pre-order traversal: operation, go left, go right and recurse. So max nodes traversed == m and subroot checking atmost n nodes
        Time Complexity: O(m*n), check the subtree for each node, worst case is O(m+n) since we break early for a no matching node
        Space O(m+n)

        """

        def isSameTree(p, q):
            """
            Time Complexity: O(n), n is number of nodes in a smaller tree
            """

            if (p and not q) or (q and not p): return False
            if not p and not q: return True

            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 
        
        if not root: return False
       
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

        

        
        