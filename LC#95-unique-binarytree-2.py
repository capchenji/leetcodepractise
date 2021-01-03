# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        else:
            return self.cal([i for i in range(1,n+1)])
    
    def cal(self, lst):
        if not lst: return [None];
        res = []
        for i in range(len(lst)):
            for left in self.cal(lst[0:i]):
                for right in self.cal(lst[i+1:]):
                    node, node.left, node.right = TreeNode(lst[i]), left, right
                    res += [node]
                    
        return res
        