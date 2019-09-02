# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        d[n] = True
        while self.someMaths(n) != 1:
            n = self.someMaths(n)
            if n in d: return False
            else: d[n] = True
        return True

    def someMaths(self, n):
        s, res = str(n), 0
        for l in s:
            res += int(l)**2
        return res
