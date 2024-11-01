# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        
        if list1.val < list2.val:
            ret_list = ListNode(list1.val, None)
            list1 = list1.next
        else:
            ret_list = ListNode(list2.val, None)
            list2 = list2.next
            
        if list1 is None:
            ret_list.next = list2
            return ret_list
            
        if list2 is None:
            ret_list.next = list1
            return ret_list
        first_node= ret_list
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                ret_list.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                ret_list.next = ListNode(list2.val, None)
                list2 = list2.next
            ret_list = ret_list.next

        if list1 is None:
            ret_list.next = list2
            return first_node

        if list2 is None:
            ret_list.next = list1
            return first_node
            
            
            
        