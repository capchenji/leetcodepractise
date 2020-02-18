# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        p = None
        current = head
        
        while current is not None:
            next = current.next
            current.next = p
            p = current
            current = next
        head = p
        return head
