# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        
        def dfs(root, s):
            if root is None:  # Base case: empty node, return False
                return False
            s += root.val  # Increment the sum by the current node's value
            # If it's a leaf and the sum matches targetSum, return True
            if root.left is None and root.right is None and s == targetSum:
                return True
            # Recursively search the left and right subtrees
            return dfs(root.left, s) or dfs(root.right, s)
        
        return dfs(root, 0)