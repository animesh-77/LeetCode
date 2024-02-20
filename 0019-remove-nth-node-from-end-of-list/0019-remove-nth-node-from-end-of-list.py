# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node_list= [head]
    
        while head.next is not None:
            node_list.append(head.next)
            head= head.next
            
        # node_list[1].next= node_list[3]
        # return node_list[0]
    
    
    
        if n == len(node_list):
            if len(node_list)>=2:
                return node_list[1]
            else:
                return None
        
        if n==1:
            if len(node_list)==1:
                return None
            else:
                node_list[-n-1].next= None
                return node_list[0]
            
        node_list[-n-1].next= node_list[-n+1]
        
        return node_list[0]
        
            
        