# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        total= 0
        head2= head
        while head2 is not None:
            total +=1
            head2= head2.next
        
        # print(total)
        # node_list[1].next= node_list[3]
        # return node_list[0]
    
        if total-n == 0:
            return head.next
        
        node= head
        for i in range(0, total-n):
            if i== total-n-1:
                try:
                    node.next= node.next.next
                except:
                    node.next= None
            
            else:
                node= node.next
        
        
        return head
        