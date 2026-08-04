# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            leftHeight = check_height(node.left)
            if leftHeight == -1:
                return -1
            
            rightHeight = check_height(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return max(leftHeight, rightHeight) + 1
        
        return check_height(root) != -1
            
            
            

