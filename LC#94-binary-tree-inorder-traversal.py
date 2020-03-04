# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        
        
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
            
        
        output = []
        inorder(root)
        
        
        return output
