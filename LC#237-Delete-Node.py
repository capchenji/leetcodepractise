# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        next_val = node.next.val
        temp = node.val
        node.val = next_val
        node.next.val = temp

        node.next = node.next.next
        
