# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 == [0]:
            return l2
        if l2 == [0]:
            return l1
        
        HEAD = ListNode()
        
        carry, current_head= 0, HEAD
        
        while (l1 is not None) or (l2 is not None) or carry>0:
            
            val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            # print(val, l1.val, l2.val)
            
            carry, digit=  val//10, val%10
            
            current_head.next= ListNode(val= digit,)
            
            current_head= current_head.next
            
            l1= l1.next if l1 is not None else None
            l2= l2.next if l2 is not None else None
            
            
        return HEAD.next
            