# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        
        elif root.left is None:
            # right is not None
            return [root.val]+self.inorderTraversal(root.right)
        
        elif root.right is None:
            # left is not None
            return self.inorderTraversal(root.left)+ [root.val]
        
        else:
            # left and right both are not None
            return  self.inorderTraversal(root.left)+ [root.val]+ self.inorderTraversal(root.right)
        