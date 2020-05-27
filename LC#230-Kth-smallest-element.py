# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        count = 0
        vals = []

        def inorder(node, vals):
            if node is None:
                return vals
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)
            return vals

        return inorder(root, vals)[k-1]
