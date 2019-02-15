# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        result=l1value=l2value = 0

        linkresult = ListNode(None)
        prelinkresult = linkresult
        header = linkresult

        carry = 0
        tmpvalue = 0
        while l1!=None or l2!=None or carry:
            linkresult = ListNode(None)
            l1value = l1.val if l1!=None else 0
            l2value = l2.val if l2!=None else 0
            if l1value+l2value+carry>=10:
                result = (l1value+l2value+carry)%10
                carry = 1
            else:
                result = (l1value+l2value+carry)
                carry = 0
            linkresult.val = result
            prelinkresult.next = linkresult
            prelinkresult = linkresult
            l1 = l1.next if l1!=None else l1
            l2 = l2.next if l2!=None else l2


        return header.next
            
