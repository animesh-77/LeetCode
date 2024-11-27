"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            print("here")
            return []
        
        elif len(root.children) > 0:
            children= []
            for child in root.children:
                children += self.postorder(child)
            return children + [root.val]
        elif len(root.children) == 0:
            
            return [root.val]
        