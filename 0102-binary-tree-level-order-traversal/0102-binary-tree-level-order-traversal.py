# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode], depth: int= 0) -> List[List[int]]:
        
        from collections import deque
        
        if root is None:
            return []
        
        result= []
        
        Dqueue= deque([root])
        
        while len(Dqueue) > 0:
            level_values= []
            level_len= len(Dqueue)
            
            for _ in range(level_len):
                
                current_node= Dqueue.popleft()
                
                level_values.append(current_node.val)
                
                if current_node.left is not None:
                    Dqueue.append(current_node.left)
                
                if current_node.right is not None:
                    Dqueue.append(current_node.right)
                
            result.append(level_values)
            
        print(f"{result=}")
        return result
        