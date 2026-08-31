# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.solve(root)
    
    def solve(self, root):
        if not root:
            return root
        
        left = root.left
        right = root.right
        root.right = left
        root.left = right
        self.solve(root.left)
        self.solve(root.right)
        return root

        