# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkMirror(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None or p.val != q.val:
                return False
            
            return checkMirror(p.left, q.right) and checkMirror(p.right, q.left)
    
        return checkMirror(root, root)