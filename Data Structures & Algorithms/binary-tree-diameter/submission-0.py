# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter = 0

        def calcheight(root):
            if root is None:
                return 0
            rightHeight = calcheight(root.right)
            leftHeight = calcheight(root.left)
            
            d = leftHeight + rightHeight
            self.maxdiameter = max(self.maxdiameter, d)

            return 1 + max(rightHeight, leftHeight)
        
        calcheight(root)
        return self.maxdiameter