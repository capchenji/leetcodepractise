# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        virtual_head = ListNode(-1)
        virtual_head.next = head
        
        pointer = virtual_head
        
        while pointer.next != None:
            if pointer.next.val == val:
                tmp = pointer.next
                pointer.next = tmp.next
            else:
                pointer = pointer.next
        
            
        
        return virtual_head.next